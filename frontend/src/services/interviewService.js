import axios from 'axios'

const API = axios.create({ baseURL: '/api' })

API.interceptors.request.use((config) => {
  const token = localStorage.getItem('ai_interview_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export const interviewService = {
  getRoles: () => API.get('/questions/roles'),
  generateQuestions: (data) => API.post('/questions/generate', data),

  startInterview: (data) => API.post('/interviews/start', data),
  getInterview: (id) => API.get(`/interviews/${id}`),
  getHistory: () => API.get('/interviews/history'),
  submitAnswer: (interviewId, data) => API.post(`/interviews/${interviewId}/answer`, data),
  completeInterview: (interviewId) => API.post(`/interviews/${interviewId}/complete`),
  cancelInterview: (interviewId) => API.delete(`/interviews/${interviewId}`),

  getReport: (interviewId) => API.get(`/evaluations/${interviewId}`),
  evaluateSingle: (data) => API.post('/evaluations/evaluate/text', data),

  getDashboardSummary: () => API.get('/dashboard/summary'),
  getDashboardProgress: () => API.get('/dashboard/progress'),
  getWeakTopics: () => API.get('/dashboard/weak-topics'),
  getRecommendations: () => API.get('/dashboard/recommendations'),
}
