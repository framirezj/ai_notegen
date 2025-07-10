import { useState } from "react";
import "./App.css";
import NoteForm from "./components/NoteForm";
import NoteList from "./components/NoteList";

function App() {
  const [refresh, setRefresh] = useState(0);

  const reloadNotes = () => setRefresh((r) => r + 1)

  return (
    <div className="max-w-2xl mx-auto mt-10 space-y-6">
      <h1 className="text-3xl font-bold text-center text-gray-100">🧠 AI NoteGen</h1>
      <NoteForm onNoteCreated={reloadNotes}/>
      <NoteList refresh={refresh}/>
    </div>
  );
}

export default App;
