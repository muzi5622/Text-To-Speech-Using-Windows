import pyttsx3
import time

about = """
_____________________Text-To-Speech_____________________
--------------------------------------------------------
---> Programmer : Muzamil 
---> Version : 1.1
---> Develop Date : 27-August-2023

_____________________Details____________________________
--------------------------------------------------------
Text-To-Speech, uses power of Python for making life 
easier for Users. You can use this program for your 
projects and many more.

_____________________Features___________________________
--------------------------------------------------------
1- Easy to use
2- Fast and convenient
3- Take less Memory (maximum 20 mb)
4- no internet required
5- free of cost
6- 2-10 Average Load Time*
7- Use Less Storage (maximum 50 mb)

*Depends on your PC 
_____________________Compatability______________________
--------------------------------------------------------
Required : Python3
Required : pyttsx3 Mode 

"""
how_to_use = """
_____________________How-To-Use_________________________
--------------------------------------------------------
1- first of all you have to make a text file
   (example.txt) file.
2- Now, paste or write your text, and save your file
3- after starting this program select option 1.
4- Then enter the number of voice which are available 
   in your pc.
5- Now type or paste your text file location.
---> For Example:
    My file is in C Directory
    Then location of my file is 
    
    --->C:\\file.txt
    --->E:\\folder\\file.txt
6- Boom! Your PC is speaking
"""

feedback = """
_____________________FeedBack___________________________
--------------------------------------------------------
if you found any problem or any error, please feelfree to
contact us. we will wait for your reviews and feedback so
we will improve this program and remove that bugs and 
error.

---> Name: Muzamil
---> Github: @muzi5622
"""
def main():

    engine = pyttsx3.init()
    print("\n")
    voices = engine.getProperty('voices')
    for index,voice in enumerate(voices, start=0):
        print(f"{index}- Voice :", voice.name)

    while True:
        try:
            select_voice = int(input("\nEnter the Available Voice Number: "))
            break
        except:
            print("Invalid Input!")

    try:
        voice_rate = input("Enter the Rate of Word Per Minute: ")
    except:
        return select_voice

    return select_voice, voice_rate

def say(select_voice,voice_rate=140):
    text = """ """  
    try:
        voice_rate = int(voice_rate)
    except:
        print("The Default voice rate is 140")

    engine = pyttsx3.init()
    engine.connect('started-utterance', onStart)
    engine.connect('finished-utterance', onEnd)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[select_voice].id)
    engine.setProperty('rate', voice_rate)
    while True:
        try:
            print("\nEnter The .txt File Location (E:\\folder\\text.txt): ")
            loc = input("---> ")
            
            with open(f"{loc}", "r") as f:
                text1 = f.read()
                text += text1
            break
        except:
            print('\nInvalid Input! or Invalid Location or Invalid .txt File')

    print("Starting...")
    time.sleep(0.4)
    print("Starting..")
    time.sleep(0.3)
    print("Runing..")
    time.sleep(0.2)
    
    engine.say(text)
    engine.runAndWait()
    time.sleep(2)
    print("Done...")
    
def credit():
    print("__________________Text-To-Speech__________________________")
    print(" ©.Muzi5622------------------------------------By-Muzamil")
def onStart(name):
    print('\n---Speech started---')
    
def onEnd(name, completed):
    print('---Speech completed---\n')

while True:
    credit()
    print("\nOptions:\n1- Text-To-Speech\n2- How to use\n3- About\n4- Feedback\n5- Exit ")
    opt = int(input("---> "))
    if opt == 1:
        credit()
        select_voice,voice_rate = main()
        say(select_voice,voice_rate)
    elif opt == 2:
        print(how_to_use.title())
        time.sleep(2)
    elif opt == 3:
        print(about.title())
        time.sleep(2)
    elif opt == 4:
        print(feedback.title())
        time.sleep(2)
    elif(opt == 5):
        print("__________________Thanks-For-Using__________________________\n ___________________Text-To-Speech_________________________")
        print("  ©.Muzi5622--------------------------------By-Muzamil")
        time.sleep(2)
        break
    else:
        print("Invalid Option!")
    credit()
