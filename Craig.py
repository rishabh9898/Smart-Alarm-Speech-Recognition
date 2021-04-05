import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
# import mydate

engine = pyttsx3.init('sapi5')
voices=	 engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish():
	hour = 	int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning I am your virtual assistant Alexa")
	elif hour>=12 and hour<18:
		speak("Good Afternoon Sir I am virtual assistant craig")
	else:
		speak("Good evening  I am your virtual assistant Alexa")
			
def take_command():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		audio=r.listen(source)
	try:
		print("Recognizing...")
		text=r.recognize_google(audio,language='en-in')
		print(text)
	except Exception:
		speak("Error...")
		print("Network Connection Error")
		return "none"
	return text

if __name__=="__main__":
	wish()
	query=take_command().lower()

	if "wikipedia" in query:
		speak("searching details wait....")
		query.replace("wikipedia","")
		results=wikipedia.summary(query,sentence=2)
		print(results)
		speak(results)
	elif 'open youtube' in query or "open video online" in query:
		webbrowser.open("www.youtube.com")
		speak("opening youtube")
	elif 'music from pc' in query or "music" in query:
		speak("ok i am going to play music")
		music_dir="./music"
		musics=os.listdir(music_dir)
		os.startfile(os.path.join(music_dir,musics[0]))
	elif 'open the office' in query or "open fmovies online" in query:
		webbrowser.open("https://fmovies.to/film/the-office.1q4p")
		speak("opening the office")
	elif 'open netflix' in query or "netflix" in query:
		webbrowser.open("https://www.netflix.com/browse")
		speak("Opening Netflix")
	elif 'd2l' in query or "open d2l" in query:
		webbrowser.open("https://d2l.ucalgary.ca/d2l/home")
		speak("Opening d2l")
	elif 'open outlook' in query or "open outlook " in query:
		webbrowser.open("https://outlook.office.com/mail/inbox")
		speak("Opening Outlook email")


	# elif 'alarm' in query:
	# 	mydate.alarm(query)
	elif 'good bye' in query:
		speak("good bye")
		exit()
	elif "shutdown" in query:
		speak("shutting down")
		os.system('shutdown -s')
	








