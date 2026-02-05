import speech_recognition as SR
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import warnings
from wikipedia.exceptions import DisambiguationError



warnings.filterwarnings("ignore")                                       # Ignore any warning messages


listener = SR.Recognizer() 
textToSpeechEngine = pyttsx3.init()           

ALEXA_VOICE = textToSpeechEngine.getProperty('voices')[1].id
textToSpeechEngine.setProperty('voice', ALEXA_VOICE)      
textToSpeechEngine.setProperty('rate', 150)                              # Control Speaking Speed 


def talk(text):
    textToSpeechEngine.say(text)
    textToSpeechEngine.runAndWait()

def alexa_command():
    command = ""
    
    try:
        with SR.Microphone() as source:                             # Use the default microphone as audio source
            print("Listening...")
            voice = listener.listen(source)                         # Listen for the first phrase and extract it into audio data
            command = listener.recognize_google(voice)              # Recognize speech using Google Web Speech API
            command = command.lower()                      
            
            if "alexa" in command:                                  # Check if the wake word "alexa" is in the command
                command = command.replace("alexa", "").strip()      # Remove the wake word from the command
                print(command)
                
    except SR.UnknownValueError:
        print("Could not understand audio")
            
    except SR.RequestError as e:
        print(f"API error: {e}")
        
    except Exception as e:
        print("Error:", e)

    return command



def run_alexa():
    command = alexa_command()
    
    if command == "":
        return "I didn't hear anything. Please try again."
    
    elif "hello" in command or "hi" in command:
        talk("Hello! I am Alexa, your personal assistant.")
        return "Hello! I am Alexa,How can I assist you today?"
    
    elif "how are you" in command:
        talk("I am fine, thank you. How can I help you today?")
        return "I am fine, thank you. How can I help you today?"
    
    elif "what can you do" in command or "features" in command:
        capabilities = ("I can play music, tell you the time and date, provide weather updates, serach information on wikipedia and tell you jokes.")
        talk(capabilities)
        return capabilities
    
    elif "thank you" in command or "thanks" in command:
        talk("You are welcome!")
        return "You are welcome!"
        
    elif "time" in command:
        getTime = datetime.datetime.now().strftime("%I:%M %p")  
        print(getTime)
        talk("Current time is" + getTime)
        return f"Current time is {getTime}"
    
    elif "date" in command:
        getDate = datetime.datetime.now().strftime("%d %B %Y")
        print(getDate)
        talk("Today's date is " + getDate)
        return f"Today's date is {getDate}"
    
    elif "weather" in command:
        talk("Checking the weather for you...")
        pywhatkit.search(command)
        return "Here is the weather information"
    
    # Play the song on YouTube 
    elif "play" in command:
        song = command.replace("play", "")                           # remove word "play" from the command   
        talk("Playing music.." + song)  
        pywhatkit.playonyt(song)                                       
        return f"Playing {song} on YouTube"
    
    
    # Search command on wikipedia    
    elif "who is" in command or "what is" in command:                  
        try:
            topic = command.replace("who is", "").replace("what is", "").strip()    
            
            if topic == "":
                print("Please say the topic name")
                talk("Please say the topic name")
                return "Please say the topic name"
            
            infoFromWikipedia = wikipedia.summary(topic, sentences=2)            
            print(infoFromWikipedia)
            talk(infoFromWikipedia)
            return infoFromWikipedia
        
        except DisambiguationError:
            errorMsg = "There are multiple results. Please be more specific."
            talk(errorMsg)
            return errorMsg
        
        except:
            errorMsg ="Sorry, I could not find any information on that topic."
            talk(errorMsg)
            return errorMsg
    
    # Get a random joke    
    elif "joke" in command:
        getJoke = pyjokes.get_joke()                                 
        print(getJoke)
        talk(getJoke) 
        return getJoke
    
    elif "stop" in command or "exit" in command:             
        talk("Okay, goodbye")
        return "Assistant stopped"
       
    # Default response if command is not recognized
    elif command != "":
        msg = "Sorry, I did not understand. Please say that again"
        talk(msg)
        return msg
    
    
    return "No command recognized"

        
run_alexa()
        
