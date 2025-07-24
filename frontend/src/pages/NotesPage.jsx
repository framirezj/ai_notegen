import { useState, useEffect } from "react";
import { getNotes, deleteNote } from "../services/api";
import NoteForm from "../components/NoteForm"
import NoteList from "../components/NoteList"
import AddTask from "../components/AddTask"

const NotesPage = () => {
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


      <AddTask handleToggleForm={handleToggleForm} showForm={showForm} />

      {showForm && (
        <NoteForm
          onNoteSubmitted={handleNoteSubmitted}
          noteToEdit={noteToEdit}
        />
      )}

      <NoteList
        notes={notes}
        onEdit={handleEditNote}
        onDelete={handleDeleteNote}
      />
    </div>
  );
};

export default NotesPage;
