import os 
import win32com.client as wincom

speak = wincom.Dispatch("sapi.SpVoice")

if __name__== '__main__':
    while True:
        print("Welcome to Robo Speaker ")
        
        x=input("Enter what you want me to Pronounce : ")
        if x == "Quit":
            break
        speak.Speak(x)