CodeGuru — Local AI Coding Assistant

A local AI-powered coding assistant built with Python, Gradio, and Ollama. CodeGuru runs completely through a locally hosted Ollama model and provides an interactive web interface for asking programming questions, generating code, and receiving responses in real time through streaming.

**🚀 Features**

Local LLM inference using Ollama
Code generation for Python and other programming languages
Gradio web interface for an interactive user experience
Streaming responses displayed progressively as the model generates them
No external LLM API required
Simple REST API integration with Ollama
Markdown-formatted responses for readable code blocks
Error handling for Ollama connection and request failures
Lightweight and easy to run locally

**🏗️ Architecture**
                     ┌─────────────────────┐
                     │      User           │
                     │  Coding Question    │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    Gradio UI        │
                     │  localhost:7860     │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     Python App      │
                     │      app.py         │
                     └──────────┬──────────┘
                                │
                         HTTP POST Request
                                │
                                ▼
                     ┌─────────────────────┐
                     │     Ollama API      │
                     │ localhost:11434     │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   CodeGuru Model    │
                     │      Local LLM      │
                     └──────────┬──────────┘
                                │
                         Streaming Tokens
                                │
                                ▼
                     ┌─────────────────────┐
                     │    Gradio UI        │
                     │ Generated Response  │
                     └─────────────────────┘
**🛠️ Technologies Used**
Technology	Purpose
Python	Application development
Ollama	Local LLM runtime
CodeGuru	Local coding model
Gradio	Web-based user interface
Requests	HTTP communication with Ollama
Git	Version control
GitHub	Source-code hosting

**📁 Project Structure**
CodeGuru-Ollama-Gradio/
│
├── app.py
├── modelfile
├── requirements.txt
├── .gitignore
└── README.md
app.py

Main Python application responsible for:

Creating the Gradio interface
Receiving user prompts
Sending requests to Ollama
Streaming model responses
Displaying generated responses
Handling connection and API errors
modelfile

Ollama model configuration used to create the local codeguru model.
requirements.txt

Contains the Python dependencies required by the application.
.gitignore

Prevents unnecessary and sensitive files such as virtual environments, Python cache files, and environment variables from being committed.

**⚙️ Prerequisites**

Before running the project, install:
Python 3.10+
Ollama
Git

Verify Python:
python --version
Verify Ollama:
ollama --version

**🦙 Ollama Setup**
The application expects an Ollama model named:
codeguru

Verify that the model exists:
ollama list

You should see:

NAME
codeguru
If the model does not exist, create it using the provided modelfile.

From the project directory:
ollama create codeguru -f modelfile

Then verify:
ollama list

Test the model directly:
ollama run codeguru

Try:
Write a Python function for binary search.
If the model responds correctly, the Ollama setup is ready.

🐍 Python Environment Setup

Clone the repository:
git clone https://github.com/Anipireddy-Pavan/CodeGuru-Ollama-Gradio.git

Navigate into the project:
cd CodeGuru-Ollama-Gradio

Create a virtual environment:
Windows
python -m venv .venv

Activate it:
.venv\Scripts\Activate.ps1

For Windows Command Prompt:
.venv\Scripts\activate

📦 Install Dependencies
Install the required Python packages:
pip install -r requirements.txt

The main dependencies are:
requests
gradio
▶️ Run the Application

Make sure Ollama is running.

If necessary:
ollama serve
Then open another terminal and activate the virtual environment:
cd CodeGuru-Ollama-Gradio
.venv\Scripts\Activate.ps1

Run the application:

python app.py

You should see:

Running on local URL: http://127.0.0.1:7860
Open the URL in your browser:

http://127.0.0.1:7860
💡 Example Prompts

CodeGuru can be used for questions such as:

Python
Write a Python function for binary search.
Data Structures
Explain the difference between a stack and a queue with Python examples.
SQL
Write a SQL query to find the second highest salary.
Machine Learning
Explain random forest and provide a Python implementation.
Debugging
Why does this Python code produce an IndexError?
Algorithms
Implement merge sort in Python and explain its time complexity.
⚡ Streaming Responses

CodeGuru uses Ollama's streaming API:

"stream": True
The Python application receives the generated response incrementally instead of waiting for the entire response.
The process is:

User Prompt
     ↓
Python
     ↓
Ollama API
     ↓
LLM generates tokens
     ↓
Python receives tokens
     ↓
Gradio updates UI

This provides a better user experience because the response begins appearing while the model is still generating.

🔌 Ollama API

The application communicates with Ollama through:
http://localhost:11434/api/generate

Example request:

data = {
    "model": "codeguru",
    "prompt": prompt,
    "stream": True
}

The application processes Ollama's streamed JSON responses and progressively updates the Gradio interface.

🔒 Privacy

One of the main benefits of this project is that inference is performed locally.

User
 ↓
Local Gradio Application
 ↓
Local Python Application
 ↓
Local Ollama Server
 ↓
Local LLM

No external LLM API key is required for the basic application.
This makes the project useful for experimenting with local AI applications and private coding workflows.

🧪 Error Handling

The application handles common failures including:
Ollama is not running
Could not connect to Ollama.

Start Ollama:
ollama serve
Model does not exist

Check:
ollama list
Create the model:
ollama create codeguru -f modelfile
Request timeout
The application has a request timeout to prevent indefinitely waiting for an unavailable Ollama response.

🔧 Configuration
The Ollama endpoint and model are configured in app.py:

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codeguru"

To use another Ollama model, change:
MODEL_NAME = "codeguru"
to the name of an installed local model.

For example:
MODEL_NAME = "your-model-name"
📊 Performance Considerations

Response generation speed depends on:

LLM size
CPU/GPU hardware
Available RAM/VRAM
Model quantization
Prompt length
Number of generated tokens

Smaller local models generally provide faster responses, while larger models can provide better reasoning and code-generation capabilities at the cost of higher resource usage.

You can inspect installed models using:

ollama list
🔐 GitHub Security

This repository intentionally excludes:

.venv/
.env
.env.*
__pycache__/
*.pyc

Do not commit:

API keys
Passwords
Access tokens
Private credentials
Local environment files containing secrets

The .gitignore file is included to help prevent accidental commits.

🚀 Improvements

Potential enhancements include:

 Conversation memory
 Chat-based Gradio interface
 Code syntax highlighting
 Code execution sandbox
 Multiple Ollama model selection
 File upload and code analysis
 Automatic code debugging
 GitHub repository analysis
 RAG-based documentation search
 Multi-agent coding workflow
 Model performance monitoring
 Docker deployment
 Unit-test generation
 Code quality analysis
 Authentication for shared deployments
🎯 Learning Outcomes

This project demonstrates practical experience with:

Local Large Language Models
Ollama
LLM inference
REST API integration
Streaming LLM responses
Python application development
Gradio UI development
Prompt engineering
Error handling
Virtual environments
Git and GitHub
Local AI application architecture

📌 Project Status
Status: Active Development
Application: Local AI Coding Assistant
Model Runtime: Ollama
Interface: Gradio
Inference: Local

👨‍💻 Author
Anipireddy Pavan Kumar
Computer Science & Engineering | Data Science | AI/ML | Generative AI
GitHub: Anipireddy-Pavan
