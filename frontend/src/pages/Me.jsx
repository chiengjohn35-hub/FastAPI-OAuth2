import { useAuth } from "../Context/Authcontext";

export default function Me() {
  const { user } = useAuth();

  if (!user) {
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <div className="spinner-border text-primary" role="status"></div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-md-6">

          <div className="card shadow p-4">
            <h2 className="text-center mb-3">Your Profile</h2>

            <ul className="list-group list-group-flush">
              <li className="list-group-item">
                <strong>Name:</strong> {user.name}
              </li>
              <li className="list-group-item">
                <strong>Email:</strong> {user.email}
              </li>
              <li className="list-group-item">
                <strong>Verified:</strong> {user.is_verified ? "Yes" : "No"}
              </li>
              <li className="list-group-item">
                <strong>ID:</strong> {user.id}
              </li>
            </ul>
          </div>

        </div>
      </div>
    </div>
  );
}
