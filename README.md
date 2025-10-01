# 🤖 AI-Powered To-Do List

An intelligent task management application that automatically categorizes your tasks using Natural Language Processing (NLP). Built with FastAPI backend and React frontend.

---

## 🎯 How It Works

### **The Magic Behind Task Categorization:**

1. **You type a task** - "Buy milk and bread"
2. **AI analyzes the text** - Uses spaCy NLP to understand keywords
3. **Smart categorization** - Automatically assigns categories like "Shopping", "Work", "Health", etc.
4. **Beautiful display** - Shows your task with a colored category badge

### **Task Categories:**
- 🛒 **Shopping**: buy, purchase, order, milk, grocery, shop
- 💼 **Work**: email, report, meeting, project, deadline  
- ❤️ **Health**: exercise, run, gym, doctor, medicine
- 👤 **Personal**: call, visit, family, friend, birthday
- 📝 **Other**: Default for unmatched tasks

---

## 🏗️ Architecture

### **Backend (FastAPI)**
- **Python 3.11+** with FastAPI framework
- **spaCy NLP** for intelligent text analysis
- **REST API** with multiple endpoints
- **CORS enabled** for frontend communication

### **Frontend (React)**
- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS** + **shadcn/ui** for beautiful UI
- **Real-time API integration**

---

## 🚀 Quick Start

### **Prerequisites:**
- Python 3.11+ (for backend)
- Node.js 18+ (for frontend)

### **Local Development:**

1. **Start the Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
python main.py
```

2. **Start the Frontend:**
```bash
cd frontend
npm install
cp env.example .env
# Edit .env: VITE_API_URL=http://localhost:8000
npm run dev
```

3. **Access the Application:**
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

---

## 🔧 Environment Variables

### **Frontend (.env file):**
```bash
VITE_API_URL=http://localhost:8000
```

### **Backend:**
- **PORT**: Automatically set by the server

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API information |
| `GET` | `/health` | Health check |
| `POST` | `/tag-task` | Categorize single task |
| `POST` | `/tag-tasks` | Categorize multiple tasks |
| `GET` | `/categories` | Get available categories |
| `GET` | `/demo` | Demo with example tasks |
| `GET` | `/docs` | Interactive API documentation |

### **Example API Usage:**

**Categorize a single task:**
```bash
curl -X POST "http://localhost:8000/tag-task" \
     -H "Content-Type: application/json" \
     -d '{"task": "Buy milk and bread"}'
```

**Response:**
```json
{
  "task": "Buy milk and bread",
  "category": "Shopping"
}
```

---

## 📁 Project Structure

```
ai-powered-todo-list/
├── backend/                 # FastAPI Backend
│   ├── main.py             # Main application
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Backend docs
├── frontend/                # React Frontend
│   ├── src/                # Source code
│   │   ├── components/     # UI components
│   │   ├── pages/          # Page components
│   │   └── hooks/          # Custom hooks
│   ├── package.json        # Node dependencies
│   ├── vite.config.ts      # Vite configuration
│   └── README.md           # Frontend docs
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 🎨 Features

### **Backend Features:**
- ✅ Intelligent task categorization using spaCy NLP
- ✅ RESTful API with FastAPI
- ✅ Multiple endpoints for single/batch processing
- ✅ Interactive API documentation (Swagger UI)
- ✅ CORS support for frontend integration
- ✅ Health check endpoints

### **Frontend Features:**
- ✅ Modern React with TypeScript
- ✅ Beautiful UI with Tailwind CSS and shadcn/ui
- ✅ Real-time task categorization
- ✅ Responsive design for all devices
- ✅ Toast notifications for user feedback
- ✅ Wave background with glass morphism effects
- ✅ Category badges with icons and colors

---

## 🔮 Future Enhancements

- [ ] Task editing and deletion
- [ ] User authentication and task persistence
- [ ] Multiple category support per task
- [ ] ML-based classifier for smarter tagging
- [ ] Task due dates and priority levels
- [ ] Dark/light theme toggle
- [ ] Offline support with PWA
- [ ] Multi-language support

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🚀 Live Demo

**Frontend:** [To-Do-List Link](https://ai-todo-frontend.onrender.com)

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing Python web framework
- [spaCy](https://spacy.io/) for the powerful NLP library
- [React](https://reactjs.org/) for the frontend framework
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [shadcn/ui](https://ui.shadcn.com/) for the beautiful UI components
- [Vite](https://vitejs.dev/) for the fast build tool
