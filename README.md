# Smartbridge GenAI Chatbot Demo

This project demonstrates a dual-chatbot interface for Smartbridge:
- **Dialogflow Messenger Bot** (cloud-based, embedded via widget)
- **RAG (Retrieval-Augmented Generation) Chatbot** (local, powered by OpenAI and LangChain)

Inspired by the [Smartbridge_GenAI_candidate_assignment](#) documentation.

---

## Features
- **Dialogflow Bot**: Interact with a Dialogflow agent directly in the browser.
- **RAG Chatbot**: Ask questions about Salesforce AI using a local Python backend that leverages transcript data and OpenAI LLMs.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=sk-...
```

### 4. Run the Flask Backend
```bash
python rag_chatbot_api.py
```

- The backend will serve the HTML demo at [http://localhost:5000/](http://localhost:5000/)
- The `/chat` endpoint powers the RAG chatbot responses.

### 5. Open the Demo
Visit [http://localhost:5000/](http://localhost:5000/) in your browser.

---

## File Structure
- `smartbridge_chatbot_demo.html` — Main demo page (served by Flask)
- `rag_chatbot_api.py` — Flask backend exposing the RAG chatbot
- `requirements.txt` — Python dependencies
- `smartbridge_salesforce_ai_transcript.txt` — Knowledge base for RAG chatbot
- `faiss_index/` — Vector index for fast retrieval (auto-generated)

---

## Dialogflow Messenger
- The Dialogflow bot is embedded using the provided widget and agent ID.
- No backend setup is required for Dialogflow; it works out-of-the-box in the HTML.

---

## RAG Chatbot (Local)
- Powered by LangChain, OpenAI, and FAISS vector search.
- Answers are generated based on the transcript in `smartbridge_salesforce_ai_transcript.txt`.
- Requires a valid OpenAI API key.

---

## Deployment Notes
- For production, consider deploying the Flask app on a cloud platform (Heroku, Azure, AWS, etc.).
- Ensure your OpenAI API key is securely managed.
- The Dialogflow widget will work anywhere with internet access.

---

## References
- [Smartbridge_GenAI_candidate_assignment](#) *(replace with actual link if available)*
- [Dialogflow Messenger Documentation](https://cloud.google.com/dialogflow/es/docs/integrations/dialogflow-messenger)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/api-reference/introduction)

---

## License
This project is for educational/demo purposes as part of the Smartbridge GenAI candidate assignment. 