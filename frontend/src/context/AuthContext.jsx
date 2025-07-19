import { createContext, useContext, useState, useEffect } from "react";

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
    <AuthContext.Provider value={{ token, loginUser, logout }}>
      {children}
    </AuthContext.Provider>
  )


}

