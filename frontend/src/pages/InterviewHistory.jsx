import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { interviewService } from '../services/interviewService'

function ScoreBadge({ score, status }) {
  if (status !== 'COMPLETED' || score == null) return <span className="badge-yellow">{status}</span>
  const color = score >= 75 ? 'badge-green' : score >= 60 ? 'badge-yellow' : 'badge-red'
  return <span className={color}>{Math.round(score)}%</span>
}

export default function InterviewHistory() {
  const navigate = useNavigate()
  const [interviews, setInterviews] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    interviewService.getHistory()
      .then(res => setInterviews(res.data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  const formatDate = (dt) => dt ? new Date(dt).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) : '—'

  if (loading) return (
    <div className="flex items-center justify-center h-64">
      <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600" />
    </div>
  )

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">📋 Interview History</h1>
          <p className="text-gray-500 text-sm mt-1">{interviews.length} interview{interviews.length !== 1 ? 's' : ''} total</p>
        </div>
        <button onClick={() => navigate('/interview/setup')} className="btn-primary">
          + New Interview
        </button>
      </div>

      {interviews.length === 0 ? (
        <div className="card text-center py-16">
          <div className="text-5xl mb-4">📝</div>
          <h2 className="text-lg font-semibold text-gray-700 mb-2">No interviews yet</h2>
          <p className="text-gray-400 mb-6">Start your first mock interview to see your history here.</p>
          <button onClick={() => navigate('/interview/setup')} className="btn-primary px-8">
            🎯 Start First Interview
          </button>
        </div>
      ) : (
        <div className="card p-0 overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-50 border-b border-gray-100">
              <tr>
                <th className="text-left px-6 py-3 text-xs font-semibold text-gray-500 uppercase">#</th>
                <th className="text-left px-6 py-3 text-xs font-semibold text-gray-500 uppercase">Role</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-gray-500 uppercase">Difficulty</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-gray-500 uppercase">Questions</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-gray-500 uppercase">Score</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-gray-500 uppercase">Date</th>
                <th className="px-4 py-3"></th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-50">
              {interviews.map((iv, i) => (
                <tr key={iv.id} className="hover:bg-gray-50 transition-colors cursor-pointer"
                  onClick={() => iv.status === 'COMPLETED' && navigate(`/interview/${iv.id}/report`)}>
                  <td className="px-6 py-4 text-sm text-gray-400">{i + 1}</td>
                  <td className="px-6 py-4">
                    <div className="font-medium text-sm text-gray-800">{iv.role_name}</div>
                  </td>
                  <td className="px-4 py-4">
                    <span className="text-xs text-gray-500">{iv.difficulty}</span>
                  </td>
                  <td className="px-4 py-4 text-sm text-gray-600">
                    {iv.questions_answered}/{iv.total_questions}
                  </td>
                  <td className="px-4 py-4">
                    <ScoreBadge score={iv.overall_score} status={iv.status} />
                  </td>
                  <td className="px-4 py-4 text-sm text-gray-400">{formatDate(iv.completed_at || iv.started_at)}</td>
                  <td className="px-4 py-4">
                    {iv.status === 'COMPLETED' && (
                      <button
                        onClick={(e) => { e.stopPropagation(); navigate(`/interview/${iv.id}/report`) }}
                        className="text-xs text-blue-600 hover:underline"
                      >
                        View Report →
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
