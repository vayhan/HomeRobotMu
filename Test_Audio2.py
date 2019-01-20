from gtts import gTTS
import winsound

tts = gTTS("Eylül", lang='tr')
tts.save("myvoice.mp3")
winsound.PlaySound ('myvoice.mp3', winsound.SND_FILENAME )
