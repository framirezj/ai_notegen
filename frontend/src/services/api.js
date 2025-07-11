import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000"
});

export const getNotes = () => api.get("/notes");
export const createNote = (data) => api.post("/notes/", data)
export const deleteNote = (id) => api.delete(`/notes/${id}`)
export const updateNote = (id, data) => api.put(`/notes/${id}`, data)