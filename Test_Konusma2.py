import speech_recognition as sr
import vlc
from gtts import gTTS
from tempfile import TemporaryFile

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)
# recognize speech using Google Speech Recognition
try:
	print("Google Speech Recognition thinks you said in Turkish: -  " + r.recognize_google(audio, language = "tr-TR"))
	ccc = text=r.recognize_google(audio, language = "tr-TR")
	tts = gTTS(ccc, lang='tr')
	tts.save("myvoice.mp3")
	p = vlc.MediaPlayer('myvoice.mp3')
	p.play()
	p.stop()
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
