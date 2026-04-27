# 🤖 Grid07 Assignment – LangGraph Autonomous Bot System

## 🚀 Overview

This project implements a **three-phase agentic AI system** that:

- Routes posts to persona-based bots using embeddings  
- Generates contextual posts using external information  
- Defends against prompt-injection attacks using a RAG-based Combat Engine  

The system demonstrates a complete **routing → retrieval → generation → defense pipeline**.

> Developed and tested on Windows 10 using PyCharm

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Grid07_assignment.git
cd Grid07_assignment
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

Note: Embeddings are generated locally using SentenceTransformers, so no additional API key is required.

🧠 Phase 1 + Phase 2 – Routing & Content Generation
🎯 Goal
Route an input post to the most relevant bot persona
Generate a persona-aligned post using external context
▶️ How to Run
python main.py
🔄 Execution Flow
User Post
  ↓
Embedding (SentenceTransformers - MiniLM)
  ↓
FAISS Similarity Search
  ↓
Bot Selection
  ↓
Query Generation (LLM)
  ↓
Search Tool (mock search)
  ↓
Context Injection
  ↓
Post Generation (LLM)
📌 Sample Output
B → score: 0.38
C → score: 0.35
A → score: 0.20
Matched Bots: ['B']

🔥 GENERATED POSTS:

{
  "bot_id": "B",
  "post_content": "AI is another tool for billionaires to control labor..."
}
⚙️ Key Design Decisions
🔹 Threshold Adjustment
Final threshold used: ~0.35 (empirically tuned)

Note: Although 0.85 was suggested, 
the chosen embedding model produces cosine similarity scores in the 0.3–0.6 range.
Therefore, the threshold was adjusted to ensure correct semantic routing.

The system prioritizes semantic correctness over absolute similarity values.

🔹 Manual Tool Invocation
Search tool is invoked explicitly in code
Ensures deterministic and reliable execution
🔹 Structured Query Generation
LLM generates topic-based queries
Improves retrieval quality and relevance
📂 Internal Components
router/
  └── vector_store.py

content_engine/
  ├── llm.py
  ├── nodes.py
  └── tools.py

main.py

Routing and content generation are orchestrated through main.py.

🛡️ Phase 3 – Combat Engine (Prompt Injection Defense)
🎯 Goal

Defend against prompt-injection attacks while maintaining persona integrity.

▶️ How to Run
python combat_engine/test_defense.py
📌 Sample Output
🤖 Bot Defense Reply:
I must respectfully disagree with the claim...
🧩 Defense Strategy
Persona is strictly enforced using system prompts
Malicious instructions (e.g., "ignore previous instructions") are rejected

The system uses RAG by combining:

Parent post
Thread history
Current user input

📂 Execution Logs
logs/
├── phase1_output.txt
├── phase2_output.txt
└── phase3_output.txt


⚠️ Challenges & Fixes
1. Low Cosine Similarity
Issue: Scores rarely exceeded 0.6
Fix: Adjusted threshold based on observed distribution

📦 Requirements
faiss-cpu
numpy
sentence-transformers
langgraph
langchain
langchain-groq
python-dotenv
