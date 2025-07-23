import { Plus, X } from "lucide-react";


const AddTask = ({handleToggleForm, showForm}) => {


  return (
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
  );
};

export default AddTask;
