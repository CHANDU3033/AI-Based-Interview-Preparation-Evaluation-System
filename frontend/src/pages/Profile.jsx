import React, { useEffect, useState } from 'react'
import { useAuth } from '../contexts/AuthContext'
import { authService } from '../services/authService'

const ROLES = ['Python Developer', 'Data Analyst', 'AI/ML Engineer', 'SQL Developer', 'Software Developer']

export default function Profile() {
  const { user, updateUser } = useAuth()
  const [editing, setEditing] = useState(false)
  const [form, setForm] = useState({
    name: '', target_role: '', education: '', college: '', branch: '', experience_years: 0
  })
  const [loading, setLoading] = useState(false)
  const [msg, setMsg] = useState({ text: '', type: '' })

  useEffect(() => {
    if (user) setForm({
      name: user.name || '',
      target_role: user.target_role || '',
      education: user.education || '',
      college: user.college || '',
      branch: user.branch || '',
      experience_years: user.experience_years || 0,
    })
  }, [user])

  const handleSave = async () => {
    setLoading(true)
    setMsg({ text: '', type: '' })
    try {
      const res = await authService.updateProfile(form)
      updateUser(res.data)
      setEditing(false)
      setMsg({ text: '✓ Profile updated successfully!', type: 'green' })
    } catch {
      setMsg({ text: 'Failed to update profile.', type: 'red' })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900">👤 My Profile</h1>
        {!editing && (
          <button onClick={() => setEditing(true)} className="btn-secondary">
            ✏️ Edit Profile
          </button>
        )}
      </div>

      {msg.text && (
        <div className={`px-4 py-3 rounded-lg text-sm border ${
          msg.type === 'green' ? 'bg-green-50 border-green-200 text-green-700' : 'bg-red-50 border-red-200 text-red-700'
        }`}>
          {msg.text}
        </div>
      )}

      <div className="card">
        {/* Avatar */}
        <div className="flex items-center space-x-4 mb-6 pb-6 border-b border-gray-100">
          <div className="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white text-2xl font-bold">
            {user?.name?.[0]?.toUpperCase() || 'U'}
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900">{user?.name}</h2>
            <p className="text-gray-500 text-sm">{user?.email}</p>
            {user?.target_role && (
              <span className="badge-blue text-xs mt-1">{user.target_role}</span>
            )}
          </div>
        </div>

        {/* Fields */}
        <div className="space-y-4">
          {[
            ['Name', 'name', 'text'],
            ['Education', 'education', 'text'],
            ['College / University', 'college', 'text'],
            ['Branch / Specialization', 'branch', 'text'],
          ].map(([label, key, type]) => (
            <div key={key}>
              <label className="block text-sm font-medium text-gray-600 mb-1">{label}</label>
              {editing ? (
                <input
                  type={type}
                  className="input-field"
                  value={form[key]}
                  onChange={(e) => setForm({ ...form, [key]: e.target.value })}
                />
              ) : (
                <p className="text-gray-800 py-2 border-b border-gray-100">
                  {user?.[key] || <span className="text-gray-400 italic">Not set</span>}
                </p>
              )}
            </div>
          ))}

          {/* Target Role */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Target Job Role</label>
            {editing ? (
              <select className="input-field" value={form.target_role} onChange={(e) => setForm({ ...form, target_role: e.target.value })}>
                <option value="">Select role</option>
                {ROLES.map(r => <option key={r} value={r}>{r}</option>)}
              </select>
            ) : (
              <p className="text-gray-800 py-2 border-b border-gray-100">
                {user?.target_role || <span className="text-gray-400 italic">Not set</span>}
              </p>
            )}
          </div>

          {/* Experience */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Experience (years)</label>
            {editing ? (
              <input
                type="number"
                min="0"
                step="0.5"
                className="input-field"
                value={form.experience_years}
                onChange={(e) => setForm({ ...form, experience_years: parseFloat(e.target.value) || 0 })}
              />
            ) : (
              <p className="text-gray-800 py-2 border-b border-gray-100">
                {user?.experience_years || 0} years
              </p>
            )}
          </div>
        </div>

        {editing && (
          <div className="flex space-x-3 mt-6">
            <button onClick={handleSave} disabled={loading} className="btn-primary">
              {loading ? 'Saving...' : '💾 Save Changes'}
            </button>
            <button onClick={() => { setEditing(false); setMsg({ text: '', type: '' }) }} className="btn-secondary">
              Cancel
            </button>
          </div>
        )}
      </div>
    </div>
  )
}
