import os
import time
import sqlite3
import winsound
import speech_recognition as sr
import logging
from gtts import gTTS
from tempfile import TemporaryFile


class commandText:
    sTT = "1"
    pSTT = "1"
    mainCommand = "1"
    def __init__(self, execMode ):
        self.execMode = execMode    #ModeToReadText
        if self.execMode == "1":
            logging.info( "COMMAND: Real Mode Command Type Selected" )
        elif self.execMode == "2":
            logging.info( "COMMAND: Manuel Command Type Selected" )
        
    def setSTT(self,mText):
        if self.execMode == "1":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.sTT = r.recognize_google(audio, language = "tr-TR")
                logging.info( "COMMAND: STT=" + self.sTT )
                return self.sTT
            except sr.UnknownValueError:
                self.sTT = "anlamadım"
                logging.info( "COMMAND: STT=" + self.sTT )
                return self.sTT
            except sr.RequestError as e:
                self.sTT = ( "Anamerkezden cevap alınamıyor; {0}".format(e) )
                logging.info( "COMMAND: STT=" + self.sTT )
                return self.sTT
        elif self.execMode == "2":
            self.sTT = mText
            logging.info( "COMMAND: STT=" + self.sTT )
            return self.sTT
        
    def setPSTT(self):
        gapText = " "
        self.pSTT = self.sTT + gapText
        self.pSTT = self.pSTT.lower()
        logging.info( "COMMAND: PSTT=" + self.pSTT )
        return ( self.pSTT )
    
    def getMC(self): #Main Command and Director
        self.mC = "kanka"
        logging.info( "COMMAND: MC=" + self.mC )
        return self.mC
    
    def isMC(self): #Main Command and Director
        if self.mC in self.pSTT:
            self.isMCR = True           #Command Related
            self.pSTT = self.pSTT.strip( self.mC )
            logging.info( "COMMAND: MCR=TRUE" )
        elif not self.mC in self.pSTT:
            self.isMCR = False          #Not Command Related
            logging.info( "COMMAND: MCR=FALSE" )
        return self.isMCR
    
    def sPSTT(self):
        strippedSentence = self.pSTT
        #Gelen kırpılmış kelimelerin ilk ve son karakteri boşluk ise sil
        #İlk Karakter
        if ( strippedSentence[0] == " " ):
            strippedSentence = strippedSentence[1:]
        #Son Karakter
        gkcKS = len(strippedSentence) - 1
        if ( strippedSentence[gkcKS] == " " ):
            strippedSentence = strippedSentence[:gkcKS]
        self.sPSTT = strippedSentence
        logging.info( "COMMAND: PSST=" + self.sPSTT )
        return self.sPSTT
        
    #def getDBTOC(self): #Type of Command 1.Q&A 2.Learning 3.Command
        
    def getDBA(self):       #Answer
        conn = sqlite3.connect('MuDB.db')
        c = conn.cursor()
        t = (self.sPSTT,)
        c.execute('Select * from Komut where komutADI=? order by random() limit 1', t)
        for row in c:
            self.comType = row[2]
            logging.info( "COMMAND: DB:comTYPE=" + str(row[2]) )  
            t = ( row[3], )
            logging.info( "COMMAND: DB:KOMUT=" + str(row[1]) )            
            c.execute('Select * from Cevap where cevapID=?', t)
            for row in c:
                self.answer = row[1]
                logging.info( "COMMAND: ANSWER=" + self.answer )
                return self.answer
            return self.comType
        conn.close()
        return self.answer
    def setDBA_LMA(self):
        conn = sqlite3.connect('MuDB.db')
        c = conn.cursor()
        t = (self.sPSTT,)
        c.execute('Select * from Komut where komutADI=? order by random() limit 1', t)
        for row in c:
            self.comType = row[2]
            logging.info( "COMMAND: DB:comTYPE=" + str(row[2]) )  
            t = ( row[3], )
            logging.info( "COMMAND: DB:KOMUT=" + str(row[1]) )            
            c.execute('Select * from Cevap where cevapID=?', t)
            for row in c:
                self.answer = row[1]
                logging.info( "COMMAND: ANSWER=" + self.answer )
                return self.answer
            return self.comType
        conn.close()
        return self.answer

class answerFile:
    def __init__(self):
        name = "answerFile.mp3"      # Name Of File
        self.name = name
        logging.info( "FILE: nOF=" + self.name )

    def removeFile(self):
        logging.info("FILE: Delete File")
        if os.path.exists(self.name):
            try:
                os.remove(str(self.name))
                logging.info("FILE: Deleted Succesfully")
            except OSError as e:
                logging.error ("FILE: Error: %s - %s." % (e.filename,e.strerror))
        else:
            logging.warning("FILE: The file does not exist")
            
    def createFile(self,answer):
        tts = gTTS(answer, lang='tr')
        tts.save(self.name)
        winsound.PlaySound (self.name, winsound.SND_FILENAME )

    def playFile(self):
        winsound.PlaySound (self.name, winsound.SND_FILENAME )
        
        
def run():
    logging.basicConfig(filename='application.log',level=logging.DEBUG)
    logging.warning("START: Application")
    #while True:
    fileAnswer = answerFile()
    fileAnswer.removeFile()
    c1 = commandText("1")   #log:COMMAND
    c1.setSTT("kanka öğrenme modunu aç")
    c1.setPSTT()
    c1.getMC()
    c1.isMC()
    c1.sPSTT()
    if c1.isMCR == True:
        c1.getDBA()
        if ( str(c1.comType) == "1"):   #Question Answer            fileAnswer.createFile(c1.answer)
            fileAnswer.createFile(c1.answer)
            fileAnswer.playFile()
        elif (str(c1.comType) == "2"): #Learning            logging.info("LM: Learning Mode Opened")
            #İlk önce öğreneceği Komut nedir?
            fileLMQuestion = answerFile()
            fileLMQuestion.removeFile()
            learnLMQ = commandText("2")
            learnLMQ.setSTT("Komut")
            learnLMQ.setPSTT()
            learnLMQ.sPSTT()
            fileLMQuestion.playFile()
            fileLMQuestion.removeFile()
            #Sonra önce öğreneceği Komut nedir?
            learnLMA = commandText("2")
            learnLMA.setSTT("Cevap")
            learnLMA.setPSTT()
            learnLMA.sPSTT()
        elif (str(c1.comType) == "3"):
            q = q    
    return 
        
if __name__ == "__main__":
    run()
