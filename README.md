#  Jarvis Virtual Assistant

A Python-based AI voice assistant inspired by Jarvis. It uses speech recognition, text-to-speech, and local LLMs to provide a natural voice-controlled experience and automate everyday tasks.

##  Features

*  Voice command recognition
*  Natural text-to-speech using Edge TTS
*  Local AI responses powered by Ollama
*  Open websites in your browser
*  Get real-time weather information
*  Interactive voice conversations
*  Fast and lightweight Python implementation
*  Easy to extend with new commands and features

##  Technologies Used

* Python
* SpeechRecognition
* Edge TTS
* Pygame
* Ollama
* Requests
* Asyncio

##  Project Structure

```text
Jarvis-Virtual-Assistant/
│── main.py
│── requirements.txt
│── README.md
└── .gitignore
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Jarvis-Virtual-Assistant.git
cd Jarvis-Virtual-Assistant
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull your preferred model, for example:

```bash
ollama pull gemma3:4b
```

or

```bash
ollama pull llama3.2
```

Make sure the Ollama server is running before starting Jarvis.

### 5. Run the project

```bash
python main.py
```

##  Note

Every time Jarvis speaks, an audio (`.mp3`) file is generated automatically for text-to-speech playback. The file is temporary and is removed after playback.

##  What I Learned

Building this project helped me learn:

* Working with Speech Recognition
* Converting text to speech using Edge TTS
* Asynchronous programming with Asyncio
* Integrating local LLMs using Ollama
* Working with REST APIs using Requests
* Audio playback using Pygame
* Python project structure and dependency management

##  Future Improvements

* GUI interface
* Wake word detection
* Home automation support
* Calendar and reminder integration
* Music control
* Email and messaging support
* AI memory and conversation history
* Plugin system for custom commands

##  Contributing

Contributions are welcome!

If you'd like to improve this project by adding new features or fixing bugs, feel free to fork the repository, make your changes, and submit a pull request.

##  Support

If you found this project useful, consider giving it a ** Star** on GitHub. It helps others discover the project and motivates further development.

## 📌 Note

* Every time Jarvis responds using text-to-speech, an **MP3 audio file is automatically generated and saved**.
* The generated audio file is used for playback, making it easy to review or reuse the spoken response if needed.
* If you prefer not to keep these audio files, you can modify the code to delete them automatically after playback.
