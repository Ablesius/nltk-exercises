# Übungsblatt_4.py
#
# Alexander Blesius & Denise Schmidt
#
#
#
# Aufgabe 3

import nltk,re,pprint

from nltk import word_tokenize

text = word_tokenize("They wind back the clock, while we chase after the wind.")

nltk.pos_tag(text)

# Output: [('They', 'PRP'), ('wind', 'VBP'), ('back', 'RB'), ('the', 'DT'),
# ('clock', 'NN'), (',', ','), ('while', 'IN'), ('we', 'PRP'), ('chase', 'VBP'),
# ('after', 'IN'), ('the', 'DT'), ('wind', 'NN'), ('.', '.')]
# Bei "wind" kommt es zu Unterschieden bei der Wortart und der Aussprache.
# "wind" wird zunächst als Verb benutzt (die Uhr zurückdrehen) und dann als Nomen (der Wind).
# Bei wind/Verb wird das i als ei ausgesprochen.
# Bei wind/Nomen wird das i als i ausgesprochen.

#Aufgabe 34



#Aufgabe 5
grammar = nltk.CFG.fromstring("""
	PHRASE -> AdjP | NP CON NP
	NP -> Adj N | N
	AdjP -> N CON N
	Adj -> 'old'
	N -> 'men' | 'women'
	CON -> 'and'
""")

sent = [("old", ("men"), ("and"), ("women")]

# Lesart 1: old men and old women (das Adjektiv wird auf beide Nomen bezogen und
# dominiert die Nomen = steht im Baum oben).
# Lesart 2: die Phrase besteht aus zwei "unabhängigen Nomen", nämlich alten Männern
# und Frauen aller Altersstufen.

#Aufgabe 25
