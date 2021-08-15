# This program greets everyone Happy Independence Day

from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == "__main__":
    speak("Happy Independence Day Technopanti WIth Yash. Happy Independence Day Of India Technopanti WIth Yash. Happy 75th Independence Day of India Technopanti WIth Yash")