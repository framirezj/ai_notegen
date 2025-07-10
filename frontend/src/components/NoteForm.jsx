import { useState } from "react";
import { createNote } from "../services/api";

const NoteForm = ({onNoteCreated}) => {
  //variables de estado
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  //metodos
  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (!title || !content) return;

    await createNote({ title, content })
    setTitle("")
    setContent("")
    onNoteCreated();
  };

  //retorno
  return (
    <form onSubmit={handleSubmit}
      className="space-y-4 p-4 bg-white shadow rounded"
    >
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-2 w-full"
      />
      <textarea
        placeholder="Content"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        className="border p-2 w-full"
      />
      <button className="bg-blue-500 text-white px-4 py-2 rounded">Save Note</button>
    </form>
  );
};

export default NoteForm;
