const ResultsDisplay = ({ results }) => {
  if (!results) return null;

  const getRiskColor = (riskLevel) => {
    switch (riskLevel.toLowerCase()) {
      case 'high':
        return 'bg-red-100 border-red-500 text-red-800';
      case 'medium':
        return 'bg-yellow-100 border-yellow-500 text-yellow-800';
      case 'low':
        return 'bg-green-100 border-green-500 text-green-800';
      default:
        return 'bg-gray-100 border-gray-500 text-gray-800';
    }
  };

  const getRiskIcon = (riskLevel) => {
    switch (riskLevel.toLowerCase()) {
      case 'high':
        return '⚠️';
      case 'medium':
        return '⚡';
      case 'low':
        return '✅';
      default:
        return '📊';
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* Risk Level Card */}
      <div
        className={`border-l-4 rounded-lg p-6 ${getRiskColor(
          results.risk_level
        )}`}
      >
        <div className="flex items-center gap-3 mb-2">
          <span className="text-3xl">{getRiskIcon(results.risk_level)}</span>
          <h2 className="text-2xl font-bold">
            Risk Level: {results.risk_level}
          </h2>
        </div>
      </div>

      {/* Analysis Card */}
      <div className="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
        <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
          <span>📋</span> Conflict Analysis
        </h3>
        <p className="text-gray-700 leading-relaxed whitespace-pre-line">
          {results.analysis}
        </p>
      </div>

      {/* Recommendations Card */}
      {results.recommendations && (
        <div className="bg-blue-50 rounded-lg shadow-lg p-6 border border-blue-200">
          <h3 className="text-xl font-bold text-blue-900 mb-4 flex items-center gap-2">
            <span>💡</span> Recommendations
          </h3>
          <p className="text-blue-800 leading-relaxed">
            {results.recommendations}
          </p>
        </div>
      )}

      {/* Conflicting Patents */}
      {results.conflicting_patents &&
        results.conflicting_patents.length > 0 && (
          <div className="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
            <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <span>📄</span> Potentially Conflicting Patents
            </h3>
            <ul className="space-y-2">
              {results.conflicting_patents.map((patent, idx) => (
                <li
                  key={idx}
                  className="flex items-center gap-2 text-gray-700 bg-gray-50 p-3 rounded"
                >
                  <span className="text-blue-600 font-mono font-semibold">
                    {patent}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        )}

      {/* Retrieved Patents */}
      {results.retrieved_patents && results.retrieved_patents.length > 0 && (
        <div className="bg-white rounded-lg shadow-lg p-6 border border-gray-200">
          <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
            <span>🔍</span> Similar Patents Found
          </h3>
          <div className="space-y-4">
            {results.retrieved_patents.map((patent, idx) => (
              <div
                key={idx}
                className="border-l-4 border-blue-500 bg-gray-50 p-4 rounded"
              >
                <div className="flex justify-between items-start mb-2">
                  <h4 className="font-semibold text-gray-800">
                    {patent.metadata?.title || 'Untitled Patent'}
                  </h4>
                  <span className="text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded">
                    {(patent.score * 100).toFixed(1)}% match
                  </span>
                </div>
                <p className="text-sm text-gray-600 font-mono mb-2">
                  {patent.metadata?.publication_number}
                </p>
                <p className="text-sm text-gray-700">
                  {patent.metadata?.abstract?.substring(0, 200)}...
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultsDisplay;
