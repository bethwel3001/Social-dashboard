from flask import Flask, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Dummy data endpoint
@app.route('/api/metrics')
def get_metrics():
    dummy_data = {
        "twitter": {
            "followers": 1500,
            "likes": 3200,
            "engagement_rate": 4.5
        },
        "instagram": {
            "followers": 2300,
            "likes": 4500,
            "engagement_rate": 3.8
        }
    }
    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)