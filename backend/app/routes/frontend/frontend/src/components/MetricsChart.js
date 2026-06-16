import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

function MetricsChart({ data }) {
  return (
    <div
      style={{
        background: "#0f172a",
        padding: "20px",
        borderRadius: "20px",
        marginBottom: "30px"
      }}
    >
      <h2 style={{ color: "#38bdf8" }}>
        Live Memory Usage
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="memory"
            stroke="#38bdf8"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default MetricsChart;
