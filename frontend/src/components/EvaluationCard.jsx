import React from 'react'
import ScoreBar from './ScoreBar'

function ScoreBadge({ score }) {
  const color = score >= 75 ? 'bg-green-100 text-green-800 border-green-200'
    : score >= 60 ? 'bg-yellow-100 text-yellow-800 border-yellow-200'
    : 'bg-red-100 text-red-800 border-red-200'
  return (
    <div className={`inline-flex items-center px-3 py-1.5 rounded-full border text-sm font-bold ${color}`}>
      {Math.round(score)}%
    </div>
  )
}

export default function EvaluationCard({ evaluation }) {
  if (!evaluation) return null
  const { relevance_score, accuracy_score, completeness_score,
          communication_score, overall_score, feedback, strengths = [], improvements = [] } = evaluation

  return (
    <div className="card mt-4 border-l-4 border-l-blue-500 animate-fade-in">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-semibold text-gray-800">📊 Evaluation Result</h3>
        <ScoreBadge score={overall_score} />
      </div>

      <div className="space-y-1 mb-4">
        <ScoreBar label="Technical Accuracy" score={accuracy_score} />
        <ScoreBar label="Relevance" score={relevance_score} />
        <ScoreBar label="Completeness" score={completeness_score} />
        <ScoreBar label="Communication" score={communication_score} />
      </div>

      {feedback && (
        <div className="bg-blue-50 rounded-lg p-3 mb-4">
          <p className="text-sm text-blue-800">{feedback}</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {strengths.length > 0 && (
          <div>
            <h4 className="text-xs font-semibold text-green-700 uppercase tracking-wide mb-2">✓ Strengths</h4>
            <ul className="space-y-1">
              {strengths.map((s, i) => (
                <li key={i} className="text-xs text-gray-700 flex items-start space-x-1">
                  <span className="text-green-500 mt-0.5">•</span><span>{s}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
        {improvements.length > 0 && (
          <div>
            <h4 className="text-xs font-semibold text-orange-700 uppercase tracking-wide mb-2">↑ Improve</h4>
            <ul className="space-y-1">
              {improvements.map((imp, i) => (
                <li key={i} className="text-xs text-gray-700 flex items-start space-x-1">
                  <span className="text-orange-500 mt-0.5">•</span><span>{imp}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  )
}
