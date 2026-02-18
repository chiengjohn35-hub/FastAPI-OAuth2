import { useState } from "react";
import { login, getMe } from "../services/auth";
import { useAuth } from "../Context/Authcontext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { setUser } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const res = await login(email, password);
      localStorage.setItem("access_token", res.data.access_token);

      const me = await getMe();
      setUser(me.data);

      navigate("/me");
    } catch (err) {
      alert(err.response?.data?.detail || "Login failed");
    }
  }

  return (
    <div className="d-flex justify-content-center align-items-center vh-100 bg-light">
      <div className="card shadow p-4" style={{ width: "380px" }}>
        <h2 className="text-center mb-3">Welcome Back</h2>
        <p className="text-center text-muted mb-4">Log in to your account</p>

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <button type="submit" className="btn btn-primary w-100">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
