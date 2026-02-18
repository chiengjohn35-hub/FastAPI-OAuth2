import api from "./apis";

export function register(data) {
  return api.post("/auth/register", data);
}

export function login(email, password) {
  const form = new FormData();
  form.append("username", email);
  form.append("password", password);

  return api.post("/auth/token", form);
}

export function getMe() {
  return api.get("/auth/me");
}
