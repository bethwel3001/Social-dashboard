import { useState, useEffect } from 'react';
import axios from 'axios';
import MetricCards from './components/Dashboard/MetricCards';
import LineChart from './components/Dashboard/LineChart';

export default function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/metrics')
      .then(res => setData(res.data))
      .catch(console.error);
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-8">
      <h1 className="text-3xl font-bold mb-8 dark:text-white">Social Analytics</h1>
      {data ? (
        <>
          <MetricCards data={data} />
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow mt-8">
            <LineChart />
          </div>
        </>
      ) : (
        <p className="dark:text-white">Loading...</p>
      )}
    </div>
  );
}