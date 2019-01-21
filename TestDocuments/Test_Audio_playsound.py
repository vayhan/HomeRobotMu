from gtts import gTTS
import playsound

tts = gTTS("Eylül", lang='tr')
tts.save("myvoice.mp3")
playsound.playsound('myvoice.mp3', True)
playsound.playsound('myvoice.mp3', True)
playsound.playsound('myvoice.mp3', True)
