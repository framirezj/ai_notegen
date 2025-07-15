import axios from "axios";

const apiurl = import.meta.env.VITE_API_URL;

const api = axios.create({
    baseURL: apiurl
});

export const getNotes = () => api.get("/notes");
export const createNote = (data) => api.post("/notes/", data)
export const deleteNote = (id) => api.delete(`/notes/${id}`)
export const updateNote = (id, data) => api.put(`/notes/${id}`, data)