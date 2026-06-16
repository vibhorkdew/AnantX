import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { backButtonStyle } from "../styles/navigationStyles";

function Monitoring() {
    const navigate = useNavigate();
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("http://localhost:8000/api/monitoring")
            .then(res => res.json())
            .then(data => setData(data));
    }, []);

    if (!data) {
        return <h2 style={{ color: "white" }}>Loading...</h2>;
    }

    const runningContainers = data.containers.filter(
        container => container.status === "running"
    ).length;

    return (
        <div
            style={{
                minHeight: "100vh",
                background: "#020617",
                color: "white",
                padding: "30px"
            }}
        >
            {/* BUTTON CONTROLS */}
            <div style={{ display: "flex", gap: "15px", marginBottom: "25px" }}>
                <button
                    onClick={() => navigate("/dashboard")}
                    style={backButtonStyle}
                >
                    ← Back to Dashboard
                </button>

                <button
                    onClick={() => window.open("http://localhost:3001", "_blank")}
                    style={{
                        padding: "10px 16px",
                        borderRadius: "10px",
                        border: "1px solid #38bdf8",
                        cursor: "pointer",
                        background: "transparent",
                        color: "#38bdf8",
                        fontWeight: "600",
                        transition: "0.2s"
                    }}
                >
                    📊 Open Grafana Dashboard
                </button>
            </div>

            <h1
                style={{
                    fontSize: "42px",
                    marginBottom: "10px",
                    color: "#38bdf8"
                }}
            >
                Container Monitoring Center
            </h1>

            <p
                style={{
                    color: "#94a3b8",
                    marginBottom: "40px"
                }}
            >
                Real-Time Infrastructure & Container Health Monitoring
            </p>

            {/* SUMMARY CARDS */}
            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fit,minmax(250px,1fr))",
                    gap: "20px",
                    marginBottom: "40px"
                }}
            >
                <div
                    style={{
                        background: "#0f172a",
                        padding: "25px",
                        borderRadius: "18px",
                        border: "1px solid #38bdf8"
                    }}
                >
                    <h3>Total Containers</h3>
                    <h1 style={{ color: "#38bdf8" }}>{data.count}</h1>
                </div>

                <div
                    style={{
                        background: "#0f172a",
                        padding: "25px",
                        borderRadius: "18px",
                        border: "1px solid #22c55e"
                    }}
                >
                    <h3>Running Containers</h3>
                    <h1 style={{ color: "#22c55e" }}>{runningContainers}</h1>
                </div>

                <div
                    style={{
                        background: "#0f172a",
                        padding: "25px",
                        borderRadius: "18px",
                        border: "1px solid #f59e0b"
                    }}
                >
                    <h3>Platform Health</h3>
                    <h1 style={{ color: "#f59e0b" }}>100%</h1>
                </div>

                <div
                    style={{
                        background: "#0f172a",
                        padding: "25px",
                        borderRadius: "18px",
                        border: "1px solid #a855f7"
                    }}
                >
                    <h3>Status</h3>
                    <h1 style={{ color: "#a855f7" }}>ACTIVE</h1>
                </div>
            </div>

            {/* TABLE HEADER */}
            <div
                style={{
                    background: "#0f172a",
                    padding: "20px",
                    borderRadius: "18px 18px 0 0",
                    borderBottom: "1px solid #1e293b"
                }}
            >
                <h2 style={{ margin: 0, color: "#38bdf8" }}>Active Containers</h2>
            </div>

            {/* TABLE */}
            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                    background: "#0f172a",
                    borderRadius: "0 0 18px 18px",
                    overflow: "hidden"
                }}
            >
                <thead>
                    <tr style={{ background: "#111827" }}>
                        <th style={{ padding: "16px", textAlign: "left" }}>
                            Container Name
                        </th>
                        <th style={{ padding: "16px", textAlign: "left" }}>
                            Status
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {data.containers.map((container, index) => (
                        <tr
                            key={index}
                            style={{ borderBottom: "1px solid #1e293b" }}
                        >
                            <td style={{ padding: "16px", fontWeight: "600" }}>
                                {container.name}
                            </td>
                            <td style={{ padding: "16px" }}>
                                <span
                                    style={{
                                        padding: "8px 14px",
                                        borderRadius: "999px",
                                        fontWeight: "600",
                                        background:
                                            container.status === "running"
                                                ? "#14532d"
                                                : "#7f1d1d",
                                        color:
                                            container.status === "running"
                                                ? "#22c55e"
                                                : "#ef4444"
                                    }}
                                >
                                    ● {container.status.toUpperCase()}
                                </span>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <div
                style={{
                    textAlign: "center",
                    marginTop: "30px",
                    color: "#64748b",
                    fontSize: "12px"
                }}
            >
                © 2026 AnantX Team | AnantX DevSecOps Platform
            </div>
        </div>
    );
}

export default Monitoring;