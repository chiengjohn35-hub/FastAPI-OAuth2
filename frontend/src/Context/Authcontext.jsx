import { createContext, useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getMe } from "../services/auth";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Check token on first load
  useEffect(() => {
    async function fetchUser() {
      const token = localStorage.getItem("access_token");
      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const res = await getMe();
        setUser(res.data);
      } catch {
        localStorage.removeItem("access_token");
      }

      setLoading(false);
    }

    fetchUser();
  }, []);

  function logout() {
    localStorage.removeItem("access_token");
    setUser(null);
    navigate("/login");   // 🔥 redirect after logout
  }

  return (
    <AuthContext.Provider value={{ user, setUser, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}

