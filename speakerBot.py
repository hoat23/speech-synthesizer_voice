#coding:utf-8
# pip install pyttsx3
# pip install pypiwin32

import os
import sys
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume',1.0)
engine.setProperty('rate',230)
engine.setProperty('voice','spanish')

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def readFileTXT(nameFileTXT):
    fullText = open(nameFileTXT)
    speak("Leyendo archivo ["+nameFileTXT+"]")
    for linea in fullText.readlines():
        linea = linea[:-1]
        speak(linea)


speak("hola mundo, probando sintetizador de voz")
readFileTXT("text2read.txt")
