import speech_recognition as sr
import pyttsx3

def main():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Got it! Now to recognize it...")

    text = None
    # Convert the audio to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if text is None:
        return
    # Respond to the user
    if text.startsWith("Hello"):
        engine.say("Hello, how can I help you?")
    elif text == "What is the weather today?":
        engine.say("The weather today is sunny with a high of 75 degrees and a low of 60 degrees.")
    else:
        engine.say("I'm sorry, I didn't understand that.")

    engine.runAndWait()

if __name__ == "__main__":
    main()