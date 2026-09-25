import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)

def get_ui_html():
    _root_dir = os.path.dirname(os.path.dirname(_backend_dir))
    _idx_path = os.path.join(_root_dir, "index.html")
    if os.path.exists(_idx_path):
        try:
            with open(_idx_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass
    return INDEX_HTML_CONTENT

INDEX_HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🎯 AI Interview Preparation & Evaluation System</title>
  
  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Outfit', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          colors: {
            brand: {
              50: '#f0f5ff',
              100: '#e0ebff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
              800: '#3730a3',
              900: '#312e81',
            },
            accent: {
              cyan: '#06b6d4',
              emerald: '#10b981',
              amber: '#f59e0b',
              rose: '#f43f5e',
              purple: '#a855f7'
            }
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Outfit', sans-serif;
      background-color: #0b0f19;
      color: #f1f5f9;
      background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(168, 85, 247, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(6, 182, 212, 0.08) 0px, transparent 50%);
      background-attachment: fixed;
    }

    .glass-card {
      background: rgba(17, 24, 39, 0.7);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    .glass-nav {
      background: rgba(11, 15, 25, 0.85);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .btn-gradient {
      background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .btn-gradient:hover {
      box-shadow: 0 0 25px rgba(99, 102, 241, 0.5);
      transform: translateY(-2px);
    }

    .gradient-text {
      background: linear-gradient(135deg, #818cf8 0%, #c084fc 50%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .progress-bar-glow {
      box-shadow: 0 0 12px currentColor;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0f172a;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
  </style>
  <script src="https://accounts.google.com/gsi/client" async defer></script>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-brand-500 selection:text-white">

  <!-- Toast Container -->
  <div id="toast-container" class="fixed top-20 right-6 z-50 flex flex-col gap-3 max-w-md pointer-events-none"></div>

  <!-- Navbar -->
  <nav class="glass-nav sticky top-0 z-40 px-6 py-4">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Brand Logo -->
      <div class="flex items-center gap-3 cursor-pointer" onclick="navigateTo('dashboard')">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 via-accent-purple to-accent-cyan flex items-center justify-center shadow-lg shadow-brand-500/30">
          <i class="fa-solid font-bold text-white text-xl">🎯</i>
        </div>
        <div>
          <span class="text-xl font-extrabold tracking-tight gradient-text">AI Interview Master</span>
          <span class="block text-xs text-slate-400 font-medium">B.Tech AI & Data Science Project</span>
        </div>
      </div>

      <!-- Nav Navigation Links -->
      <div id="nav-links" class="hidden md:flex items-center gap-1 bg-slate-900/60 p-1.5 rounded-2xl border border-slate-800/80">
        <button onclick="navigateTo('dashboard')" id="nav-dashboard" class="nav-btn px-4 py-2 rounded-xl text-sm font-semibold transition-all flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-chart-pie text-brand-500"></i> Dashboard
        </button>
        <button onclick="navigateTo('setup')" id="nav-setup" class="nav-btn px-4 py-2 rounded-xl text-sm font-semibold transition-all flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-play text-accent-cyan"></i> New Interview
        </button>
        <button onclick="navigateTo('history')" id="nav-history" class="nav-btn px-4 py-2 rounded-xl text-sm font-semibold transition-all flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-clock-rotate-left text-accent-purple"></i> History
        </button>
        <button onclick="navigateTo('profile')" id="nav-profile" class="nav-btn px-4 py-2 rounded-xl text-sm font-semibold transition-all flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-user text-accent-emerald"></i> Profile
        </button>
      </div>

      <!-- Action & Auth Button -->
      <div class="flex items-center gap-3">
        <a href="/docs" target="_blank" class="hidden sm:flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 border border-slate-700/50 transition-all">
          <i class="fa-solid fa-code text-brand-400"></i> FastAPI Docs
        </a>

        <div id="auth-state-area">
          <button onclick="openAuthModal()" class="px-5 py-2.5 rounded-xl text-sm font-semibold btn-gradient text-white shadow-lg">
            Login / Register
          </button>
        </div>
      </div>
    </div>
  </nav>

  <!-- Main Dynamic View Area -->
  <main class="flex-grow max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

    <!-- 1. DASHBOARD VIEW -->
    <div id="view-dashboard" class="view-panel space-y-8">
      
      <!-- Welcome Hero Banner -->
      <div class="relative overflow-hidden rounded-3xl glass-card p-8 sm:p-10 border border-brand-500/20">
        <div class="absolute -right-12 -bottom-12 w-64 h-64 bg-brand-600/20 rounded-full blur-3xl pointer-events-none"></div>
        <div class="relative z-10 max-w-2xl space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold">
            <span class="w-2 h-2 rounded-full bg-accent-emerald animate-pulse"></span> FastAPI + NLP AI System Active
          </div>
          <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-white">
            Welcome back, <span id="dash-user-name" class="gradient-text">Candidate</span>! 👋
          </h1>
          <p class="text-slate-400 text-base leading-relaxed">
            Practice technical & HR interview questions, receive instant semantic evaluation scored by NLP & Groq AI, and boost your hiring potential.
          </p>
          <div class="flex flex-wrap gap-4 pt-2">
            <button onclick="navigateTo('setup')" class="px-6 py-3 rounded-xl font-bold btn-gradient text-white flex items-center gap-2 shadow-xl">
              <i class="fa-solid fa-rocket"></i> Start Mock Interview
            </button>
            <button onclick="navigateTo('history')" class="px-6 py-3 rounded-xl font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition-all">
              <i class="fa-solid fa-list-check"></i> View Past Reports
            </button>
          </div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
          <div class="w-14 h-14 rounded-2xl bg-brand-500/10 border border-brand-500/20 flex items-center justify-center text-brand-400 text-2xl">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <div>
            <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Total Practice</p>
            <h3 id="stat-total" class="text-3xl font-extrabold text-white mt-1">0</h3>
            <span class="text-xs text-slate-500">Interviews Completed</span>
          </div>
        </div>

        <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
          <div class="w-14 h-14 rounded-2xl bg-accent-cyan/10 border border-accent-cyan/20 flex items-center justify-center text-accent-cyan text-2xl">
            <i class="fa-solid fa-chart-line"></i>
          </div>
          <div>
            <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Average Score</p>
            <h3 id="stat-avg" class="text-3xl font-extrabold text-white mt-1">0%</h3>
            <span class="text-xs text-slate-500">Across all sessions</span>
          </div>
        </div>

        <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
          <div class="w-14 h-14 rounded-2xl bg-accent-emerald/10 border border-accent-emerald/20 flex items-center justify-center text-accent-emerald text-2xl">
            <i class="fa-solid fa-trophy"></i>
          </div>
          <div>
            <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Best Score</p>
            <h3 id="stat-best" class="text-3xl font-extrabold text-white mt-1">0%</h3>
            <span class="text-xs text-slate-500">Peak Performance</span>
          </div>
        </div>

        <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
          <div class="w-14 h-14 rounded-2xl bg-accent-purple/10 border border-accent-purple/20 flex items-center justify-center text-accent-purple text-2xl">
            <i class="fa-solid fa-brain"></i>
          </div>
          <div>
            <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Evaluation Engine</p>
            <h3 id="stat-engine" class="text-xl font-bold text-slate-200 mt-1">NLP + TF-IDF</h3>
            <span class="text-xs text-accent-emerald flex items-center gap-1 mt-0.5"><i class="fa-solid fa-circle-check"></i> System Operational</span>
          </div>
        </div>
      </div>

      <!-- Charts & Insights Row -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Progression Chart -->
        <div class="lg:col-span-2 glass-card p-6 sm:p-7 rounded-3xl space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-lg font-bold text-white flex items-center gap-2">
                <i class="fa-solid fa-chart-area text-brand-400"></i> Score Progression
              </h2>
              <p class="text-xs text-slate-400">Your score trajectory over recent interview sessions</p>
            </div>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">Real-time</span>
          </div>
          <div class="h-64 relative">
            <canvas id="progressionChart"></canvas>
          </div>
        </div>

        <!-- Recommendations & Focus Areas -->
        <div class="glass-card p-6 sm:p-7 rounded-3xl space-y-5 flex flex-col justify-between">
          <div>
            <h2 class="text-lg font-bold text-white flex items-center gap-2 mb-1">
              <i class="fa-solid fa-lightbulb text-accent-amber"></i> Focus Recommendations
            </h2>
            <p class="text-xs text-slate-400 mb-4">AI-generated topics to improve technical depth</p>
            
            <div id="dash-recs-list" class="space-y-3">
              <!-- Dynamic items inserted via JS -->
              <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-sm text-slate-300 flex items-start gap-3">
                <i class="fa-solid fa-circle-notch fa-spin text-brand-400 mt-0.5"></i>
                <span>Loading insights...</span>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-800">
            <button onclick="navigateTo('setup')" class="w-full py-3 rounded-xl font-bold bg-brand-600/20 hover:bg-brand-600/30 text-brand-300 border border-brand-500/40 transition-all text-sm flex items-center justify-center gap-2">
              <i class="fa-solid fa-fire"></i> Practice Weak Topics
            </button>
          </div>
        </div>
      </div>

    </div>

    <!-- 2. SETUP INTERVIEW VIEW -->
    <div id="view-setup" class="view-panel max-w-3xl mx-auto space-y-8 hidden">
      <div class="text-center space-y-2">
        <h1 class="text-3xl font-extrabold text-white tracking-tight">Configure Your Mock Interview</h1>
        <p class="text-slate-400 text-sm">Select target role, difficulty level, and session parameters to initiate AI questions.</p>
      </div>

      <div class="glass-card p-8 rounded-3xl space-y-8">
        
        <!-- Job Role Selection -->
        <div class="space-y-3">
          <label class="block text-sm font-semibold text-slate-200 flex items-center gap-2">
            <i class="fa-solid fa-briefcase text-brand-400"></i> Select Target Job Role
          </label>
          <div id="roles-selector-container" class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <!-- Dynamic Job Role Cards -->
            <div class="p-4 rounded-2xl bg-slate-900/60 border border-slate-800 text-center text-slate-400 animate-pulse">
              Loading available roles...
            </div>
          </div>
        </div>

        <!-- Difficulty Level -->
        <div class="space-y-3">
          <label class="block text-sm font-semibold text-slate-200 flex items-center gap-2">
            <i class="fa-solid fa-layer-group text-accent-cyan"></i> Experience / Difficulty Level
          </label>
          <div class="grid grid-cols-3 gap-3">
            <button type="button" onclick="selectDifficulty('Beginner')" id="diff-Beginner" class="diff-btn p-4 rounded-2xl border border-slate-800 bg-slate-900/60 hover:bg-slate-800 text-center transition-all">
              <span class="block text-base font-bold text-emerald-400">Beginner</span>
              <span class="text-xs text-slate-400">Core Concepts</span>
            </button>
            <button type="button" onclick="selectDifficulty('Intermediate')" id="diff-Intermediate" class="diff-btn p-4 rounded-2xl border-2 border-brand-500 bg-brand-500/10 text-center transition-all">
              <span class="block text-base font-bold text-brand-400">Intermediate</span>
              <span class="text-xs text-slate-400">Standard Technical</span>
            </button>
            <button type="button" onclick="selectDifficulty('Advanced')" id="diff-Advanced" class="diff-btn p-4 rounded-2xl border border-slate-800 bg-slate-900/60 hover:bg-slate-800 text-center transition-all">
              <span class="block text-base font-bold text-purple-400">Advanced</span>
              <span class="text-xs text-slate-400">Deep Architecture</span>
            </button>
          </div>
        </div>

        <!-- Question Count & Mode -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-slate-200 flex items-center gap-2">
              <i class="fa-solid fa-list-ol text-accent-purple"></i> Question Count
            </label>
            <select id="setup-question-count" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-slate-200 focus:outline-none focus:border-brand-500 font-medium">
              <option value="3">3 Questions (Quick Practice ~5 mins)</option>
              <option value="5" selected>5 Questions (Standard ~10 mins)</option>
              <option value="10">10 Questions (Comprehensive ~20 mins)</option>
            </select>
          </div>

          <div class="space-y-2">
            <label class="block text-sm font-semibold text-slate-200 flex items-center gap-2">
              <i class="fa-solid fa-keyboard text-accent-emerald"></i> Response Mode
            </label>
            <select id="setup-mode" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-slate-200 focus:outline-none focus:border-brand-500 font-medium">
              <option value="TEXT" selected>Text Answer (Type & Submit)</option>
              <option value="VOICE" disabled>Voice / Speech-to-Text (Phase 2)</option>
            </select>
          </div>
        </div>

        <!-- Submit Button -->
        <button id="btn-start-interview" onclick="startInterviewSession()" class="w-full py-4 rounded-2xl font-extrabold btn-gradient text-white text-lg shadow-2xl flex items-center justify-center gap-3">
          <i class="fa-solid fa-play"></i> Start Interview Session
        </button>

      </div>
    </div>

    <!-- 3. MOCK INTERVIEW SCREEN VIEW -->
    <div id="view-interview" class="view-panel max-w-4xl mx-auto space-y-6 hidden">
      
      <!-- Top Status Header -->
      <div class="glass-card p-6 rounded-3xl flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span id="interview-role-badge" class="px-3.5 py-1.5 rounded-xl bg-brand-500/20 text-brand-300 font-bold text-sm border border-brand-500/30">
            Python Developer
          </span>
          <span id="interview-difficulty-badge" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-semibold text-xs border border-slate-700">
            Intermediate
          </span>
        </div>

        <!-- Timer Card -->
        <div class="flex items-center gap-3 bg-slate-900/80 px-4 py-2 rounded-2xl border border-slate-800">
          <i class="fa-solid fa-clock text-accent-amber animate-pulse"></i>
          <span class="text-xs font-medium text-slate-400">Time Elapsed:</span>
          <span id="interview-timer" class="font-mono text-lg font-bold text-white">00:00</span>
        </div>
      </div>

      <!-- Question Box -->
      <div class="glass-card p-8 rounded-3xl space-y-6 relative overflow-hidden">
        <div class="flex items-center justify-between border-b border-slate-800/80 pb-4">
          <span id="question-progress-text" class="text-xs font-bold uppercase tracking-wider text-slate-400">
            Question 1 of 5
          </span>
          <span id="question-category-badge" class="px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 text-xs font-bold border border-cyan-500/20">
            Technical
          </span>
        </div>

        <div class="space-y-3">
          <h2 id="current-question-text" class="text-xl sm:text-2xl font-bold text-white leading-snug">
            Loading question prompt...
          </h2>
        </div>

        <!-- Student Answer Field -->
        <div class="space-y-3 pt-2">
          <div class="flex items-center justify-between">
            <label class="text-sm font-semibold text-slate-300 flex items-center gap-2">
              <i class="fa-solid fa-pen-nib text-brand-400"></i> Your Detailed Technical Response:
            </label>
            <span id="word-count-badge" class="text-xs font-mono text-slate-400">0 words</span>
          </div>

          <textarea id="student-answer-input" rows="7" oninput="updateWordCount()" placeholder="Type your answer here clearly. Explain core concepts, syntax, use cases, and trade-offs to maximize your score..." class="w-full bg-slate-950/80 border border-slate-800 rounded-2xl p-4 text-slate-100 placeholder-slate-500 focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500 transition-all font-sans text-base leading-relaxed"></textarea>
        </div>

        <!-- Submit & Actions Footer -->
        <div class="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-slate-800/80">
          <button type="button" id="btn-cancel-interview" onclick="cancelCurrentInterview()" class="px-4 py-2.5 rounded-xl text-xs font-semibold text-rose-400 hover:bg-rose-500/10 transition-all">
            <i class="fa-solid fa-circle-xmark"></i> Cancel Interview
          </button>

          <button id="btn-submit-answer" onclick="submitAnswer()" class="px-8 py-3.5 rounded-2xl font-extrabold btn-gradient text-white shadow-xl flex items-center gap-2">
            <span>Submit Answer & Evaluate</span> <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- 4. INTERVIEW REPORT VIEW -->
    <div id="view-report" class="view-panel max-w-4xl mx-auto space-y-8 hidden">
      
      <!-- Summary Hero Card -->
      <div class="glass-card p-8 sm:p-10 rounded-3xl space-y-6 relative overflow-hidden border border-brand-500/20">
        <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="space-y-2 text-center sm:text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-semibold">
              <i class="fa-solid fa-circle-check"></i> Interview Session Completed
            </div>
            <h1 id="report-role-title" class="text-3xl font-extrabold text-white">Python Developer Report</h1>
            <p id="report-meta-text" class="text-slate-400 text-sm">Completed on 25 Sep • 5 Questions Evaluated</p>
          </div>

          <!-- Overall Score Dial/Badge -->
          <div class="flex flex-col items-center justify-center p-6 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-2xl min-w-[160px]">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-widest">Overall Score</span>
            <span id="report-overall-score" class="text-5xl font-extrabold gradient-text mt-1">0%</span>
            <span id="report-grade-label" class="text-xs font-bold text-emerald-400 mt-1">Grade: A</span>
          </div>
        </div>

        <!-- 4 Metric Score Bars -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-6 border-t border-slate-800">
          <div class="space-y-1">
            <span class="text-xs text-slate-400">Technical Accuracy</span>
            <div class="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
              <div id="bar-tech" class="h-full bg-brand-500 rounded-full" style="width: 0%"></div>
            </div>
            <span id="val-tech" class="text-sm font-bold text-slate-200">0%</span>
          </div>

          <div class="space-y-1">
            <span class="text-xs text-slate-400">Relevance</span>
            <div class="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
              <div id="bar-rel" class="h-full bg-accent-cyan rounded-full" style="width: 0%"></div>
            </div>
            <span id="val-rel" class="text-sm font-bold text-slate-200">0%</span>
          </div>

          <div class="space-y-1">
            <span class="text-xs text-slate-400">Completeness</span>
            <div class="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
              <div id="bar-comp" class="h-full bg-accent-purple rounded-full" style="width: 0%"></div>
            </div>
            <span id="val-comp" class="text-sm font-bold text-slate-200">0%</span>
          </div>

          <div class="space-y-1">
            <span class="text-xs text-slate-400">Communication</span>
            <div class="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
              <div id="bar-comm" class="h-full bg-accent-emerald rounded-full" style="width: 0%"></div>
            </div>
            <span id="val-comm" class="text-sm font-bold text-slate-200">0%</span>
          </div>
        </div>
      </div>

      <!-- Strengths & Recommendations -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Strong Areas -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <h3 class="text-lg font-bold text-emerald-400 flex items-center gap-2">
            <i class="fa-solid fa-circle-check"></i> Demonstrated Strengths
          </h3>
          <ul id="report-strengths-list" class="space-y-2 text-sm text-slate-300">
            <li class="flex items-start gap-2"><i class="fa-solid fa-check text-emerald-500 mt-1"></i> Good conceptual understanding</li>
          </ul>
        </div>

        <!-- Recommendations -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <h3 class="text-lg font-bold text-amber-400 flex items-center gap-2">
            <i class="fa-solid fa-lightbulb"></i> Key Recommendations
          </h3>
          <ul id="report-recs-list" class="space-y-2 text-sm text-slate-300">
            <li class="flex items-start gap-2"><i class="fa-solid fa-arrow-right text-amber-500 mt-1"></i> Review syntax details</li>
          </ul>
        </div>
      </div>

      <!-- Question-by-Question Breakdown -->
      <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-6">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <i class="fa-solid fa-list-check text-brand-400"></i> Per-Question Evaluation Breakdown
        </h2>

        <div id="report-questions-accordion" class="space-y-4">
          <!-- Dynamically populated via JS -->
        </div>
      </div>

      <div class="flex justify-center gap-4">
        <button onclick="navigateTo('setup')" class="px-8 py-3.5 rounded-2xl font-extrabold btn-gradient text-white shadow-xl">
          <i class="fa-solid fa-rotate-right"></i> Start Another Session
        </button>
        <button onclick="navigateTo('dashboard')" class="px-6 py-3.5 rounded-2xl font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">
          Back to Dashboard
        </button>
      </div>

    </div>

    <!-- 5. INTERVIEW HISTORY VIEW -->
    <div id="view-history" class="view-panel max-w-5xl mx-auto space-y-6 hidden">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-extrabold text-white tracking-tight">Interview History</h1>
          <p class="text-slate-400 text-sm">Review your past practice sessions and score progression.</p>
        </div>
        <button onclick="navigateTo('setup')" class="px-5 py-2.5 rounded-xl font-bold btn-gradient text-white text-sm">
          <i class="fa-solid fa-plus"></i> New Practice Session
        </button>
      </div>

      <div class="glass-card rounded-3xl overflow-hidden border border-slate-800">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs font-bold text-slate-400 uppercase border-b border-slate-800">
              <tr>
                <th class="px-6 py-4">ID</th>
                <th class="px-6 py-4">Job Role</th>
                <th class="px-6 py-4">Difficulty</th>
                <th class="px-6 py-4">Questions</th>
                <th class="px-6 py-4">Overall Score</th>
                <th class="px-6 py-4">Status</th>
                <th class="px-6 py-4">Date</th>
                <th class="px-6 py-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody id="history-table-body" class="divide-y divide-slate-800/60">
              <tr>
                <td colspan="8" class="px-6 py-8 text-center text-slate-400">
                  <i class="fa-solid fa-circle-notch fa-spin text-brand-400 mr-2"></i> Loading interview history...
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 6. PROFILE VIEW -->
    <div id="view-profile" class="view-panel max-w-2xl mx-auto space-y-6 hidden">
      <div class="glass-card p-8 rounded-3xl space-y-6">
        <div class="flex items-center gap-5 border-b border-slate-800 pb-6">
          <div class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-brand-600 to-accent-purple flex items-center justify-center text-white text-3xl font-bold shadow-xl">
            <i class="fa-solid fa-user-graduate"></i>
          </div>
          <div>
            <h2 id="prof-name" class="text-2xl font-bold text-white">Student User</h2>
            <p id="prof-email" class="text-slate-400 text-sm">student@example.com</p>
            <span id="prof-role-badge" class="inline-block mt-2 px-3 py-0.5 rounded-full bg-brand-500/20 text-brand-300 text-xs font-semibold border border-brand-500/30">
              Candidate Student
            </span>
          </div>
        </div>

        <form id="profile-form" onsubmit="handleProfileUpdate(event)" class="space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-slate-400 mb-1">Target Job Role</label>
              <input type="text" id="prof-target-role" placeholder="e.g. Python Developer" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-400 mb-1">Education Level</label>
              <input type="text" id="prof-education" placeholder="e.g. B.Tech AI & DS" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-slate-400 mb-1">College / University</label>
              <input type="text" id="prof-college" placeholder="Engineering College" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-400 mb-1">Branch / Major</label>
              <input type="text" id="prof-branch" placeholder="Artificial Intelligence & Data Science" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
            </div>
          </div>

          <button type="submit" class="w-full py-3 rounded-xl font-bold btn-gradient text-white text-sm shadow-lg mt-4">
            Save Profile Details
          </button>
        </form>

      <!-- Google Sign In Button -->
      <div class="pt-1">
        <div class="relative flex py-2 items-center">
          <div class="flex-grow border-t border-slate-800"></div>
          <span class="flex-shrink mx-3 text-xs font-bold text-slate-500 uppercase">Or Continue With</span>
          <div class="flex-grow border-t border-slate-800"></div>
        </div>
        <button type="button" onclick="handleGoogleSignIn()" class="w-full py-3 rounded-xl bg-slate-900/90 hover:bg-slate-800 border border-slate-700 text-white font-semibold text-sm flex items-center justify-center gap-3 transition-all shadow">
          <svg class="w-5 h-5" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.8 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.3 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3s.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 10.8 0 12s.7 2.3 1.9 4.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.3-6.4-5.2L1.9 16C3.7 19.7 7.5 23 12 23z"/></svg>
          <span>Sign in with Google</span>
        </button>
      </div>


        <div class="pt-4 border-t border-slate-800 text-center">
          <button onclick="handleLogout()" class="text-sm font-semibold text-rose-400 hover:text-rose-300 transition-all">
            <i class="fa-solid fa-right-from-bracket"></i> Sign Out of Session
          </button>
        </div>
      </div>
    </div>

  </main>

  <!-- AUTH MODAL -->
  <div id="auth-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/75 backdrop-blur-md hidden p-4">
    <div class="glass-card max-w-md w-full p-8 rounded-3xl space-y-6 relative border border-slate-700/80 shadow-2xl">
      <button onclick="closeAuthModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white transition-all">
        <i class="fa-solid fa-xmark text-xl"></i>
      </button>

      <div class="text-center space-y-1">
        <h2 id="auth-modal-title" class="text-2xl font-extrabold text-white">Sign In to Your Account</h2>
        <p class="text-slate-400 text-xs">Enter your details to sync interview progress.</p>
      </div>

      <!-- Quick Demo Login Bar -->
      <div class="bg-brand-500/10 border border-brand-500/20 p-3 rounded-2xl text-center space-y-2">
        <span class="text-xs font-bold text-brand-300 block">Quick Demo Login:</span>
        <div class="flex justify-center gap-2">
          <button type="button" onclick="quickLogin('student@ai.com', 'password123')" class="px-3 py-1.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white text-xs font-bold transition-all shadow">
            ⚡ Demo Student
          </button>
          <button type="button" onclick="quickLogin('admin@ai.com', 'password123')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition-all border border-slate-700">
            🛡 Demo Admin
          </button>
        </div>
      </div>

      <!-- Auth Form -->
      <form id="auth-form" onsubmit="handleAuthSubmit(event)" class="space-y-4">
        <div id="field-name" class="space-y-1 hidden">
          <label class="block text-xs font-semibold text-slate-300">Full Name</label>
          <input type="text" id="auth-name-input" placeholder="Srikar Candidate" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
        </div>

        <div class="space-y-1">
          <label class="block text-xs font-semibold text-slate-300">Email Address</label>
          <input type="email" id="auth-email-input" required placeholder="student@ai.com" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
        </div>

        <div class="space-y-1">
          <label class="block text-xs font-semibold text-slate-300">Password</label>
          <input type="password" id="auth-password-input" required placeholder="••••••••" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm focus:outline-none focus:border-brand-500">
        </div>

        <button type="submit" id="btn-auth-submit" class="w-full py-3.5 rounded-xl font-bold btn-gradient text-white text-sm shadow-xl">
          Sign In
        </button>
      </form>

      <!-- Google Sign In Button -->
      <div class="pt-1">
        <div class="relative flex py-2 items-center">
          <div class="flex-grow border-t border-slate-800"></div>
          <span class="flex-shrink mx-3 text-xs font-bold text-slate-500 uppercase">Or Continue With</span>
          <div class="flex-grow border-t border-slate-800"></div>
        </div>
        <button type="button" onclick="handleGoogleSignIn()" class="w-full py-3 rounded-xl bg-slate-900/90 hover:bg-slate-800 border border-slate-700 text-white font-semibold text-sm flex items-center justify-center gap-3 transition-all shadow">
          <svg class="w-5 h-5" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.8 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.3 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3s.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 10.8 0 12s.7 2.3 1.9 4.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.3-6.4-5.2L1.9 16C3.7 19.7 7.5 23 12 23z"/></svg>
          <span>Sign in with Google</span>
        </button>
      </div>


      <div class="text-center text-xs text-slate-400">
        <span id="auth-toggle-prompt">Don't have an account?</span>
        <button type="button" onclick="toggleAuthMode()" id="auth-toggle-btn" class="font-bold text-brand-400 hover:underline ml-1">
          Create Account
        </button>
      </div>
    </div>
  </div>

  <!-- ANSWER EVALUATION RESULT MODAL -->
  <div id="eval-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md hidden p-4">
    <div class="glass-card max-w-xl w-full p-8 rounded-3xl space-y-6 relative border border-slate-700 shadow-2xl">
      <div class="flex items-center justify-between border-b border-slate-800 pb-4">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
          <h3 class="text-lg font-bold text-white">AI Evaluation Completed</h3>
        </div>
        <span id="eval-overall-badge" class="px-4 py-1.5 rounded-full bg-brand-500/20 text-brand-300 font-extrabold text-base border border-brand-500/40">
          Overall: 85%
        </span>
      </div>

      <!-- Feedback Box -->
      <div class="bg-slate-900/90 border border-slate-800 p-4 rounded-2xl space-y-2">
        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">AI Evaluator Feedback</span>
        <p id="eval-feedback-text" class="text-sm text-slate-200 leading-relaxed">
          Good understanding of core concepts.
        </p>
      </div>

      <!-- Strengths & Improvements -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
        <div class="bg-emerald-500/10 border border-emerald-500/20 p-3.5 rounded-xl space-y-2">
          <span class="font-bold text-emerald-400 block"><i class="fa-solid fa-thumbs-up"></i> Strengths</span>
          <ul id="eval-strengths-list" class="space-y-1 text-slate-300"></ul>
        </div>
        <div class="bg-amber-500/10 border border-amber-500/20 p-3.5 rounded-xl space-y-2">
          <span class="font-bold text-amber-400 block"><i class="fa-solid fa-lightbulb"></i> Areas to Focus</span>
          <ul id="eval-improvements-list" class="space-y-1 text-slate-300"></ul>
        </div>
      </div>

      <button onclick="closeEvalModalNext()" class="w-full py-3.5 rounded-xl font-bold btn-gradient text-white text-sm shadow-xl flex items-center justify-center gap-2">
        <span>Proceed to Next Question</span> <i class="fa-solid fa-arrow-right"></i>
      </button>
    </div>
  </div>

  <!-- JAVASCRIPT APP LOGIC -->
  <script>
    // --- STATE & ENVIRONMENT ---
    let token = localStorage.getItem('token') || '';

    function getApiBaseUrl() {
      const saved = localStorage.getItem('custom_backend_url');
      if (saved && saved.trim()) return saved.trim().replace(/\/+$/, '');

      const host = window.location.hostname;
      const protocol = window.location.protocol;

      if (protocol !== 'file:' && (host === 'localhost' || host === '127.0.0.1')) {
        return '';
      }

      return 'https://ai-interview-backend-qlso.onrender.com';
    }

    const API_BASE_URL = getApiBaseUrl();
    let currentUser = null;
    let jobRoles = [];
    let selectedRoleId = null;
    let selectedDifficulty = 'Intermediate';

    let activeInterview = null;
    let timerInterval = null;
    let timerSeconds = 0;
    let pendingNextQuestion = null;
    let chartInstance = null;
    let isAuthRegisterMode = false;

    // --- API CALL HELPER WITH AUTO STALE TOKEN PURGE ---
    async function apiCall(path, options = {}) {
      const cleanPath = path.startsWith('/') ? path : '/' + path;
      let url = '';
      if (path.startsWith('http://') || path.startsWith('https://')) {
        url = path;
      } else {
        url = API_BASE_URL + cleanPath;
      }

      options.headers = options.headers || {};
      if (!(options.body instanceof FormData) && !options.headers['Content-Type']) {
        options.headers['Content-Type'] = 'application/json';
      }
      options.headers['Bypass-Tunnel-Reminder'] = 'true';

      if (token) {
        options.headers['Authorization'] = 'Bearer ' + token;
      }

      try {
        const res = await fetch(url, options);
        const contentType = res.headers.get('content-type') || '';

        let data;
        if (contentType.includes('application/json')) {
          data = await res.json();
        } else {
          const text = await res.text();
          data = { detail: text || res.statusText };
        }

        if (res.status === 401) {
          token = '';
          localStorage.removeItem('token');
          currentUser = null;
          updateAuthUI();
        }

        if (!res.ok) {
          const msg = (data && (data.detail || data.message)) || ('Request failed with status ' + res.status);
          throw new Error(typeof msg === 'object' ? JSON.stringify(msg) : msg);
        }
        return data;
      } catch (err) {
        console.error('API Call Error:', err);
        throw err;
      }
    }

    // --- TOAST SYSTEM ---
    function showToast(message, type) {
      if (message && message.includes('Could not validate credentials')) return;

      type = type || 'info';
      const container = document.getElementById('toast-container');
      if (!container) return;

      const toast = document.createElement('div');
      const bgClass = type === 'error' ? 'bg-rose-500/90 border-rose-400' : type === 'success' ? 'bg-emerald-500/90 border-emerald-400' : 'bg-brand-500/90 border-brand-400';
      toast.className = 'flex items-center gap-3 px-5 py-3.5 rounded-2xl text-white font-medium shadow-2xl backdrop-blur-md border text-sm transition-all duration-300 transform translate-y-2 opacity-0 ' + bgClass;

      const icon = type === 'error' ? 'fa-circle-xmark' : type === 'success' ? 'fa-circle-check' : 'fa-circle-info';
      toast.innerHTML = '<i class="fa-solid ' + icon + ' text-lg"></i><span>' + message + '</span>';

      container.appendChild(toast);
      setTimeout(() => {
        toast.classList.remove('translate-y-2', 'opacity-0');
      }, 10);

      setTimeout(() => {
        toast.classList.add('translate-y-2', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }

    // --- NAVIGATION LOGIC ---
    function navigateTo(viewId, skipScroll = false) {
      document.querySelectorAll('.view-panel').forEach(v => v.classList.add('hidden'));
      const target = document.getElementById('view-' + viewId);
      if (target) target.classList.remove('hidden');

      document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('bg-brand-600', 'text-white');
        btn.classList.add('text-slate-400', 'hover:bg-slate-800/60');
      });
      const activeNavBtn = document.getElementById('nav-' + viewId);
      if (activeNavBtn) {
        activeNavBtn.classList.remove('text-slate-400', 'hover:bg-slate-800/60');
        activeNavBtn.classList.add('bg-brand-600', 'text-white');
      }

      if (viewId === 'dashboard') loadDashboardData();
      if (viewId === 'setup') loadJobRoles();
      if (viewId === 'history') loadHistoryData();
      if (viewId === 'profile') loadProfileData();

      // Do NOT scroll upward when starting or navigating to interview view
      if (!skipScroll && viewId !== 'interview') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // --- AUTHENTICATION & GOOGLE SIGN-IN ---
    function openAuthModal() {
      const modal = document.getElementById('auth-modal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeAuthModal() {
      const modal = document.getElementById('auth-modal');
      if (modal) modal.classList.add('hidden');
    }

    function toggleAuthMode() {
      isAuthRegisterMode = !isAuthRegisterMode;
      const title = document.getElementById('auth-modal-title');
      if (title) title.innerText = isAuthRegisterMode ? 'Create Your Account' : 'Sign In to Your Account';

      const nameField = document.getElementById('field-name');
      if (nameField) nameField.classList.toggle('hidden', !isAuthRegisterMode);

      const submitBtn = document.getElementById('btn-auth-submit');
      if (submitBtn) submitBtn.innerText = isAuthRegisterMode ? 'Register & Sign In' : 'Sign In';

      const promptEl = document.getElementById('auth-toggle-prompt');
      if (promptEl) promptEl.innerText = isAuthRegisterMode ? 'Already have an account?' : "Don't have an account?";

      const toggleBtn = document.getElementById('auth-toggle-btn');
      if (toggleBtn) toggleBtn.innerText = isAuthRegisterMode ? 'Sign In' : 'Create Account';
    }

    function quickLogin(email, password) {
      const emailIn = document.getElementById('auth-email-input');
      const passIn = document.getElementById('auth-password-input');
      if (emailIn) emailIn.value = email;
      if (passIn) passIn.value = password;
      handleAuthSubmit(new Event('submit'));
    }

    async function handleAuthSubmit(e) {
      if (e && e.preventDefault) e.preventDefault();
      const emailIn = document.getElementById('auth-email-input');
      const passIn = document.getElementById('auth-password-input');
      const email = emailIn ? emailIn.value : '';
      const password = passIn ? passIn.value : '';

      if (isAuthRegisterMode) {
        const nameInput = document.getElementById('auth-name-input');
        const name = (nameInput && nameInput.value) ? nameInput.value : 'Candidate';
        await executeAuth('/api/auth/register', { name: name, email: email, password: password });
      } else {
        await executeAuth('/api/auth/login', { email: email, password: password });
      }
    }

    async function handleGoogleCredentialResponse(response) {
      if (response && response.credential) {
        await executeAuth('/api/auth/google', { credential: response.credential });
      }
    }

    async function handleGoogleSignIn() {
      if (window.google && window.google.accounts && window.google.accounts.id) {
        window.google.accounts.id.initialize({
          client_id: "1092837465019-google-app-id.apps.googleusercontent.com",
          callback: handleGoogleCredentialResponse
        });
        window.google.accounts.id.prompt();
      }

      const email = prompt("Google Sign In\n\nEnter your Google account email:", "student@ai.com");
      if (!email || !email.includes('@')) return;
      const name = email.split('@')[0].replace(/[._]/g, ' ');
      const formattedName = name.charAt(0).toUpperCase() + name.slice(1);
      await executeAuth('/api/auth/google', { email: email, name: formattedName });
    }

    async function executeAuth(endpoint, body) {
      try {
        const data = await apiCall(endpoint, {
          method: 'POST',
          body: JSON.stringify(body)
        });

        token = data.access_token;
        localStorage.setItem('token', token);
        currentUser = data.user;
        updateAuthUI();
        closeAuthModal();
        showToast('Welcome ' + (currentUser.name || '') + '! Authenticated successfully.', 'success');
        loadDashboardData();
      } catch (err) {
        showToast(err.message, 'error');
      }
    }

    async function fetchCurrentUser() {
      if (!token) {
        try {
          const data = await apiCall('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({ email: 'student@ai.com', password: 'password123' })
          });
          token = data.access_token;
          localStorage.setItem('token', token);
          currentUser = data.user;
        } catch (e) {}
        updateAuthUI();
        return;
      }
      try {
        currentUser = await apiCall('/api/auth/me');
        updateAuthUI();
      } catch (err) {
        token = '';
        localStorage.removeItem('token');
        currentUser = null;
        updateAuthUI();
        try {
          const data = await apiCall('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({ email: 'student@ai.com', password: 'password123' })
          });
          token = data.access_token;
          localStorage.setItem('token', token);
          currentUser = data.user;
          updateAuthUI();
        } catch (e) {}
      }
    }

    function handleLogout() {
      token = '';
      localStorage.removeItem('token');
      currentUser = null;
      updateAuthUI();
      showToast('Logged out successfully.', 'info');
      navigateTo('dashboard');
    }

    function updateAuthUI() {
      const authArea = document.getElementById('auth-state-area');
      const dashName = document.getElementById('dash-user-name');
      if (!authArea) return;

      if (currentUser) {
        if (dashName) dashName.innerText = currentUser.name;
        authArea.innerHTML =
          '<div class="flex items-center gap-3">' +
            '<div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-indigo-600 flex items-center justify-center text-white font-bold text-sm shadow-md">' +
              (currentUser.name ? currentUser.name.charAt(0).toUpperCase() : 'U') +
            '</div>' +
            '<div class="hidden md:block text-left">' +
              '<div class="text-xs font-bold text-white line-clamp-1">' + currentUser.name + '</div>' +
              '<div class="text-[10px] text-slate-400 capitalize">' + (currentUser.role || 'student') + '</div>' +
            '</div>' +
            '<button onclick="handleLogout()" title="Sign Out" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-rose-400 transition-colors ml-1">' +
              '<i class="fa-solid fa-right-from-bracket"></i>' +
            '</button>' +
          '</div>';
      } else {
        if (dashName) dashName.innerText = 'Candidate';
        authArea.innerHTML =
          '<button onclick="openAuthModal()" class="px-5 py-2.5 rounded-xl text-sm font-semibold btn-gradient text-white shadow-lg hover:shadow-brand-500/25 transition-all flex items-center gap-2">' +
            '<i class="fa-solid fa-right-to-bracket"></i>' +
            '<span>Sign In</span>' +
          '</button>';
      }
    }

    // --- JOB ROLES & SELECTION ---
    async function loadJobRoles() {
      try {
        jobRoles = await apiCall('/api/questions/roles');
        renderJobRoles(jobRoles);
      } catch (err) {
        console.error('Failed to load roles:', err);
      }
    }

    function renderJobRoles(roles) {
      const container = document.getElementById('roles-selector-container');
      if (!container) return;
      if (!roles || roles.length === 0) {
        container.innerHTML = '<div class="col-span-full p-6 text-center text-slate-400">No job roles found.</div>';
        return;
      }

      container.innerHTML = roles.map((role, idx) => {
        const isSelected = selectedRoleId ? selectedRoleId === role.id : idx === 0;
        const borderClass = isSelected ? 'border-2 border-brand-500 bg-brand-500/10' : 'border-slate-800 bg-slate-900/60';
        const iconClass = isSelected ? '' : 'opacity-0';
        return '<div onclick="selectJobRole(' + role.id + ')" id="role-card-' + role.id + '" class="role-card p-4 rounded-2xl border ' + borderClass + ' hover:bg-slate-800/80 cursor-pointer transition-all space-y-1">' +
          '<div class="flex items-center justify-between">' +
            '<h4 class="font-bold text-white text-base">' + role.role_name + '</h4>' +
            '<i class="fa-solid fa-circle-check role-check-icon text-brand-400 text-lg ' + iconClass + ' transition-opacity"></i>' +
          '</div>' +
          '<p class="text-xs text-slate-400 line-clamp-2">' + (role.description || 'Practice role-specific interview questions.') + '</p>' +
        '</div>';
      }).join('');

      if (roles.length > 0 && !selectedRoleId) {
        selectedRoleId = roles[0].id;
      }
    }

    function selectJobRole(id) {
      selectedRoleId = id;
      document.querySelectorAll('.role-card').forEach(el => {
        el.classList.remove('border-2', 'border-brand-500', 'bg-brand-500/10');
        el.classList.add('border-slate-800', 'bg-slate-900/60');
      });
      document.querySelectorAll('.role-check-icon').forEach(el => el.classList.add('opacity-0'));

      const target = document.getElementById('role-card-' + id);
      if (target) {
        target.classList.add('border-2', 'border-brand-500', 'bg-brand-500/10');
        const icon = target.querySelector('.role-check-icon');
        if (icon) icon.classList.remove('opacity-0');
      }
    }

    function selectDifficulty(diff) {
      selectedDifficulty = diff;
      document.querySelectorAll('.diff-btn').forEach(btn => {
        btn.classList.remove('border-2', 'border-brand-500', 'bg-brand-500/10');
        btn.classList.add('border-slate-800', 'bg-slate-900/60');
      });
      const target = document.getElementById('diff-' + diff);
      if (target) {
        target.classList.add('border-2', 'border-brand-500', 'bg-brand-500/10');
      }
    }

    // --- INTERVIEW SESSION WORKFLOW ---
    async function startInterviewSession() {
      if (!token) {
        await fetchCurrentUser();
      }

      if (!token) {
        openAuthModal();
        showToast('Please login first to start an interview session.', 'info');
        return;
      }

      if (!selectedRoleId) {
        showToast('Please select a job role.', 'error');
        return;
      }

      const countInput = document.getElementById('setup-question-count');
      const count = countInput ? parseInt(countInput.value) || 5 : 5;
      const modeInput = document.getElementById('setup-mode');
      const mode = modeInput ? modeInput.value : 'TEXT';

      const btn = document.getElementById('btn-start-interview');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Initializing AI Questions...';
      }

      try {
        const data = await apiCall('/api/interviews/start', {
          method: 'POST',
          body: JSON.stringify({
            role_id: selectedRoleId,
            difficulty: selectedDifficulty,
            total_questions: count,
            mode: mode
          })
        });

        activeInterview = data;
        renderInterviewQuestion(data.current_question, 1, data.total_questions);
        startTimer();
        navigateTo('interview');
        showToast('Mock Interview Session Started!', 'success');
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = '<i class="fa-solid fa-play"></i> Start Interview Session';
        }
      }
    }

    function renderInterviewQuestion(q, currentIdx, total) {
      if (!activeInterview || !q) return;
      document.getElementById('interview-role-badge').innerText = activeInterview.role_name || 'Technical';
      document.getElementById('interview-difficulty-badge').innerText = activeInterview.difficulty || 'Intermediate';
      document.getElementById('question-progress-text').innerText = 'Question ' + currentIdx + ' of ' + total;
      document.getElementById('question-category-badge').innerText = q.category || 'Technical';
      document.getElementById('current-question-text').innerText = q.question_text || '';
      document.getElementById('student-answer-input').value = '';
      updateWordCount();
    }

    function updateWordCount() {
      const textInput = document.getElementById('student-answer-input');
      const text = textInput ? textInput.value.trim() : '';
      const words = text ? text.split(/\s+/).length : 0;
      const badge = document.getElementById('word-count-badge');
      if (badge) badge.innerText = words + ' words';
    }

    function startTimer() {
      stopTimer();
      timerSeconds = 0;
      const display = document.getElementById('interview-timer');
      timerInterval = setInterval(() => {
        timerSeconds++;
        const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
        const secs = String(timerSeconds % 60).padStart(2, '0');
        if (display) display.innerText = mins + ':' + secs;
      }, 1000);
    }

    function stopTimer() {
      if (timerInterval) clearInterval(timerInterval);
    }

    async function submitAnswer() {
      const textInput = document.getElementById('student-answer-input');
      const text = textInput ? textInput.value.trim() : '';
      if (!text) {
        showToast('Please enter an answer before submitting.', 'error');
        return;
      }

      const btn = document.getElementById('btn-submit-answer');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-brain fa-spin"></i> NLP Evaluating...';
      }

      try {
        const interviewId = activeInterview ? (activeInterview.interview_id || (activeInterview.interview ? activeInterview.interview.id : activeInterview.id)) : null;
        if (!interviewId) throw new Error('No active interview ID found.');

        const data = await apiCall('/api/interviews/' + interviewId + '/answer', {
          method: 'POST',
          body: JSON.stringify({
            answer_text: text,
            duration_seconds: timerSeconds
          })
        });

        displayEvalModal(data.evaluation, data.next_question, data.interview_complete);
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = '<span>Submit Answer & Evaluate</span> <i class="fa-solid fa-arrow-right"></i>';
        }
      }
    }

    function displayEvalModal(evalData, nextQuestion, isComplete) {
      pendingNextQuestion = nextQuestion;
      const overall = evalData && evalData.overall_score ? Math.round(evalData.overall_score) : 0;
      document.getElementById('eval-overall-badge').innerText = 'Overall: ' + overall + '%';
      document.getElementById('eval-feedback-text').innerText = (evalData && evalData.feedback) || 'Answer processed.';

      const strList = document.getElementById('eval-strengths-list');
      const strengths = (evalData && evalData.strengths) ? (typeof evalData.strengths === 'string' ? JSON.parse(evalData.strengths) : evalData.strengths) : ['Good effort'];
      if (strList) {
        strList.innerHTML = strengths.map(s => '<li class="flex items-start gap-2"><i class="fa-solid fa-check text-emerald-400 mt-1"></i><span>' + s + '</span></li>').join('');
      }

      const impList = document.getElementById('eval-improvements-list');
      const improvements = (evalData && evalData.improvements) ? (typeof evalData.improvements === 'string' ? JSON.parse(evalData.improvements) : evalData.improvements) : ['Keep practicing'];
      if (impList) {
        impList.innerHTML = improvements.map(i => '<li class="flex items-start gap-2"><i class="fa-solid fa-lightbulb text-amber-400 mt-1"></i><span>' + i + '</span></li>').join('');
      }

      setMetricBar('rel', evalData ? evalData.relevance_score : 0);
      setMetricBar('acc', evalData ? evalData.accuracy_score : 0);
      setMetricBar('comp', evalData ? evalData.completeness_score : 0);

      const btnNext = document.getElementById('btn-eval-next');
      if (btnNext) {
        btnNext.innerText = isComplete ? 'Complete & View Full Report' : 'Next Question';
      }

      const modal = document.getElementById('eval-modal');
      if (modal) modal.classList.remove('hidden');
    }

    function setMetricBar(metric, val) {
      const num = Math.round(val || 0);
      const bar = document.getElementById('eval-' + metric + '-bar');
      const txt = document.getElementById('eval-' + metric + '-val');
      if (bar) bar.style.width = num + '%';
      if (txt) txt.innerText = num + '%';
    }

    async function closeEvalModalNext() {
      const modal = document.getElementById('eval-modal');
      if (modal) modal.classList.add('hidden');

      if (pendingNextQuestion) {
        const totalQ = activeInterview.total_questions || 5;
        const currentQIdx = (activeInterview.questions_answered || 0) + 1;
        activeInterview.questions_answered = currentQIdx;
        renderInterviewQuestion(pendingNextQuestion, currentQIdx, totalQ);
        startTimer();
        pendingNextQuestion = null;
      } else {
        stopTimer();
        const btn = document.getElementById('btn-submit-answer');
        if (btn) btn.disabled = true;

        showToast('Interview Session Complete! Generating Report...', 'success');
        try {
          const interviewId = activeInterview ? (activeInterview.interview_id || (activeInterview.interview ? activeInterview.interview.id : activeInterview.id)) : null;
          const reportData = await apiCall('/api/interviews/' + interviewId + '/complete', {
            method: 'POST'
          });
          renderPerformanceReport(reportData);
          navigateTo('report');
        } catch (err) {
          showToast('Error completing session: ' + err.message, 'error');
        }
      }
    }

    // --- INSTANT UNCONDITIONAL CANCEL INTERVIEW HANDLER ---
    async function cancelCurrentInterview() {
      let proceed = true;
      try {
        proceed = confirm('Are you sure you want to cancel this interview session? Progress will be lost.');
      } catch (e) {
        proceed = true;
      }
      if (!proceed) return;

      const interviewId = activeInterview ? (activeInterview.interview_id || (activeInterview.interview ? activeInterview.interview.id : activeInterview.id)) : null;

      // Immediately & unconditionally switch UI state back to dashboard
      stopTimer();
      activeInterview = null;
      navigateTo('dashboard');
      showToast('Interview cancelled.', 'info');

      // Send cancel notification to backend asynchronously in background
      if (interviewId) {
        apiCall('/api/interviews/' + interviewId, { method: 'DELETE' }).catch(err => {
          console.log('Background cancel notification:', err);
        });
      }
    }

    // --- PERFORMANCE REPORT & DASHBOARD ---
    function renderPerformanceReport(data) {
      const iv = data.interview || data;
      const score = Math.round(iv.overall_score || 0);

      document.getElementById('report-role-title').innerText = (iv.role_name || 'Technical') + ' Performance Report';
      document.getElementById('report-meta-text').innerText = (iv.difficulty || 'Intermediate') + ' Difficulty | Mode: ' + (iv.mode || 'TEXT') + ' | ' + (data.answers ? data.answers.length : 0) + ' Questions Evaluated';

      document.getElementById('report-overall-score').innerText = score + '%';
      document.getElementById('report-grade-label').innerText = score >= 85 ? 'Grade: A (Excellent)' : score >= 70 ? 'Grade: B (Good)' : 'Grade: C (Needs Practice)';

      const strongList = document.getElementById('report-strengths-list');
      const strongAreas = iv.strong_areas ? (typeof iv.strong_areas === 'string' ? JSON.parse(iv.strong_areas) : iv.strong_areas) : ['Strong domain knowledge'];
      if (strongList) {
        strongList.innerHTML = strongAreas.map(s => '<li class="flex items-start gap-2"><i class="fa-solid fa-circle-check text-emerald-400 mt-1"></i><span>' + s + '</span></li>').join('');
      }

      const recsList = document.getElementById('report-recs-list');
      const recommendations = iv.recommendations ? (typeof iv.recommendations === 'string' ? JSON.parse(iv.recommendations) : iv.recommendations) : ['Continue practicing practice questions'];
      if (recsList) {
        recsList.innerHTML = recommendations.map(r => '<li class="flex items-start gap-2"><i class="fa-solid fa-lightbulb text-amber-400 mt-1"></i><span>' + r + '</span></li>').join('');
      }

      const accordion = document.getElementById('report-questions-accordion');
      if (accordion && data.answers) {
        accordion.innerHTML = data.answers.map((ans, idx) => {
          const ev = ans.evaluation || {};
          const ov = Math.round(ev.overall_score || 0);
          return '<div class="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-3">' +
            '<div class="flex items-center justify-between text-xs text-slate-400">' +
              '<span class="font-bold text-brand-400">Q' + (idx + 1) + '</span>' +
              '<span class="px-2.5 py-1 rounded-full bg-brand-500/10 text-brand-400 font-semibold">' + ov + '% Score</span>' +
            '</div>' +
            '<h5 class="font-bold text-white text-sm">' + ans.question_text + '</h5>' +
            '<div class="p-3 rounded-xl bg-slate-950/60 text-xs text-slate-300 font-mono">' + ans.answer_text + '</div>' +
            '<p class="text-xs text-slate-400 italic">' + (ev.feedback || 'Evaluated successfully.') + '</p>' +
          '</div>';
        }).join('');
      }
    }

    async function loadDashboardData() {
      if (!token) return;
      try {
        const [sum, prog, recsData] = await Promise.all([
          apiCall('/api/dashboard/summary').catch(() => ({})),
          apiCall('/api/dashboard/progress').catch(() => ([])),
          apiCall('/api/dashboard/recommendations').catch(() => ({ recommendations: [] }))
        ]);

        const statTotal = document.getElementById('stat-total');
        const statAvg = document.getElementById('stat-avg');
        const statBest = document.getElementById('stat-best');

        if (statTotal) statTotal.innerText = sum.total_interviews || 0;
        if (statAvg) statAvg.innerText = Math.round(sum.avg_score || 0) + '%';
        if (statBest) statBest.innerText = Math.round(sum.best_score || 0) + '%';

        if (prog && prog.length > 0) {
          renderProgressionChart(prog);
        }

        const recsList = document.getElementById('dash-recs-list');
        if (recsList && recsData && recsData.recommendations) {
          recsList.innerHTML = recsData.recommendations.map(r =>
            '<li class="flex items-start gap-2.5 text-xs text-slate-300"><i class="fa-solid fa-sparkles text-brand-400 mt-0.5"></i><span>' + r + '</span></li>'
          ).join('');
        }
      } catch (err) {
        console.error('Error loading dashboard:', err);
      }
    }

    function renderProgressionChart(data) {
      const canvas = document.getElementById('progressionChart');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      if (chartInstance) chartInstance.destroy();

      const labels = data.map((d, i) => 'Session ' + (i + 1));
      const scores = data.map(d => Math.round(d.score || 0));

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Overall Score (%)',
            data: scores,
            borderColor: '#6366f1',
            backgroundColor: 'rgba(99, 102, 241, 0.1)',
            tension: 0.4,
            fill: true,
            pointBackgroundColor: '#818cf8',
            pointRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: { min: 0, max: 100, grid: { color: 'rgba(255,255,255,0.05)' } },
            x: { grid: { display: false } }
          }
        }
      });
    }

    async function loadHistoryData() {
      if (!token) return;
      try {
        const list = await apiCall('/api/interviews/history');
        const tbody = document.getElementById('history-table-body');
        if (!tbody) return;

        if (!list || list.length === 0) {
          tbody.innerHTML = '<tr><td colspan="6" class="p-6 text-center text-slate-400 text-sm">No interview history found.</td></tr>';
          return;
        }

        tbody.innerHTML = list.map(iv => {
          const date = iv.started_at ? new Date(iv.started_at).toLocaleDateString() : 'N/A';
          const score = iv.overall_score !== null ? Math.round(iv.overall_score) + '%' : 'In Progress';
          return '<tr class="border-b border-slate-800/60 hover:bg-slate-800/30 transition-colors">' +
            '<td class="py-4 px-4 font-bold text-white text-sm">' + iv.role_name + '</td>' +
            '<td class="py-4 px-4 text-xs text-slate-300">' + iv.difficulty + '</td>' +
            '<td class="py-4 px-4 text-xs text-slate-400">' + date + '</td>' +
            '<td class="py-4 px-4 text-xs font-bold text-brand-400">' + score + '</td>' +
            '<td class="py-4 px-4 text-xs"><span class="px-2.5 py-1 rounded-full text-[10px] font-bold ' + (iv.status === 'COMPLETED' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-amber-500/10 text-amber-400 border border-amber-500/20') + '">' + iv.status + '</span></td>' +
            '<td class="py-4 px-4 text-xs"><button onclick="viewPastReport(' + iv.id + ')" class="px-3 py-1.5 rounded-xl bg-brand-600/20 hover:bg-brand-600/40 text-brand-300 font-bold transition-all">View Report</button></td>' +
          '</tr>';
        }).join('');
      } catch (err) {
        console.error('Error loading history:', err);
      }
    }

    async function viewPastReport(id) {
      try {
        const reportData = await apiCall('/api/evaluations/' + id);
        renderPerformanceReport(reportData);
        navigateTo('report');
      } catch (err) {
        showToast('Failed to load past report: ' + err.message, 'error');
      }
    }

    async function loadProfileData() {
      if (!currentUser) await fetchCurrentUser();
      if (!currentUser) return;
      document.getElementById('prof-name').innerText = currentUser.name || '';
      document.getElementById('prof-email').innerText = currentUser.email || '';
      document.getElementById('prof-target-role').value = currentUser.target_role || '';
      document.getElementById('prof-education').value = currentUser.education || '';
      document.getElementById('prof-college').value = currentUser.college || '';
      document.getElementById('prof-branch').value = currentUser.branch || '';
    }

    async function saveProfileData(e) {
      if (e && e.preventDefault) e.preventDefault();
      try {
        const updated = await apiCall('/api/auth/me', {
          method: 'PUT',
          body: JSON.stringify({
            target_role: document.getElementById('prof-target-role').value,
            education: document.getElementById('prof-education').value,
            college: document.getElementById('prof-college').value,
            branch: document.getElementById('prof-branch').value
          })
        });
        currentUser = updated;
        showToast('Profile updated successfully!', 'success');
      } catch (err) {
        showToast(err.message, 'error');
      }
    }

    // --- ATTACH ALL HANDLERS GLOBALLY TO WINDOW OBJECT ---
    window.navigateTo = navigateTo;
    window.openAuthModal = openAuthModal;
    window.closeAuthModal = closeAuthModal;
    window.toggleAuthMode = toggleAuthMode;
    window.quickLogin = quickLogin;
    window.handleAuthSubmit = handleAuthSubmit;
    window.handleGoogleSignIn = handleGoogleSignIn;
    window.handleLogout = handleLogout;
    window.selectJobRole = selectJobRole;
    window.selectDifficulty = selectDifficulty;
    window.startInterviewSession = startInterviewSession;
    window.submitAnswer = submitAnswer;
    window.closeEvalModalNext = closeEvalModalNext;
    window.cancelCurrentInterview = cancelCurrentInterview;
    window.viewPastReport = viewPastReport;
    window.saveProfileData = saveProfileData;

    // --- INITIALIZE APP ON DOM READY & ATTACH DIRECT LISTENERS ---
    document.addEventListener('DOMContentLoaded', async () => {
      await fetchCurrentUser();
      await loadJobRoles();
      loadDashboardData();

      const btnCancel = document.getElementById('btn-cancel-interview');
      if (btnCancel) {
        btnCancel.addEventListener('click', cancelCurrentInterview);
      }
    });
  </script>
</body>
</html>"""
