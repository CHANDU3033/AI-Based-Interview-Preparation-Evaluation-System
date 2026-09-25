import axios from 'axios'

const API = axios.create({ baseURL: '/api' })

// Attach JWT token to every request
API.interceptors.request.use((config) => {
  const token = localStorage.getItem('ai_interview_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export const authService = {
  register: (data) => API.post('/auth/register', data),
  login: (data) => API.post('/auth/login', data),
  getMe: () => API.get('/auth/me'),
  updateProfile: (data) => API.put('/auth/me', data),
}
