import React, { useState } from "react";
import {
    BrowserRouter,
    Routes,
    Route,
    Navigate,
    Outlet
} from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Containers from "./pages/Containers";
import Vulnerabilities from "./pages/Vulnerabilities";
import Monitoring from "./pages/Monitoring";
import AIAssistant from "./pages/AIAssistant";
import Threats from "./pages/Threats";

const RequireAuth = () => {
    const token = localStorage.getItem("token");

    if (!token) {
        return <Navigate to="/login" replace />;
    }

    return <Outlet />;
};

function App() {
    const [authenticated, setAuthenticated] = useState(
        !!localStorage.getItem("token")
    );

    const isAuthenticated =
        authenticated || !!localStorage.getItem("token");

    const handleLoginSuccess = () => {
        setAuthenticated(true);
    };

    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/login"
                    element={
                        <Login
                            setAuthenticated={
                                handleLoginSuccess
                            }
                        />
                    }
                />

                <Route element={<RequireAuth />}>
                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />
                    <Route
                        path="/dashboard/threats"
                        element={<Threats />}
                    />
                    <Route
                        path="/dashboard/vulnerabilities"
                        element={<Vulnerabilities />}
                    />
                    <Route
                        path="/dashboard/containers"
                        element={<Containers />}
                    />
                    <Route
                        path="/dashboard/ai"
                        element={<AIAssistant />}
                    />
                    <Route
                        path="/dashboard/monitoring"
                        element={<Monitoring />}
                    />
                </Route>

                <Route
                    path="/"
                    element={
                        isAuthenticated ? (
                            <Navigate to="/dashboard" replace />
                        ) : (
                            <Navigate to="/login" replace />
                        )
                    }
                />

                <Route
                    path="*"
                    element={
                        isAuthenticated ? (
                            <Navigate to="/dashboard" replace />
                        ) : (
                            <Navigate to="/login" replace />
                        )
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
