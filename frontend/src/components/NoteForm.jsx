import { useState, useEffect } from "react";
import { createNote, updateNote } from "../services/api";

const NoteForm = ({ onNoteSubmitted, noteToEdit }) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    if (noteToEdit) {
      setTitle(noteToEdit.title);
      setContent(noteToEdit.content);
    } else {
      setTitle("");
      setContent("");
    }
  }, [noteToEdit]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title || !content) return;

    const noteData = { title, content };

    if (noteToEdit) {
      await updateNote(noteToEdit.id, noteData);
    } else {
      await createNote(noteData);
    }

    onNoteSubmitted();
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4 p-5 bg-gray-800 shadow rounded-xl"
    >
      <h3 className="text-white text-xl font-semibold">
        {noteToEdit ? "Edit Task" : "New Task"}
      </h3>
      <label className="text-gray-300 block text-sm font-medium">Title</label>
      <input
        type="text"
        placeholder="Enter task title..."
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-4 w-full text-gray-300 rounded-lg bg-gray-700 placeholder-gray-400"
      />
      <label className="text-gray-300 block text-sm font-medium">Content</label>
      <textarea
        placeholder="Enter task details..."
        value={content}
        rows={4}
        onChange={(e) => setContent(e.target.value)}
        className="border px-4 py-3 w-full text-gray-300 rounded-lg bg-gray-700 placeholder-gray-400"
      />
      <button className="bg-blue-500 px-5 hover:bg-blue-600 text-white py-3 rounded-lg transition-all duration-200 transform hover:scale-105 font-medium">
        {noteToEdit ? "Update Task" : "Add Task"}
      </button>
    </form>
  );
};

export default NoteForm;