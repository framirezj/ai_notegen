import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { login } from "../services/api";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const { loginUser } = useContext(AuthContext);

  const navigate = useNavigate();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    // Limpiar el error cuando el usuario empieza a escribir de nuevo
    if (error) setError(null);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    // Limpiar el error cuando el usuario empieza a escribir de nuevo
    if (error) setError(null);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      const response = await login({ email, password });
      console.log("Login successful:", response.data);
      loginUser(response.data.access_token);
      navigate("/notes");
    } catch (error) {
      console.error("Error logging in:", error);
      setError("Credenciales inválidas. Inténtalo de nuevo.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-[80%] max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Login</h2>
      <form onSubmit={handleLogin}>
        <div className="mb-4">
          <label
            className="block text-sm font-medium text-gray-700 mb-1"
            htmlFor="email"
          >
            Email
          </label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={handleEmailChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div className="mb-4">
          <label
            className="block text-sm font-medium text-gray-700 mb-1"
            htmlFor="password"
          >
            Password
          </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        <button
          type="submit"
          disabled={isLoading}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md transition-all duration-200 transform hover:scale-105 shadow-lg hover:shadow-xl"
        >
          {isLoading ? "Iniciando sesión..." : "Login"}
        </button>
      </form>
    </div>
  );
};

export default Login;
