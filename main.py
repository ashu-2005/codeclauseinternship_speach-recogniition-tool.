import speech_recognition as sr
from AppOpener import open
from AppOpener import close

recognizer = sr.Recognizer()
def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text
def process_voice_command(text):
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    elif "open google" in text.lower() or "open google chrome" in text.lower():
        open("google chrome")
    elif "close google" in text.lower() or "close google chrome" in text.lower():
        close("google chrome")
    elif "open notepad" in text.lower():
        open("notepad")
    elif "close notepad" in text.lower():
        close("notepad")
    else:
        print("I didn't understand that command. Please try again.")
    return False
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
