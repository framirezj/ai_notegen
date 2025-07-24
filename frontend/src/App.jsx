import { AuthProvider } from "./context/AuthContext";
import Login from "./pages/Login";
import "./App.css";
import NotesPage from "./pages/NotesPage";
import ProtectedRoute from "./components/ProtectedRoute";
import { Routes, Route } from "react-router-dom";
import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "./context/AuthContext";

function App() {
  const { isAuthenticated } = useContext(AuthContext);

  return (
    <>
      <Routes>
        <Route
          path="/"
          element={
            isAuthenticated ? (
              <Navigate to="/notes" />
            ) : (
              <Navigate to="/login" />
            )
          }
        />

        <Route
          path="/login"
          element={isAuthenticated ? <Navigate to="/notes" /> : <Login />}
        />

        <Route element={<ProtectedRoute />}>
          <Route path="/notes" element={<NotesPage />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
