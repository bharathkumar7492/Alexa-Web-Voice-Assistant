# Alexa-Web-Voice-Assistant

#🎙️ Alexa Web Voice Assistant (Python + Flask)

A web-based voice assistant built using Python and Flask that listens to user commands and responds with speech in real time. The assistant can play songs, fetch information from Wikipedia, tell jokes, and provide time/date updates through voice interaction.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#🚀 Features

🎧 Voice command recognition using SpeechRecognition

🔊 Text-to-speech response using pyttsx3

🌐 Web interface built with Flask, HTML, CSS, JavaScript

▶️ Play songs directly on YouTube

📚 Fetch information from Wikipedia

😂 Generate random jokes

🕒 Provide real-time date & time

🛡️ Exception handling for unclear audio & API errors


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#🛠️ Tech Stack

Backend - 

Python
Flask


Voice Processing - 

SpeechRecognition (Google Web Speech API)
pyttsx3


Frontend - 

HTML
CSS
JavaScript (Speech Synthesis)


Libraries Used - 
pywhatkit
wikipedia
pyjokes
datetime


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#⚙️ How It Works


1. User clicks the Listen button on the webpage

2. Flask triggers the Python backend

3. Microphone captures voice input

4. SpeechRecognition converts speech → text

5. Assistant processes the command

6. pyttsx3 converts response → speech

7. Result is displayed + spoken on screen



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#💻 Installation & Setup


1️⃣ Clone the Repository
git clone https://github.com/your-username/alexa-web-voice-assistant.git
cd alexa-web-voice-assistant

2️⃣ Install Dependencies
pip install flask SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes

3️⃣ Run the Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#🧠 Supported Voice Commands


Try saying:

“Alexa play song name”

“Alexa what is Python”

“Alexa tell me a joke”

“Alexa time”

“Alexa date”

“Alexa how are you”

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#✖️ Error Handling

The system handles:

Unclear voice input

API request failures

Wikipedia ambiguity errors

Empty command detection

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#👨‍💻 Author

BharathKumar Ravi

Software Development engineer (Fresher)

GitHub: https://github.com/bharathkumar7492
