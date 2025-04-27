import { useState, useEffect } from 'react'
import axios from 'axios'
import MetricCards from './components/Dashboard/MetricCards'

export default function App() {
  const [data, setData] = useState(null)

  useEffect(() => {
    axios.get('http://localhost:5000/api/metrics')
      .then(res => setData(res.data))
      .catch(console.error)
  }, [])

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-8">
      <h1 className="text-3xl font-bold mb-8 dark:text-white">Social Analytics</h1>
      {data ? <MetricCards data={data} /> : <p>Loading...</p>}
    </div>
  )
}