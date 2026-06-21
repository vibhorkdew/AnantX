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
import Logs from "./pages/Logs";

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

                {/* Public Route */}
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

                {/* Protected Routes */}
                <Route element={<RequireAuth />}>

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/threats"
                        element={<Threats />}
                    />

                    <Route
                        path="/vulnerabilities"
                        element={<Vulnerabilities />}
                    />

                    <Route
                        path="/containers"
                        element={<Containers />}
                    />

                    <Route
                        path="/monitoring"
                        element={<Monitoring />}
                    />

                    <Route
                        path="/logs"
                        element={<Logs />}
                    />

                    <Route
                        path="/ai"
                        element={<AIAssistant />}
                    />

                </Route>

                {/* Default Route */}
                <Route
                    path="/"
                    element={
                        isAuthenticated ? (
                            <Navigate
                                to="/dashboard"
                                replace
                            />
                        ) : (
                            <Navigate
                                to="/login"
                                replace
                            />
                        )
                    }
                />

                {/* Fallback */}
                <Route
                    path="*"
                    element={
                        isAuthenticated ? (
                            <Navigate
                                to="/dashboard"
                                replace
                            />
                        ) : (
                            <Navigate
                                to="/login"
                                replace
                            />
                        )
                    }
                />

            </Routes>
        </BrowserRouter>
    );
}

export default App;