import React, { useEffect, useState, useCallback } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { interviewService } from '../services/interviewService'
import QuestionCard from '../components/QuestionCard'
import AnswerInput from '../components/AnswerInput'
import EvaluationCard from '../components/EvaluationCard'

export default function MockInterview() {
  const { id } = useParams()
  const navigate = useNavigate()

  const [interview, setInterview] = useState(null)
  const [currentQuestion, setCurrentQuestion] = useState(null)
  const [evaluation, setEvaluation] = useState(null)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [isComplete, setIsComplete] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  const loadInterview = useCallback(async () => {
    try {
      const res = await interviewService.getInterview(id)
      setInterview(res.data)
      setCurrentQuestion(res.data.current_question)
      if (res.data.status === 'COMPLETED') setIsComplete(true)
    } catch {
      setError('Failed to load interview.')
    } finally {
      setLoading(false)
    }
  }, [id])

  useEffect(() => { loadInterview() }, [loadInterview])

  const handleSubmitAnswer = async (answerText, durationSeconds) => {
    if (!currentQuestion) return
    setIsSubmitting(true)
    setEvaluation(null)
    try {
      const res = await interviewService.submitAnswer(id, {
        question_id: currentQuestion.id || 0,
        answer_text: answerText,
        duration_seconds: durationSeconds,
      })
      const data = res.data
      setEvaluation(data.evaluation)
      setInterview(prev => ({ ...prev, questions_answered: data.questions_answered }))

      if (data.interview_complete) {
        // Complete the interview
        await interviewService.completeInterview(id)
        setIsComplete(true)
      } else {
        setCurrentQuestion(data.next_question)
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to submit answer.')
    } finally {
      setIsSubmitting(false)
    }
  }

  const handleNextQuestion = () => {
    setEvaluation(null)
  }

  if (loading) return (
    <div className="flex items-center justify-center h-64">
      <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600" />
    </div>
  )

  if (error) return (
    <div className="text-center py-12">
      <p className="text-red-600">{error}</p>
      <button onClick={() => navigate('/interview/setup')} className="btn-primary mt-4">
        Start New Interview
      </button>
    </div>
  )

  // Completion screen
  if (isComplete) return (
    <div className="max-w-xl mx-auto text-center py-12">
      <div className="text-7xl mb-4">🎉</div>
      <h1 className="text-3xl font-bold text-gray-900 mb-2">Interview Complete!</h1>
      <p className="text-gray-500 mb-8">
        You've answered all {interview?.total_questions} questions. View your detailed performance report below.
      </p>
      <div className="flex flex-col sm:flex-row gap-3 justify-center">
        <button onClick={() => navigate(`/interview/${id}/report`)} className="btn-primary px-8 py-3 text-base">
          📊 View Full Report
        </button>
        <button onClick={() => navigate('/interview/setup')} className="btn-secondary px-8 py-3 text-base">
          🔄 Start New Interview
        </button>
      </div>
    </div>
  )

  const progress = interview ? (interview.questions_answered / interview.total_questions) * 100 : 0

  return (
    <div className="max-w-3xl mx-auto space-y-4">
      {/* Header bar */}
      <div className="card p-4">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-3">
            <span className="text-lg font-bold text-gray-800">🎯 AI Mock Interview</span>
            <span className="badge-blue">{interview?.role_name}</span>
            <span className="badge-yellow">{interview?.difficulty}</span>
          </div>
          <span className="text-sm font-medium text-gray-600">
            {interview?.questions_answered} / {interview?.total_questions} answered
          </span>
        </div>
        {/* Progress bar */}
        <div className="w-full bg-gray-100 rounded-full h-2.5">
          <div
            className="bg-blue-600 h-2.5 rounded-full transition-all duration-500"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>

      {/* Question */}
      {currentQuestion && (
        <QuestionCard
          question={currentQuestion.question_text}
          questionNumber={currentQuestion.index}
          totalQuestions={interview?.total_questions}
          category={currentQuestion.category}
          difficulty={currentQuestion.difficulty}
        />
      )}

      {/* Evaluation result (shown after submission) */}
      {evaluation && (
        <>
          <EvaluationCard evaluation={evaluation} />
          {!isComplete && (
            <div className="flex justify-end">
              <button onClick={handleNextQuestion} className="btn-primary">
                Next Question →
              </button>
            </div>
          )}
        </>
      )}

      {/* Answer input (shown when no evaluation yet) */}
      {!evaluation && currentQuestion && (
        <AnswerInput onSubmit={handleSubmitAnswer} isSubmitting={isSubmitting} />
      )}
    </div>
  )
}
