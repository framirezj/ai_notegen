import { useEffect, useState } from "react";
import { getNotes } from "../services/api";

const NoteList = ({refresh}) => {
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        getNotes().then((res) => setNotes(res.data));
    },[refresh])

    return(
        <div className="p-4 space-y-4">
            {notes.map( (note) => (
                <div key={note.id} className="p-4 border rounded shadow">
                    <h2>{note.title}</h2>
                    <p>{note.content}</p>
                </div>
            ))}
        </div>
    )

}

export default NoteList;