import speech_recognition as sr
import asyncio
import edge_tts
import pygame
import os
import time
import uuid
import webbrowser
import ollama
import requests
import random

# -----------------------------
# Async TTS function
# -----------------------------
async def speak_async(text, voice="en-US-GuyNeural", rate="-15%"):
    filename = f"{uuid.uuid4()}.mp3"  # unique temp file
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(filename)

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                print("Cleanup error:", e)

shutdown_phrases = [
    "System shutting down. Goodbye, Sir.",
    "Jarvis going offline. Until next time.",
    "Powering down. All systems disengaged.",
    "Shutdown sequence initiated. Have a good day.",
    "Jarvis offline. Standing by for reactivation.",
    "System terminated. Awaiting next startup."
]

def speak(text, voice="en-US-GuyNeural"):
    asyncio.run(speak_async(text, voice))

# -----------------------------
# Chat with Gemma
# -----------------------------
chat_history = [
    {'role': 'system', 'content': 'You are Jarvis, a helpful AI assistant. Suhail is using you as a local LLM.'}
]

def ask_gemma(prompt, recognizer):
    chat_history.append({'role': 'user', 'content': prompt})
    response = ollama.chat(model='gemma2:2b', messages=chat_history)
    output = response['message']['content']
    chat_history.append({'role': 'assistant', 'content': output})
    print(output)
    speak(output)

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            speak("Still online, ask something")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

        cmd = recognizer.recognize_google(audio)
        print("Heard:", cmd)

        if "shutdown" in cmd.lower() or "poweroff" in cmd.lower():
            stdwn_phrase=random.choice(shutdown_phrases)
            speak(stdwn_phrase)
            break

        handled = processcomd(cmd)
        if not handled:
            ask_gemma(cmd, recognizer)

# -----------------------------
# News fetch
# -----------------------------
def get_news(topic="technology"):
    GNEWS_API_KEY = "Your api key"
    url = f"https://gnews.io/api/v4/search?q={topic}&token={GNEWS_API_KEY}&lang=en"
    response = requests.get(url)
    data = response.json()

    if "articles" in data:
        headlines = [article["title"] for article in data["articles"][:3]]
        return "Here are the latest headlines: " + "; ".join(headlines)
    return "No news found."

# -----------------------------
# Command handler
# -----------------------------
def processcomd(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://in.linkedin.com")
        return True
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return True
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
        return True
    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
        return True
    elif "news" in c:
        headlines = get_news("technology")
        speak(headlines)
        return True
    else:
        return False

# -----------------------------
# Main loop
# -----------------------------
if __name__ == "__main__":
    speak("Jarvis activated. All systems operational.")
    time.sleep(1)

    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)

            word = r.recognize_google(audio)
            print("Recognized:", word)

            if "jarvis" in word.lower():
                speak("Online and ready. What would you like me to do?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Jarvis active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    print("Command:", command)

                    handled = processcomd(command)
                    if not handled:
                        ask_gemma(command, r)

        except Exception as e:
            print("Error:", e)
            # speak("Say clearly")
