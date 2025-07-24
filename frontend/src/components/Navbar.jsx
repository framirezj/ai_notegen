import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import { LogOut } from "lucide-react";

const Navbar = () => {
  //const { logout } = useContext(AuthContext)
  //con hook personalizado
  const { logout } = useAuth();

  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav className="bg-gray-800 shadow p-4 px-6 flex justify-between items-center mb-6">
        <h1 className="text-xl font-bold text-gray-100">📝 🧠 AI NoteGen</h1>
      <button onClick={handleLogout} className="flex items-center gap-2 bg-gray-700 text-gray-300 hover:text-red-700 hover:bg-red-300 px-4 py-2 rounded-lg transition-all duration-200">
        <LogOut className="w-5 h-5"/>
        <span className="hidden sm:inline">Cerrar sesión</span>
      </button>
    </nav>
  );
};

export default Navbar;
