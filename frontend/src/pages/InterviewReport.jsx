import React, { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { interviewService } from '../services/interviewService'
import ScoreBar from '../components/ScoreBar'
import FeedbackPanel from '../components/FeedbackPanel'
import EvaluationCard from '../components/EvaluationCard'

function OverallBadge({ score }) {
  const color = score >= 75 ? 'bg-green-100 text-green-800 border-green-300'
    : score >= 60 ? 'bg-yellow-100 text-yellow-800 border-yellow-300'
    : 'bg-red-100 text-red-800 border-red-300'
  const label = score >= 75 ? 'Excellent' : score >= 60 ? 'Good' : 'Needs Work'
  return (
    <div className={`inline-flex flex-col items-center px-8 py-4 rounded-2xl border-2 ${color}`}>
      <span className="text-5xl font-bold">{Math.round(score)}%</span>
      <span className="text-sm font-medium mt-1">{label}</span>
    </div>
  )
}

export default function InterviewReport() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [report, setReport] = useState(null)
  const [loading, setLoading] = useState(true)
  const [openAnswer, setOpenAnswer] = useState(null)

  useEffect(() => {
    interviewService.getReport(id)
      .then(res => setReport(res.data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [id])

  if (loading) return (
    <div className="flex items-center justify-center h-64">
      <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600" />
    </div>
  )

  if (!report) return <div className="text-center py-12 text-gray-400">Report not found.</div>

  const { interview, answers } = report
  const chartData = [
    { name: 'Technical', score: Math.round(interview.technical_score || 0) },
    { name: 'Relevance', score: Math.round(interview.relevance_score || 0) },
    { name: 'Completeness', score: Math.round(interview.completeness_score || 0) },
    { name: 'Communication', score: Math.round(interview.communication_score || 0) },
  ]

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Header */}
      <div className="text-center card">
        <h1 className="text-2xl font-bold text-gray-900 mb-1">🎉 Interview Report</h1>
        <p className="text-gray-500 text-sm mb-5">
          {interview.role_name} · {interview.difficulty} · {interview.total_questions} Questions
        </p>
        {interview.overall_score != null && <OverallBadge score={interview.overall_score} />}
      </div>

      {/* Score Bars */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-4">📊 Score Breakdown</h2>
        <ScoreBar label="Technical Accuracy" score={interview.technical_score || 0} />
        <ScoreBar label="Answer Relevance" score={interview.relevance_score || 0} />
        <ScoreBar label="Completeness" score={interview.completeness_score || 0} />
        <ScoreBar label="Communication" score={interview.communication_score || 0} />
      </div>

      {/* Bar Chart */}
      <div className="card">
        <h2 className="font-semibold text-gray-800 mb-4">📈 Performance Chart</h2>
        <ResponsiveContainer width="100%" height={200}>
          <BarChart data={chartData} barSize={40}>
            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
            <XAxis dataKey="name" tick={{ fontSize: 12 }} />
            <YAxis domain={[0, 100]} tick={{ fontSize: 12 }} />
            <Tooltip formatter={(v) => [`${v}%`]} />
            <Bar dataKey="score" fill="#2563eb" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Feedback Panel */}
      <FeedbackPanel
        strongAreas={interview.strong_areas || []}
        weakAreas={interview.weak_areas || []}
        recommendations={interview.recommendations || []}
      />

      {/* Per-question accordion */}
      {answers?.length > 0 && (
        <div className="card">
          <h2 className="font-semibold text-gray-800 mb-4">📋 Question-by-Question Breakdown</h2>
          <div className="space-y-3">
            {answers.map((ans, i) => (
              <div key={ans.answer_id} className="border border-gray-100 rounded-xl overflow-hidden">
                <button
                  onClick={() => setOpenAnswer(openAnswer === i ? null : i)}
                  className="w-full flex items-center justify-between p-4 text-left hover:bg-gray-50 transition"
                >
                  <div className="flex items-center space-x-3">
                    <span className="text-sm font-semibold text-blue-600">Q{i + 1}</span>
                    <span className="text-sm text-gray-700 line-clamp-1">{ans.question_text}</span>
                  </div>
                  <div className="flex items-center space-x-2 shrink-0 ml-3">
                    {ans.evaluation && (
                      <span className={`text-sm font-bold ${
                        ans.evaluation.overall_score >= 75 ? 'text-green-600'
                        : ans.evaluation.overall_score >= 60 ? 'text-yellow-600'
                        : 'text-red-600'
                      }`}>
                        {Math.round(ans.evaluation.overall_score)}%
                      </span>
                    )}
                    <span className="text-gray-400 text-xs">{openAnswer === i ? '▲' : '▼'}</span>
                  </div>
                </button>

                {openAnswer === i && (
                  <div className="px-4 pb-4 border-t border-gray-100 bg-gray-50">
                    <div className="mt-3 mb-2">
                      <p className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1">Your Answer</p>
                      <p className="text-sm text-gray-700 bg-white rounded-lg p-3 border border-gray-100">
                        {ans.answer_text}
                      </p>
                    </div>
                    {ans.evaluation && <EvaluationCard evaluation={ans.evaluation} />}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-3">
        <button onClick={() => navigate('/interview/setup')} className="btn-primary flex-1 py-3">
          🔄 Start New Interview
        </button>
        <button onClick={() => navigate('/dashboard')} className="btn-secondary flex-1 py-3">
          📊 View Dashboard
        </button>
        <button onClick={() => navigate('/interview/history')} className="btn-secondary flex-1 py-3">
          📋 Interview History
        </button>
      </div>
    </div>
  )
}
