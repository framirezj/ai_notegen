import axios from "axios";

const apiurl = import.meta.env.VITE_API_URL;

const api = axios.create({
  baseURL: apiurl,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const getNotes = () => api.get("/notes");
export const createNote = (data) => api.post("/notes/", data);
export const deleteNote = (id) => api.delete(`/notes/${id}`);
export const updateNote = (id, data) => api.put(`/notes/${id}`, data);

export const login = ({ email, password }) =>
  api.post(
    "/login",
    new URLSearchParams({
      username: email,
      password: password,
    }),
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    }
  );
