import React from 'react'

const difficultyColor = {
  Beginner: 'bg-green-100 text-green-700',
  Intermediate: 'bg-yellow-100 text-yellow-700',
  Advanced: 'bg-red-100 text-red-700',
}

const categoryColor = {
  Technical: 'bg-blue-100 text-blue-700',
  HR: 'bg-purple-100 text-purple-700',
  Project: 'bg-orange-100 text-orange-700',
  Scenario: 'bg-pink-100 text-pink-700',
}

export default function QuestionCard({ question, questionNumber, totalQuestions, category, difficulty }) {
  return (
    <div className="card animate-slide-up">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-2">
          <span className={`text-xs font-medium px-2.5 py-1 rounded-full ${categoryColor[category] || 'bg-gray-100 text-gray-700'}`}>
            {category}
          </span>
          <span className={`text-xs font-medium px-2.5 py-1 rounded-full ${difficultyColor[difficulty] || 'bg-gray-100 text-gray-700'}`}>
            {difficulty}
          </span>
        </div>
        <span className="text-sm text-gray-400 font-medium">
          Q {questionNumber + 1} / {totalQuestions}
        </span>
      </div>
      <p className="text-gray-900 text-lg leading-relaxed font-medium">{question}</p>
    </div>
  )
}
