import React, { useEffect, useState } from 'react';
import { Line } from 'recharts';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/ga/data")
      .then(res => res.json())
      .then(data => setData(data.visits.map((v, i) => ({ name: i, value: v }))));
  }, []);

  return (
    <div>
      <h1>GA4 Dashboard</h1>
      <LineChart width={400} height={300} data={data}>
        <Line type="monotone" dataKey="value" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default App;
