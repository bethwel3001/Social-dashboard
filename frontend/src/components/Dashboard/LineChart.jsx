import 'chart.js/auto';
import { Line } from 'react-chartjs-2';

export default function LineChart({ data }) {
  const chartData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr'],
    datasets: [
      {
        label: 'Twitter Followers',
        data: [1200, 1350, 1420, 1500],
        borderColor: '#1DA1F2',  // Twitter blue
        fill: false,
      },
      {
        label: 'Instagram Followers',
        data: [1800, 2000, 2200, 2300],
        borderColor: '#E1306C',  // Instagram pink
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
}