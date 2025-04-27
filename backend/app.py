from flask import Flask, jsonify, request
from flask_caching import Cache
import snscrape.modules.twitter as sntwitter
from functools import wraps
import time

app = Flask(__name__)
cache = Cache(app, config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 3600  # Cache for 1 hour
})

# Rate limiter decorator
def rate_limit(max_per_minute=30):
    def decorator(f):
        calls = []
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls_in_window = [t for t in calls if t > now - 60]
            
            if len(calls_in_window) >= max_per_minute:
                return jsonify({
                    "error": "Rate limit exceeded",
                    "retry_after": 60 - (now - calls_in_window[0])
                }), 429
                
            calls.append(now)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/v1/metrics', methods=['GET'])
@rate_limit(max_per_minute=30)
@cache.cached(query_string=True)
def get_metrics():
    platform = request.args.get('platform', type=str)
    username = request.args.get('username', type=str)
    
    if not platform or not username:
        return jsonify({"error": "Missing platform or username"}), 400
    
    try:
        if platform.lower() == 'twitter':
            # Get user profile data
            scraper = sntwitter.TwitterUserScraper(username)
            user = next(scraper.get_items()).user
            
            # Get latest 3 tweets for engagement metrics
            tweets = []
            for i, tweet in enumerate(scraper.get_items()):
                if i >= 3: break
                tweets.append({
                    "likes": tweet.likeCount,
                    "retweets": tweet.retweetCount,
                    "replies": tweet.replyCount
                })
            
            avg_engagement = {
                "likes": sum(t['likes'] for t in tweets) / len(tweets) if tweets else 0,
                "retweets": sum(t['retweets'] for t in tweets) / len(tweets) if tweets else 0
            }
            
            return jsonify({
                "platform": platform,
                "username": username,
                "metrics": {
                    "followers": user.followersCount,
                    "following": user.friendsCount,
                    "engagement_rate": avg_engagement,
                    "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
                }
            })
            
        else:
            return jsonify({"error": "Unsupported platform"}), 400
            
    except StopIteration:
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)