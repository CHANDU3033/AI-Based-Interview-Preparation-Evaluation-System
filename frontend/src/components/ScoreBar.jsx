import React from 'react'

function getColor(score) {
  if (score >= 75) return 'bg-green-500'
  if (score >= 60) return 'bg-yellow-400'
  return 'bg-red-500'
}

function getTextColor(score) {
  if (score >= 75) return 'text-green-700'
  if (score >= 60) return 'text-yellow-700'
  return 'text-red-700'
}

export default function ScoreBar({ label, score = 0 }) {
  const pct = Math.min(Math.round(score), 100)
  return (
    <div className="flex items-center space-x-3 mb-3">
      <span className="text-sm text-gray-600 w-44 shrink-0">{label}</span>
      <div className="flex-1 bg-gray-100 rounded-full h-3 overflow-hidden">
        <div
          className={`h-3 rounded-full transition-all duration-700 ${getColor(pct)}`}
          style={{ width: `${pct}%` }}
        />
      </div>
      <span className={`text-sm font-bold w-12 text-right ${getTextColor(pct)}`}>{pct}%</span>
    </div>
  )
}
