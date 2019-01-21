import os
import sys
import time
import sqlite3
import speech_recognition as sr
import logging
from gtts import gTTS
from tempfile import TemporaryFile


class commandText:
    sTT = "1"
    pSTT = "1"
    mainCommand = "1"
    def __init__(self, execMode, dirMode, dirText):
        self.execMode = execMode    #ModeToReadText
        self.dirMode = dirMode
        if dirMode == "1":
            self.setSTT("")
            self.setPSTT()
            self.getMC()
            self.isMC()
            self.sPSTT()
        elif dirMode == "2":
            self.setSTT(dirText)
            self.setPSTT()
            self.sPSTT()
            
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
    def setDBA_LMQA(self,lmQuestion,lmAnswer):
        conn = sqlite3.connect('MuDB.db')
        c = conn.cursor()
        t = (lmAnswer,)
        try:
            c.execute('INSERT INTO Cevap (cevapADI) VALUES (?)', t)
        except sqlite3.IntegrityError as e:
            print('sqlite error: ', e.args[0]) # column name is not unique
        k = (lmQuestion,'1',c.lastrowid,)
        try:
            c.execute('INSERT INTO Komut (komutADI,komutTuruID,cevapID) VALUES (?,?,?)', k)
        except sqlite3.IntegrityError as e:
            print('sqlite error: ', e.args[0]) # column name is not unique
        conn.commit()
        conn.close()

class answerFile:
    def __init__(self,answer):
        name = "answerFile.mp3"      # Name Of File
        self.name = name
        logging.info( "FILE: nOF=" + self.name )
        self.createFile(answer)
        self.playFile()
        self.removeFile()
        
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
        if os.path.exists(self.name):
            try:
                os.system("TASKKILL /F /IM wmplayer.exe")
            except OSError as e:
                logging.error ("FILE: Error: %s - %s." % (e.filename,e.strerror))
                       
    def createFile(self,answer):
        tts = gTTS(answer, lang='tr')
        tts.save(self.name)

    def playFile(self):
        os.startfile("answerFile.mp3")
        time.sleep(3) 
def run():
    execMode = "1"
    logging.basicConfig(filename='application.log',level=logging.DEBUG)
    logging.warning("START: Application")
    while True:
        c1 = commandText(execMode,"1","kanka öğrenme modunu aç")
        if c1.isMCR == True:
            c1.getDBA()
            if ( str(c1.comType) == "1"):   #Question Answer
                fileAnswer = answerFile(c1.answer)
            elif (str(c1.comType) == "2"): #Learning
                logging.info("LM: Learning Mode Opened")
                fileAnswer = answerFile(c1.answer)
                #İlk önce öğreneceği Komut nedir?
                fileLMQuestion = answerFile("Komut Nedir?")
                learnLMQ = commandText(execMode,"2","SoruVolkan")
                #Sonra önce öğreneceği Komut nedir?
                fileLMAnswer = answerFile("Cevap Nedir?")
                learnLMA = commandText(execMode,"2","CevapAyhan")
                learnLMA.setDBA_LMQA(learnLMQ.sPSTT,learnLMA.sPSTT)
                volkan = "CevapTest"
                while True:
                    fileLMAnswer = answerFile("Başka cevap var mı?")
                    learnLMA = commandText(execMode,"2",volkan)
                    if volkan == "bitti":
                        return False
                    else:
                        learnLMA.setDBA_LMQA(learnLMQ.sPSTT,learnLMA.sPSTT)
                        volkan = "bitti"
            elif (str(c1.comType) == "3"):
                fileAnswer = answerFile(c1.answer)
        
        
if __name__ == "__main__":
    run()
