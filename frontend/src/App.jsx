import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from './contexts/AuthContext'
import { ProtectedRoute } from './components/ProtectedRoute'
import Layout from './components/Layout'

// Public pages
import Login from './pages/Login'
import Register from './pages/Register'

// Protected pages
import Dashboard from './pages/Dashboard'
import InterviewSetup from './pages/InterviewSetup'
import MockInterview from './pages/MockInterview'
import InterviewReport from './pages/InterviewReport'
import InterviewHistory from './pages/InterviewHistory'
import Profile from './pages/Profile'

function RootRedirect() {
  const { user, loading } = useAuth()
  if (loading) return null
  return user ? <Navigate to="/dashboard" replace /> : <Navigate to="/login" replace />
}

function App() {
  return (
    <AuthProvider>
      <Routes>
        {/* Root redirect */}
        <Route path="/" element={<RootRedirect />} />

        {/* Public */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected */}
        <Route path="/dashboard" element={
          <ProtectedRoute><Layout><Dashboard /></Layout></ProtectedRoute>
        } />
        <Route path="/interview/setup" element={
          <ProtectedRoute><Layout><InterviewSetup /></Layout></ProtectedRoute>
        } />
        <Route path="/interview/:id" element={
          <ProtectedRoute><Layout><MockInterview /></Layout></ProtectedRoute>
        } />
        <Route path="/interview/:id/report" element={
          <ProtectedRoute><Layout><InterviewReport /></Layout></ProtectedRoute>
        } />
        <Route path="/interview/history" element={
          <ProtectedRoute><Layout><InterviewHistory /></Layout></ProtectedRoute>
        } />
        <Route path="/profile" element={
          <ProtectedRoute><Layout><Profile /></Layout></ProtectedRoute>
        } />

        {/* 404 fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}

export default App
