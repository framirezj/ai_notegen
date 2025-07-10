import { useState } from "react";
import { createNote } from "../services/api";
import { Plus } from "lucide-react";

const NoteForm = ({ onNoteCreated }) => {
  //variables de estado
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [showForm, setShowForm] = useState(false);

  //metodos
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title || !content) return;

    await createNote({ title, content });
    setTitle("");
    setContent("");
    onNoteCreated();
  };

  //retorno
  return (
    <>
      {/* Add Task Button */}
      <div className="mb-6">
        <button
          onClick={() => setShowForm(!showForm)}
          className="flex items-center gap-2 bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-xl transition-all duration-200 transform hover:scale-105 shadow-lg hover:shadow-xl"
        >
          <Plus className="h-5 w-5" />
          Add New Task
        </button>
      </div>

      {/* formulario */}
      {showForm && (
        <form
          onSubmit={handleSubmit}
          className="space-y-4 p-5 bg-gray-800 shadow rounded-xl"
        >
          <h3 className="text-white text-xl font-semibold">New Task</h3>
          <label className="text-gray-300 block text-sm font-medium">
            Title
          </label>
          <input
            type="text"
            placeholder="Enter task title..."
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="border p-4 w-full text-gray-300 rounded-lg bg-gray-700 placeholder-gray-400"
          />
          <label className="text-gray-300 block text-sm font-medium">
            Content
          </label>
          <textarea
            placeholder="Enter task details..."
            value={content}
            rows={4}
            onChange={(e) => setContent(e.target.value)}
            className="border px-4 py-3 w-full text-gray-300 rounded-lg bg-gray-700 placeholder-gray-400"
          />
          <button className="bg-blue-500 px-5 hover:bg-blue-600 text-white py-3 rounded-lg transition-all duration-200 transform hover:scale-105 font-medium">
            Add Task
          </button>
        </form>
      )}
    </>
  );
};

export default NoteForm;
