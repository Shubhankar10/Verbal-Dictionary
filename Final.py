#from PyDictionary import PyDictionary
from gtts import gTTS
from wordhoard import Definitions
from wordhoard import Synonyms
from wordhoard import Antonyms

from translate import Translator

import wikipedia
import os


#dict = PyDictionary()

print("Press:")
print("1 to Search on Wiki")
print("2 to Find Meaning of a Word")
print("3 to Translate a Word")
print("4 to Find Antonym of a Word")
print("5 to Find Synonym of a Word")
ch=int(input("\nChoice:"))

#Ask the user for word to perform the task
word=input("Enter Word: ")

if ch==1:
    #TO perform a search on WIKIPEDIA
    #wikiS =wikipedia.search(word, results = 5)
    wiki=wikipedia.summary(word, sentences=3)
    print(wiki)
    final=wiki
    
elif ch==2:
    # TO retrun Meaning of a word 
    definition = Definitions(word)
    meaning = definition.find_definitions()
    final="Meanings for "+word+" are: "
    print(final)
    for i in meaning:
        print("*",i)
        final=final+i

elif ch==3:
    #TO Translate a word in hindi
    translator= Translator(to_lang="Hindi")
    translation = translator.translate(word)
    final="Translation of "+word+" in Hindi is:  "+translation
    print(final)

elif ch==4:
    #TO retrun Antonym of the word
    #count variable is used to store only the first 5 antonym in the audio file
    count=0
    
    antonym = Antonyms(word)
    antonym_results = antonym.find_antonyms()
    final="Antonyms for "+word+" are: "
    print(final)
    
    for i in antonym_results:
        print(i)
        if(count<4):
            final=final+i
            count+=1
        
elif ch==5:
    #TO return Synonym of the word
    #count variable is used to store only the first 5 synonyms in the audio file
    count=0
    
    synonym = Synonyms(word)
    synonym_results = synonym.find_synonyms()
    final="Synonym for "+word+" are: "
    print(final)
    
    for i in synonym_results:
        print(i)
        if(count<4):
            final=final+i
            count+=1
#final contains the final output form any of the called funtions for the audio output.

#TO Speak
        
speak=str(final)
myobj = gTTS(text=speak, slow=False)

myobj.save("audio.mp3")

os.system("audio.mp3")



































