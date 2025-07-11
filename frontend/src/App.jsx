import { useState, useEffect } from "react";
import "./App.css";
import NoteForm from "./components/NoteForm";
import NoteList from "./components/NoteList";
import { getNotes, deleteNote } from "./services/api";
import { Plus, X } from "lucide-react";

function App() {
  const [notes, setNotes] = useState([]);
  const [noteToEdit, setNoteToEdit] = useState(null);
  const [showForm, setShowForm] = useState(false);

  //traemos la data desde la api
  const fetchNotes = () => {
    getNotes().then((res) => setNotes(res.data));
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  const handleToggleForm = () => {
    setShowForm((prev) => !prev);
    if (showForm) {
      setNoteToEdit(null);
    }
  };

  const handleEditNote = (note) => {
    setNoteToEdit(note);
    setShowForm(true);
  };

  const handleDeleteNote = async (id) => {
    await deleteNote(id);
    fetchNotes(); // refresh
  };

  const handleNoteSubmitted = () => {
    fetchNotes(); // refresh
    setNoteToEdit(null);
    setShowForm(false);
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 space-y-6">
      <h1 className="text-3xl font-bold text-center text-gray-100">
        🧠 AI NoteGen
      </h1>

      {/* "Add New Task" */}
      <div className="mb-6">
        <button
          onClick={handleToggleForm}
          className="flex items-center gap-2 bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-xl transition-all duration-200 transform hover:scale-105 shadow-lg hover:shadow-xl"
        >
          {showForm ? (
            <>
              <X className="h-5 w-5" /> Cancel{" "}
            </>
          ) : (
            <>
              <Plus className="h-5 w-5" /> Add New Task
            </>
          )}
        </button>
      </div>

      {/* The form */}
      {showForm && (
        <NoteForm
          onNoteSubmitted={handleNoteSubmitted}
          noteToEdit={noteToEdit}
        />
      )}

      {/* Note List */}
      <NoteList
        notes={notes}
        onEdit={handleEditNote}
        onDelete={handleDeleteNote}
      />
    </div>
  );
}

export default App;
