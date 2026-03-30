# Lumina - AI Chat Interface
A lightweight, customizable chat interface

## ✨ Features

- LLM Chatting
    - Local - chat with local models via ollama local clients 
    - Cloud - chat with cloud models via ollama.com + api key
- Theme customization

- Upcoming!!
    - File reading 
    - OCR/visual tools (only available depending on model)
    - RAG functionality
    - Web searching

## 🚀 Installation

```bash
# Clone this repo
git clone <this-repo>
cd lumina-webui

# Automatically prepares dependencies on first run
python launcher.py install
```

If you want to use local ollama models, you must have a computer capable of handling it and the ollama local server

Linux: 
```bash
sudo <package-manager install> ollama
# Ubuntu
sudo apt install ollama

# Arch
sudo pacman -S ollama

# Then install your preferred model (check on the [ollama page](https://ollama.com))
ollama serve
ollama pull <your-model-here>
```


## 🎯 Usage

Running via python (Easier multiplatform support)

```bash
python launcher.py run
```

Via bash (Unix-based OS)

```bash
sh lumina.sh
```

Via bat or terminal (Windows)

- Double click lumina.bat or create a shortcut

## ⚙️ Configuration


Edit settings in the UI panel:

- Model selection (local/cloud)

- API key management (!!!IMPORTANT FOR CLOUD!!!)

- Theme customization

- Local mode toggle
