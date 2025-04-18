---

# 🌉 Cultural Bridge Game

An interactive, multi-modal AI simulation platform for storytelling, diplomacy, and ethical reasoning. Powered by **FastAPI**, **Ollama (LLaMA3 + MiniLM embeddings)**, and **ChromaDB**, this project lets users explore:

- 🧙‍♂️ Role-Playing Story Arcs  
- 🕊️ Conflict Resolution Simulations  
- 🎙️ Ethical Debate Scenarios  
- 📚 Story Generation via RAG (Retrieval-Augmented Generation)  

---

## 🚀 Core Features

### 📚 Story Mode (RAG)
- Context-aware story generation using embeddings
- Embeds and retrieves past story events from ChromaDB
- Supports branching narrative with persistence

### 🧭 Role-Playing Mode
- Persona-driven choices in fantasy/political settings
- Available actions vary by role and game state
- Interactive session tracking with decision impact

### 🕊️ Conflict Resolution Mode
- Historical simulations (e.g., India-Pakistan, Israel-Palestine, Rwanda)
- Player as Side A, Side B, or Neutral Facilitator
- Dynamic `tension_level` impacts scenario flow
- KALKI scoring system for:
  - 🧠 Empathy
  - 🕊️ Diplomacy
  - 🕰 Historical Accuracy
  - ⚖️ Ethical Balance

### 🎤 Debate Mode
- Generates culturally sensitive moral dilemmas
- Evaluates user stance with reasoning + contextual analysis
- Embedding-powered retrieval for argument enhancement

---

## 🛠 Tech Stack

| Component        | Technology                    |
|------------------|-------------------------------|
| **Backend**      | FastAPI                       |
| **LLM**          | Ollama (`llama3`, `all-minilm`)|
| **Vector DB**    | ChromaDB                      |
| **Frontend**     | Jinja2 + HTML templates       |
| **CORS**         | Enabled for dev-friendly access |

---

## 📂 Project Structure

```
app/
├── controllers/       # Business logic per mode
├── db/                # ChromaDB singleton setup
├── routes/            # FastAPI API routes
├── schemas/           # Pydantic models and types
├── templates/         # HTML templates for basic UI
└── main.py            # Application entry point
```

---

## 🔧 Setup Instructions

### 1. Install Dependencies
```bash
pip install fastapi uvicorn python-dotenv chromadb ollama
```
> Make sure `ollama` is installed and running.  
> 👉 [https://ollama.com](https://ollama.com)

### 2. Start the API
```bash
uvicorn app.main:app --reload
```

### 3. Access the App
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)  
- Homepage: [http://localhost:8000](http://localhost:8000)

---

## 🔄 API Endpoints

### 📚 Story Mode
| Endpoint            | Method | Description |
|---------------------|--------|-------------|
| `/api/v1/story`     | POST | Start a new story |
| `/api/v1/add_story` | POST | Continue story |

### 🧭 RPG Mode
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/rpg/start` | POST | Begin role-playing session |
| `/api/v1/rpg/progress` | POST | Advance narrative |

### 🕊 Conflict Resolution
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/conflict_resolution` | POST | Play scenario as leader/diplomat/facilitator |

### 🎤 Debate Mode
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/debate/prompt` | GET | Generate moral dilemma |
| `/api/v1/debate/evaluate` | POST | Score user’s argument |

---

## 📊 KALKI Score System

| Category | Max Points | Description |
|----------|------------|-------------|
| **Empathy** | 30 | Understanding multiple viewpoints |
| **Diplomatic Skill** | 30 | Constructive dialogue, compromise |
| **Historical Accuracy** | 20 | Informed by real events |
| **Ethical Balance** | 20 | Fairness, neutrality, principles |

---

## 📘 License
MIT License — Free to use, improve, and extend.

---