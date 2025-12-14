import { useState } from 'react';

const SearchInput = ({ onSearch, isLoading }) => {
  const [inventionIdea, setInventionIdea] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inventionIdea.trim().length >= 10) {
      onSearch(inventionIdea);
    } else {
      alert('Please enter at least 10 characters describing your invention.');
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto mb-8">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label
            htmlFor="invention"
            className="block text-lg font-semibold text-gray-700 mb-2"
          >
            Describe Your Invention Idea
          </label>
          <textarea
            id="invention"
            value={inventionIdea}
            onChange={(e) => setInventionIdea(e.target.value)}
            placeholder="Example: A smart water bottle that tracks hydration levels and reminds users to drink water through LED indicators and mobile app notifications..."
            className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none resize-none h-40 text-gray-700"
            disabled={isLoading}
          />
          <p className="text-sm text-gray-500 mt-2">
            Minimum 10 characters. Be as detailed as possible for better results.
          </p>
        </div>
        <button
          type="submit"
          disabled={isLoading || inventionIdea.trim().length < 10}
          className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200 flex items-center justify-center"
        >
          {isLoading ? (
            <>
              <svg
                className="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Analyzing with AI...
            </>
          ) : (
            'Analyze for Prior Art'
          )}
        </button>
      </form>
    </div>
  );
};

export default SearchInput;
