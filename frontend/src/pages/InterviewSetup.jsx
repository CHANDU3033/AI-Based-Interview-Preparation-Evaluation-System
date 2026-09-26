import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { interviewService } from '../services/interviewService'

const DIFFICULTIES = [
  { value: 'Beginner', label: 'Beginner', icon: '🌱', desc: 'Fundamental concepts, simple questions' },
  { value: 'Intermediate', label: 'Intermediate', icon: '⚡', desc: 'Practical knowledge, real-world scenarios' },
  { value: 'Advanced', label: 'Advanced', icon: '🔥', desc: 'Deep concepts, complex problem-solving' },
]

const RESPONSE_MODES = [
  { value: 'TEXT', label: '⌨️ Text Answer', desc: 'Type & submit text responses' },
  { value: 'VOICE', label: '🎙️ Voice Dictation', desc: 'Microphone speech-to-text AI' },
  { value: 'HYBRID', label: '⚡ Hybrid Mode', desc: 'Voice dictation + text editor' },
]

const QUESTION_COUNTS = [3, 5, 10]

const ROLE_ICONS = {
  'Python Developer': '🐍',
  'Data Analyst': '📊',
  'AI/ML Engineer': '🤖',
  'SQL Developer': '🗄️',
  'Software Developer': '💻',
}

export default function InterviewSetup() {
  const navigate = useNavigate()
  const [roles, setRoles] = useState([])
  const [selected, setSelected] = useState({ role: null, difficulty: 'Intermediate', count: 5, mode: 'VOICE' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    interviewService.getRoles().then(res => setRoles(res.data)).catch(console.error)
  }, [])

  const handleStart = async () => {
    if (!selected.role) { setError('Please select a job role.'); return }
    setLoading(true)
    setError('')
    try {
      const res = await interviewService.startInterview({
        role_id: selected.role.id,
        difficulty: selected.difficulty,
        mode: selected.mode,
        total_questions: selected.count,
      })
      navigate(`/interview/${res.data.interview_id}`)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to start interview. Please try again.')
      setLoading(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">🚀 Setup Your Interview</h1>
        <p className="text-gray-500 text-sm mt-1">Customize your mock interview session</p>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 text-sm px-4 py-3 rounded-lg">{error}</div>
      )}

      {/* Step 1: Role */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-1">Step 1 — Select Job Role</h2>
        <p className="text-xs text-gray-400 mb-4">Choose the role you want to practice for</p>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
          {roles.map(role => (
            <button
              key={role.id}
              onClick={() => setSelected({ ...selected, role })}
              className={`p-4 rounded-xl border-2 text-left transition-all ${
                selected.role?.id === role.id
                  ? 'border-blue-500 bg-blue-50 shadow-sm'
                  : 'border-gray-200 hover:border-blue-300 hover:bg-gray-50'
              }`}
            >
              <div className="text-2xl mb-2">{ROLE_ICONS[role.role_name] || '💻'}</div>
              <div className="font-medium text-sm text-gray-800">{role.role_name}</div>
              {role.description && (
                <div className="text-xs text-gray-400 mt-1 line-clamp-2">{role.description}</div>
              )}
            </button>
          ))}
        </div>
      </div>

      {/* Step 2: Difficulty */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-1">Step 2 — Select Difficulty</h2>
        <p className="text-xs text-gray-400 mb-4">Choose question difficulty level</p>
        <div className="grid grid-cols-3 gap-3">
          {DIFFICULTIES.map(d => (
            <button
              key={d.value}
              onClick={() => setSelected({ ...selected, difficulty: d.value })}
              className={`p-4 rounded-xl border-2 text-center transition-all ${
                selected.difficulty === d.value
                  ? 'border-blue-500 bg-blue-50'
                  : 'border-gray-200 hover:border-blue-300'
              }`}
            >
              <div className="text-2xl mb-1">{d.icon}</div>
              <div className="font-semibold text-sm text-gray-800">{d.label}</div>
              <div className="text-xs text-gray-400 mt-1">{d.desc}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Step 3: Response Mode */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-1">Step 3 — Response Mode</h2>
        <p className="text-xs text-gray-400 mb-4">Choose how you want to answer questions</p>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {RESPONSE_MODES.map(m => (
            <button
              key={m.value}
              onClick={() => setSelected({ ...selected, mode: m.value })}
              className={`p-4 rounded-xl border-2 text-center transition-all ${
                selected.mode === m.value
                  ? 'border-blue-500 bg-blue-50'
                  : 'border-gray-200 hover:border-blue-300'
              }`}
            >
              <div className="font-semibold text-sm text-gray-800">{m.label}</div>
              <div className="text-xs text-gray-400 mt-1">{m.desc}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Step 4: Question Count */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-1">Step 4 — Number of Questions</h2>
        <p className="text-xs text-gray-400 mb-4">How many questions do you want?</p>
        <div className="flex space-x-3">
          {QUESTION_COUNTS.map(n => (
            <button
              key={n}
              onClick={() => setSelected({ ...selected, count: n })}
              className={`flex-1 py-3 rounded-xl border-2 font-semibold transition-all ${
                selected.count === n
                  ? 'border-blue-500 bg-blue-50 text-blue-700'
                  : 'border-gray-200 hover:border-blue-300 text-gray-600'
              }`}
            >
              {n} Questions
              <div className="text-xs font-normal text-gray-400 mt-0.5">
                ~{n * 2} mins
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Summary + Start */}
      {selected.role && (
        <div className="card bg-blue-50 border-blue-200">
          <h2 className="font-semibold text-blue-900 mb-3">🎯 Interview Summary</h2>
          <div className="grid grid-cols-4 gap-4 text-center">
            <div>
              <div className="text-xl">{ROLE_ICONS[selected.role.role_name] || '💻'}</div>
              <div className="text-xs text-blue-700 font-medium mt-1">{selected.role.role_name}</div>
            </div>
            <div>
              <div className="text-xl">⚡</div>
              <div className="text-xs text-blue-700 font-medium mt-1">{selected.difficulty}</div>
            </div>
            <div>
              <div className="text-xl">🎙️</div>
              <div className="text-xs text-blue-700 font-medium mt-1">{selected.mode} Mode</div>
            </div>
            <div>
              <div className="text-xl">📋</div>
              <div className="text-xs text-blue-700 font-medium mt-1">{selected.count} Questions</div>
            </div>
          </div>
        </div>
      )}

      <button
        onClick={handleStart}
        disabled={!selected.role || loading}
        className="btn-primary w-full py-3 text-base font-semibold"
      >
        {loading ? '⏳ Starting interview...' : '🚀 Start Interview'}
      </button>
    </div>
  )
}
