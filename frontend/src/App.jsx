import { useState } from 'react';
import SearchInput from './components/SearchInput';
import ResultsDisplay from './components/ResultsDisplay';
import { analyzeInvention } from './api/client';

function App() {
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (inventionIdea) => {
    setIsLoading(true);
    setError(null);
    setResults(null);

    try {
      const data = await analyzeInvention(inventionIdea);
      setResults(data);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          'Failed to analyze invention. Please ensure the backend is running and try again.'
      );
      console.error('Error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <span className="text-4xl">🛡️</span>
              <h1 className="text-3xl font-bold text-gray-900">PatentGuard</h1>
            </div>
            <p className="text-sm text-gray-600 hidden sm:block">
              AI-Powered Patent Prior Art Search
            </p>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        {!results && !isLoading && (
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-800 mb-4">
              Protect Your Innovation
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Enter your invention idea below and we'll search through thousands
              of patents to identify potential conflicts and assess your risk.
            </p>
          </div>
        )}

        {/* Search Input */}
        <SearchInput onSearch={handleSearch} isLoading={isLoading} />

        {/* Error Message */}
        {error && (
          <div className="w-full max-w-4xl mx-auto mb-8">
            <div className="bg-red-50 border-l-4 border-red-500 rounded-lg p-6">
              <div className="flex items-center gap-3">
                <span className="text-2xl">❌</span>
                <div>
                  <h3 className="text-lg font-semibold text-red-800">
                    Error
                  </h3>
                  <p className="text-red-700">{error}</p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Results */}
        <ResultsDisplay results={results} />
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm">
            PatentGuard MVP • Powered by Groq AI, Pinecone & BigQuery • For
            demonstration purposes only
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
