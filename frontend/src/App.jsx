import { useState, useEffect, useRef } from 'react'
import './App.css'

// Backend API base: env override, or production fallback when not on localhost, or same-origin for dev.
const PRODUCTION_API_ORIGIN = 'https://mathmentor-knx7.onrender.com'
const origin =
  import.meta.env.VITE_API_ORIGIN ||
  (typeof window !== 'undefined' && !/localhost|127\.0\.0\.1/.test(window.location.hostname) ? PRODUCTION_API_ORIGIN : '')
const API = origin + '/api'

async function parseJson(res) {
  const ct = res.headers.get('content-type') || ''
  if (!ct.includes('application/json')) {
    throw new Error('Server returned a non-JSON response. Is the API running?')
  }
  try {
    return await res.json()
  } catch (e) {
    throw new Error('Server returned invalid JSON. Is the API running?')
  }
}

const EXAMPLE_PROMPTS = [
  'How do I add fractions with different denominators?',
  'Explain the Pythagorean theorem.',
  'What is place value?',
  'How do I solve 2x + 5 = 15?',
]

function SendIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M22 2L11 13" />
      <path d="M22 2L15 22L11 13L2 9L22 2Z" />
    </svg>
  )
}

function App() {
  const [grade, setGrade] = useState(6)
  const [domainId, setDomainId] = useState('')
  const [domains, setDomains] = useState([])
  const [question, setQuestion] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const bottomRef = useRef(null)
  const inputRef = useRef(null)

  useEffect(() => {
    fetch(`${API}/standards/grade/${grade}`)
      .then((r) => parseJson(r))
      .then((data) => {
        if (data.domains) setDomains(data.domains)
        else setDomains([])
      })
      .catch(() => setDomains([]))
  }, [grade])

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const sendQuestion = async () => {
    const q = question.trim()
    if (!q || loading) return

    const userMsg = { role: 'user', text: q }
    setMessages((m) => [...m, userMsg])
    setQuestion('')
    setLoading(true)
    setError(null)

    try {
      const res = await fetch(`${API}/ask/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          grade,
          question: q,
          domain_id: domainId || null,
        }),
      })
      const data = await parseJson(res)
      if (!res.ok) throw new Error(data.detail || 'Request failed')

      setMessages((m) => [
        ...m,
        { role: 'assistant', text: data.answer, error: data.error || null },
      ])
    } catch (err) {
      setError(err.message)
      setMessages((m) => [
        ...m,
        {
          role: 'assistant',
          text: 'Something went wrong. Is the backend running?',
          error: true,
        },
      ])
    } finally {
      setLoading(false)
      inputRef.current?.focus()
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendQuestion()
    }
  }

  const useExample = (text) => {
    setQuestion(text)
    inputRef.current?.focus()
  }

  return (
    <div className="layout">
      <header className="header">
        <div className="headerInner">
          <div className="logo" aria-hidden>∑</div>
          <div className="titleBlock">
            <h1>Math Mentor</h1>
            <p className="subtitle">Grades 1–12 · Common Core aligned</p>
          </div>
        </div>

        <div className="controlsCard">
          <label className="label">
            Grade
            <select
              className="select"
              value={grade}
              onChange={(e) => setGrade(Number(e.target.value))}
            >
              {Array.from({ length: 12 }, (_, i) => i + 1).map((g) => (
                <option key={g} value={g}>
                  Grade {g}
                </option>
              ))}
            </select>
          </label>
          <label className="label">
            Topic (optional)
            <select
              className="select"
              value={domainId}
              onChange={(e) => setDomainId(e.target.value)}
            >
              <option value="">Any</option>
              {domains.map((d) => (
                <option key={d.id} value={d.id}>
                  {d.name}
                </option>
              ))}
            </select>
          </label>
        </div>
        {error && <p className="errorBanner">{error}</p>}
      </header>

      <main className="chat">
        {messages.length === 0 && (
          <div className="welcome">
            <p>Ask any math question. Answers are tailored to your grade and aligned with USA Common Core State Standards.</p>
            <p className="hint">Click an example below or type your own.</p>
            <div className="examplePrompts">
              {EXAMPLE_PROMPTS.map((prompt, i) => (
                <button
                  key={i}
                  type="button"
                  className="examplePrompt"
                  onClick={() => useExample(prompt)}
                >
                  {prompt}
                </button>
              ))}
            </div>
          </div>
        )}

        <ul className="messageList">
          {messages.map((msg, i) => (
            <li key={i} className={`message message--${msg.role}`}>
              <div className="messageAvatar" aria-hidden>
                {msg.role === 'user' ? 'Y' : '∑'}
              </div>
              <div className="messageBody">
                <span className="messageRole">{msg.role === 'user' ? 'You' : 'Mentor'}</span>
                <div className={`messageContent ${msg.error ? 'messageContent--error' : ''}`}>
                  {msg.text.split('\n').map((line, j) => (
                    <p key={j}>{line || '\u00A0'}</p>
                  ))}
                </div>
              </div>
            </li>
          ))}
          {loading && (
            <li className="message message--assistant">
              <div className="messageAvatar" aria-hidden>∑</div>
              <div className="messageBody">
                <span className="messageRole">Mentor</span>
                <div className="messageContent typing">
                  <span className="typingDots">
                    <span /><span /><span />
                  </span>
                </div>
              </div>
            </li>
          )}
        </ul>
        <div ref={bottomRef} />
      </main>

      <footer className="inputBar">
        <div className="inputWrap">
          <textarea
            ref={inputRef}
            className="input"
            placeholder="Ask a math question…"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={handleKeyDown}
            rows={2}
            disabled={loading}
          />
        </div>
        <button
          type="button"
          className="sendBtn"
          onClick={sendQuestion}
          disabled={loading || !question.trim()}
          aria-label="Send question"
        >
          <SendIcon />
          Ask
        </button>
      </footer>
    </div>
  )
}

export default App
