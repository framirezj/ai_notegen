import { createContext, useContext, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token"));

  const loginUser = (token) => {
    setToken(token);
    localStorage.setItem("token", token);
  }

  const logout = () => {
    setToken(null);
    localStorage.removeItem("token");
  }

  return(
    <AuthContext.Provider value={{ token, isAuthenticated: !!token, loginUser, logout }}>
      {children}
    </AuthContext.Provider>
  )


}

//hook personalizado
export const useAuth = () => useContext(AuthContext)

