import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
 
    elif hour>=12 and hour<18:
        speak("Good After Noon Sir")   
 
    else:
        speak("Good evening Sir")  
 
    speak(" How Can I help you")       
 
def takeCommand():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
 
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("boppanajayakrishna2003@gmail.com","boppana@2003")
    server.sendmail("boppanajayakrishna2003@gmail.com", to, content)
    server.close()


 
if __name__ == "__main__":
    while True:
        if 1:
            speak("Identify Yourself")
            id = takeCommand().lower()
        if 'jay' in id:
            speak("pin")
            p=takeCommand().lower()
            if(p=="0250"):
                wishMe()
                query =takeCommand().lower()
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
 
                elif 'open google' in query:
                    webbrowser.open("google.com")
 
                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                elif 'open telescope' in query:
                    webbrowser.open("ngitonline.com")
                elif 'play music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
 
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
 
                elif ' your program' in query:
                    codePath = r"C:\Users\B Jaya krishna\Documents\asst.py"
                    os.startfile(codePath)
 
                elif 'email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "adead0250@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry. I am not able to send this email")

                elif 'love' in query:
                    speak("luv u tooo "+"jayaa")
                elif 'hell' in query:
                    speak('hi sir')
                elif 'python' in query:
                    codePath = r"C:\Users\B Jaya krishna\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit).lnk"
                    os.startfile(codePath)
                elif 'shutdown' in query:
                    os.system("shutdown /s /t 10")
                    speak ("shutting down the computer")
                    break
            
                elif 'good evening' in query:
                    speak("you seem to be happy today")
                elif 'search' in query:
                    from googlesearch import *
                    import webbrowser
                    chrome_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
                    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                        webbrowser.open("https://google.com/search?q=%s" % query)
                        speak("your search result")
                elif 'your name' in query:
                    speak("my name is Radha, jaya's system assistance")
                elif 'thank' in query:
                    speak("my pleasure sir")
                    break
                else:
                    speak("i didn't get you,come again")
            else:
                speak("Wrong Password")
            
 
        
        
        
        
        
