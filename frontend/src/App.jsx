import { AuthProvider } from "./context/AuthContext";
import Login from "./pages/Login";
import "./App.css";
import NotesPage from "./pages/NotesPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<NotesPage />} />
          <Route path="/login" element={<Login />} />
          {/*falta la page de register */}
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
