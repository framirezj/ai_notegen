import { Edit3, Trash2 } from "lucide-react";

const NoteList = ({ notes, onEdit, onDelete }) => {

  return (
    <div className="flex flex-col gap-4">
      {notes.map((note) => (
        <div
          key={note.id}
          className="flex w-full bg-gray-800 shadow rounded-xl p-8 items-start"
        >
          <div className="flex-1">
            <h2 className="font-bold text-gray-100">{note.title}</h2>
            <p className="text-gray-400">{note.content}</p>
          </div>
          <div className="flex gap-2">
            <button
              className="p-2 rounded-lg transition-all duration-200 text-gray-400 hover:text-blue-700 hover:bg-blue-300"
              onClick={() => onEdit(note)} 
            >
              <Edit3 className="h-5 w-5" />
            </button>
            <button
              className="p-2 rounded-lg transition-all duration-200 text-gray-400 hover:text-red-700 hover:bg-red-300"
              onClick={() => onDelete(note.id)} 
            >
              <Trash2 className="h-5 w-5" />
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default NoteList;