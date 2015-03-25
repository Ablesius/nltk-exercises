#Sarah Knapp, Matrikelnummer: 3114787

import nltk
import re
import pprint
from nltk import ContextFreeGrammar


#Aufgabe 3:
text = "They wind back the clock, while we chase after the wind"
print nltk.word_tokenize(text)
print "\n"
print nltk.pos_tag(nltk.word_tokenize(text))
# Das Wort "wind" wird einmal als Nomen (NN) und einmal als Verb (VBP) erkannt.
""" Die Wortarten in dem Satz sind: Personalpronomen, Verb, Adverb, Artikel, Nomen
 und Präposition"""
print "\n"

#Aufgabe 34:
from nltk.corpus import brown



#Aufgabe 5:
#Teil 1
grammar1 = nltk.ContextFreeGrammar.fromstring("""
PHRASE -> AdjP | NP CON NP
NP -> Adj N | N 
AdjP -> Adj Obj
Obj -> N CON N
Adj -> 'old'
N -> 'men' | 'women'
CON -> 'and'
""")

sent = [("old"), ("men"), ("and"), ("women")]

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(sent):
	print(tree)
#Teil 2
#Satz (S (NP Mary) (VP (V saw) (NP Bob)))

tree1 = nltk.Tree('NP', ['Mary'])

tree2 = nltk.Tree('NP', ['Bob'])

tree3 = nltk.Tree('V', ['saw'])

tree4 = nltk.Tree('VP', [tree3, tree2])

tree5 = nltk.Tree('S', [tree1, tree4])

print(tree5)

tree5.draw()

#Teil 3
grammar2 = nltk.ContextFreeGrammar.fromstring("""
S -> NP VP | NP VP Time
NP -> Det N
VP -> V NP VTemp | V NP TemP
TemP -> VTemp Day
Time -> Day
Det -> 'The' | 'a'
N -> 'man' | 'woman'
V -> 'saw'
VTemp -> 'last'
Day -> 'Thursday'
""")

sent = "The woman saw a man last Thursday".split()

rd_parser = nltk.RecursiveDescentParser(grammar2)

for tree in rd_parser.parse(sent):
	print(tree)
	
#Aufgabe 25:
from nltk.corpus import gutenberg
print gutenberg.fileids()
from nltk import word_tokenize

#Drei Texte wurden von der Seite "Gutenberg Project" heruntergeladen und im Python-Verzeichnis abgespeichert.

gutenb1 = open('CountryDoctor_deBalzac.txt')    #Die einzelnen Texte werden in Python geöffnet und unter der read-Funktion abgespeichert
text1 = gutenb1.read()

gutenb2 = open('ChangedHeart_Fleming.txt')
text2 = gutenb2.read()

gutenb3 = open('HauntedMan_Dickens.txt')
text3 = gutenb3.read()

textegesamt = text1 + text2 + text3     #Die Texte werden durch Summation in einem Text zusammengefasst

textegesamtneu = re.sub(r'\n', ' ', textegesamt)    

gesamt = nltk.sent_tokenize(textegesamtneu)

longest_len = max([len(s) for s in gesamt])
sent = [s for s in gesamt if len(s) == longest_len]
print (sent)
#komplexe Aneinanderreihungen und Verschachtelungen
