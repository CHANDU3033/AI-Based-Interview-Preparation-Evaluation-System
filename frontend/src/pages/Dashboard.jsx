import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { useAuth } from '../contexts/AuthContext'
import { interviewService } from '../services/interviewService'

function StatCard({ icon, label, value, color = 'blue' }) {
  const colors = {
    blue: 'border-t-blue-500 text-blue-600',
    green: 'border-t-green-500 text-green-600',
    purple: 'border-t-purple-500 text-purple-600',
    orange: 'border-t-orange-500 text-orange-600',
  }
  return (
    <div className={`card border-t-4 ${colors[color]}`}>
      <div className="text-2xl mb-2">{icon}</div>
      <div className={`text-3xl font-bold ${colors[color]}`}>{value}</div>
      <div className="text-sm text-gray-500 mt-1">{label}</div>
    </div>
  )
}

export default function Dashboard() {
  const { user } = useAuth()
  const navigate = useNavigate()
  const [summary, setSummary] = useState(null)
  const [progress, setProgress] = useState([])
  const [weakTopics, setWeakTopics] = useState([])
  const [recommendations, setRecommendations] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      interviewService.getDashboardSummary(),
      interviewService.getDashboardProgress(),
      interviewService.getWeakTopics(),
      interviewService.getRecommendations(),
    ]).then(([s, p, w, r]) => {
      setSummary(s.data)
      setProgress(p.data)
      setWeakTopics(w.data.weak_topics || [])
      setRecommendations(r.data.recommendations || [])
    }).catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return (
    <div className="flex items-center justify-center h-64">
      <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600" />
    </div>
  )

  const hasInterviews = summary?.total_interviews > 0

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">
            Welcome back, {user?.name?.split(' ')[0]}! 👋
          </h1>
          <p className="text-gray-500 text-sm mt-1">
            {user?.target_role ? `Preparing for: ${user.target_role}` : 'Ready for your next interview?'}
          </p>
        </div>
        <button onClick={() => navigate('/interview/setup')} className="btn-primary">
          🎯 Start Interview
        </button>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <StatCard icon="📝" label="Total Interviews" value={summary?.total_interviews || 0} color="blue" />
        <StatCard icon="⭐" label="Average Score" value={hasInterviews ? `${summary.avg_score}%` : '—'} color="green" />
        <StatCard icon="🏆" label="Best Score" value={hasInterviews ? `${summary.best_score}%` : '—'} color="purple" />
        <StatCard icon="🔥" label="Keep Practicing!" value={hasInterviews ? '↑ Growing' : 'Start now'} color="orange" />
      </div>

      {/* Score Chart */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-4">📈 Score Progression</h2>
        {progress.length > 1 ? (
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={progress}>
              <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
              <XAxis dataKey="date" tick={{ fontSize: 12 }} />
              <YAxis domain={[0, 100]} tick={{ fontSize: 12 }} />
              <Tooltip formatter={(v) => [`${v}%`, 'Score']} />
              <Line
                type="monotone"
                dataKey="overall_score"
                stroke="#2563eb"
                strokeWidth={2.5}
                dot={{ fill: '#2563eb', r: 5 }}
                activeDot={{ r: 7 }}
              />
            </LineChart>
          </ResponsiveContainer>
        ) : (
          <div className="text-center py-12 text-gray-400">
            <div className="text-4xl mb-3">📊</div>
            <p>Complete at least 2 interviews to see your progress chart.</p>
            <button onClick={() => navigate('/interview/setup')} className="btn-primary mt-4">
              Start First Interview
            </button>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Weak Topics */}
        <div className="card">
          <h2 className="font-semibold text-gray-800 mb-4">🎯 Topics to Improve</h2>
          {weakTopics.length > 0 ? (
            <ul className="space-y-2">
              {weakTopics.map((t, i) => (
                <li key={i} className="flex items-center justify-between p-2 bg-orange-50 rounded-lg">
                  <span className="text-sm text-gray-700">{t.topic}</span>
                  <span className="badge-yellow">{t.count}x weak</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-sm text-gray-400">No weak topics identified yet. Keep interviewing!</p>
          )}
        </div>

        {/* Recommendations */}
        <div className="card">
          <h2 className="font-semibold text-gray-800 mb-4">💡 Study Recommendations</h2>
          {recommendations.length > 0 ? (
            <ul className="space-y-2">
              {recommendations.map((rec, i) => (
                <li key={i} className="flex items-start space-x-2 p-2 bg-blue-50 rounded-lg">
                  <span className="text-blue-500 mt-0.5">→</span>
                  <span className="text-sm text-gray-700">{rec}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-sm text-gray-400">Complete interviews to get personalized recommendations.</p>
          )}
        </div>
      </div>

      {/* Recent Interviews */}
      {summary?.recent_interviews?.length > 0 && (
        <div className="card">
          <div className="flex items-center justify-between mb-4">
            <h2 className="font-semibold text-gray-800">🕐 Recent Interviews</h2>
            <button onClick={() => navigate('/interview/history')} className="text-sm text-blue-600 hover:underline">
              View all →
            </button>
          </div>
          <div className="space-y-2">
            {summary.recent_interviews.map((iv) => (
              <div key={iv.id}
                className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 cursor-pointer transition"
                onClick={() => navigate(`/interview/${iv.id}/report`)}
              >
                <div>
                  <span className="font-medium text-sm text-gray-800">{iv.role_name}</span>
                  <span className="text-xs text-gray-400 ml-2">{iv.difficulty}</span>
                </div>
                <div className="flex items-center space-x-3">
                  {iv.overall_score != null && (
                    <span className={`font-bold text-sm ${iv.overall_score >= 75 ? 'text-green-600' : iv.overall_score >= 60 ? 'text-yellow-600' : 'text-red-600'}`}>
                      {iv.overall_score}%
                    </span>
                  )}
                  <span className="badge-blue text-xs">{iv.status}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
