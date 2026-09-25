import React from 'react'

export default function FeedbackPanel({ strongAreas = [], weakAreas = [], recommendations = [] }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
      {/* Strong Areas */}
      <div className="card border-t-4 border-t-green-500">
        <h3 className="font-semibold text-gray-800 mb-3 flex items-center space-x-2">
          <span>💪</span><span>Strong Areas</span>
        </h3>
        {strongAreas.length > 0 ? (
          <ul className="space-y-2">
            {strongAreas.map((area, i) => (
              <li key={i} className="flex items-start space-x-2 text-sm text-gray-700">
                <span className="text-green-500 font-bold mt-0.5">✓</span>
                <span>{area}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-gray-400">Complete more interviews to see your strong areas.</p>
        )}
      </div>

      {/* Weak Areas */}
      <div className="card border-t-4 border-t-orange-400">
        <h3 className="font-semibold text-gray-800 mb-3 flex items-center space-x-2">
          <span>🎯</span><span>Areas to Improve</span>
        </h3>
        {weakAreas.length > 0 ? (
          <ul className="space-y-2">
            {weakAreas.map((area, i) => (
              <li key={i} className="flex items-start space-x-2 text-sm text-gray-700">
                <span className="text-orange-500 font-bold mt-0.5">•</span>
                <span>{area}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-gray-400 italic">Great job — no major weak areas!</p>
        )}
      </div>

      {/* Recommendations */}
      <div className="card border-t-4 border-t-blue-500">
        <h3 className="font-semibold text-gray-800 mb-3 flex items-center space-x-2">
          <span>💡</span><span>Recommendations</span>
        </h3>
        {recommendations.length > 0 ? (
          <ul className="space-y-2">
            {recommendations.map((rec, i) => (
              <li key={i} className="flex items-start space-x-2 text-sm text-gray-700">
                <span className="text-blue-500 mt-0.5">→</span>
                <span>{rec}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-gray-400">No recommendations available yet.</p>
        )}
      </div>
    </div>
  )
}
