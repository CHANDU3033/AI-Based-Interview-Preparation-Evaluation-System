import React, { useState, useEffect, useRef } from 'react'

export default function AnswerInput({ onSubmit, isSubmitting }) {
  const [answer, setAnswer] = useState('')
  const [seconds, setSeconds] = useState(0)
  const timerRef = useRef(null)

  useEffect(() => {
    timerRef.current = setInterval(() => setSeconds(s => s + 1), 1000)
    return () => clearInterval(timerRef.current)
  }, [])

  const formatTime = (s) => `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`

  const handleSubmit = () => {
    clearInterval(timerRef.current)
    onSubmit(answer.trim(), seconds)
  }

  const minLength = 20
  const canSubmit = answer.trim().length >= minLength && !isSubmitting

  return (
    <div className="card mt-4">
      <div className="flex items-center justify-between mb-3">
        <label className="text-sm font-medium text-gray-700">Your Answer</label>
        <div className="flex items-center space-x-3">
          <span className="text-xs text-gray-400">{answer.length} characters</span>
          <span className="text-sm font-mono text-blue-600 font-bold">⏱ {formatTime(seconds)}</span>
        </div>
      </div>

      <textarea
        className="input-field resize-none"
        rows={6}
        placeholder="Type your answer here... (minimum 20 characters)"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        disabled={isSubmitting}
      />

      {answer.length > 0 && answer.trim().length < minLength && (
        <p className="text-xs text-amber-600 mt-1">Please write at least {minLength} characters.</p>
      )}

      <div className="flex justify-end mt-4">
        <button
          onClick={handleSubmit}
          disabled={!canSubmit}
          className="btn-primary flex items-center space-x-2"
        >
          {isSubmitting ? (
            <>
              <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" />
              </svg>
              <span>Evaluating...</span>
            </>
          ) : (
            <>
              <span>Submit Answer</span>
              <span>→</span>
            </>
          )}
        </button>
      </div>
    </div>
  )
}
