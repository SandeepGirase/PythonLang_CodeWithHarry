import win32com


def speak(str):
    form win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__='__main__';
    speak("You are the best my friend");