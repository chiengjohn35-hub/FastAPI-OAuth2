import { Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import ProtectedRoute from "./components/ProtectedRoute";
import Me from "./pages/Me";
import Navbar from "./components/Navbar";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<h1 className="text-center mt-5">Welcome to FastAPI Oauth2</h1>}/>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route
          path="/me"
          element={
            <ProtectedRoute>
              <Me />
            </ProtectedRoute>
          }
        />
      </Routes>
    </>
  );
}

export default App;

