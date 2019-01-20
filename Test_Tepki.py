import os
import time
import sqlite3
import winsound
import speech_recognition as sr
import logging
from gtts import gTTS
from tempfile import TemporaryFile
    
def run():
    while True:
        removeFile()
        isForMe = "1"
        filterFirst("1")
        if isForMe == "Kapan":
            exit

# obtain audio from the microphone
def filterFirst(filterMode):
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
    try:
        if filterMode == "1":
            xxx = r.recognize_google(audio, language = "tr-TR")
        elif filterMode == "2":
            xxx = "kanka merhaba"
        var = " "
        xxx = xxx + var
        ccc = xxx.lower()
        if "kanka" not in ccc:
            return
        elif "kanka" in ccc:
            clearedSentence = prepareData(ccc.strip( "kanka" ))
            dataFromDB = getDataFromDB(clearedSentence)
            if dataFromDB is not None:
                #start = time.time()
                tts = gTTS(dataFromDB, lang='tr')
                tts.save("myvoice.mp3")
                #end = time.time()
                #print(end - start)
                winsound.PlaySound ('myvoice.mp3', winsound.SND_FILENAME )
            return dataFromDB
    except sr.UnknownValueError:
        print("Anlamadım")
    except sr.RequestError as e:
        print("Anamerkezden cevap alınamıyor; {0}".format(e))
        
def prepareData( strippedSentence ):    
    #Gelen kırpılmış kelimelerin ilk ve son karakteri boşluk ise sil
    #İlk Karakter
    if ( strippedSentence[0] == " " ):
        strippedSentence = strippedSentence[1:]
    #Son Karakter
    gkcKS = len(strippedSentence) - 1
    if ( strippedSentence[gkcKS] == " " ):
        strippedSentence = strippedSentence[:gkcKS]
    return ( strippedSentence )

def getDataFromDB(clearedSentence):
    conn = sqlite3.connect('MuDB.db')
    c = conn.cursor()
    t = (clearedSentence,)
    c.execute('Select * from Komut where komutADI=? order by random() limit 1', t)
    for row in c:
        print ( str(row[1]) )
        print ( str(row[1]) )
        t = (row[2],)        
    c.execute('Select * from Cevap where cevapID=?', t)
    for row in c:
        return row[1]
    conn.close()

def removeFile():
    if os.path.exists("myvoice.mp3"):
        try:
            os.remove("myvoice.mp3")
        except OSError as e:
            print ("Error: %s - %s." % (e.filename,e.strerror))            
    else:
        print("The file does not exist")
        
if __name__ == "__main__":
    run()
