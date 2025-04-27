export default function MetricCards({ data }) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 className="text-gray-500 dark:text-gray-300">Twitter Followers</h3>
          <p className="text-2xl font-bold">{data?.twitter?.followers}</p>
        </div>
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 className="text-gray-500 dark:text-gray-300">Instagram Likes</h3>
          <p className="text-2xl font-bold">{data?.instagram?.likes}</p>
        </div>
      </div>
    )
  }