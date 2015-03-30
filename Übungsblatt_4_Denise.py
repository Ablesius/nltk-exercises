#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Übungsblatt_4_Denise.py
#  Copyright 2015 Alexander Blesius <onkel-pflaume@web.de>, Denise Schmidt <denise.schmidt@lehramt.uni-giessen.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# TODO:
    # find out why longest sentence differs from Denise's version

import nltk, re
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.tree import Tree
# from urllib import request
from collections import defaultdict

# Übung 3
    # Tokenize and tag the following sentence:
        # They wind back the clock, while we chase after the wind.
    # What different pronunciations and parts of speech are involved?
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
# Tipp Karlova: defaultdict (S. 194-198, Kapitel 5, ab „Incrementally Updating a Dictionary“).
    # There are 264 distinct words in the Brown Corpus having exactly three possible tags.
        # 1. Print a table with the integers 1..10 in one column,
            # and the number of distinct words in the corpus having
            # 1..10 distinct tags in the other column.
brown_tagged = brown.tagged_words(tagset='universal')   # lower all words!
dict = defaultdict(list)
for (word, tag) in brown_tagged:
    word = word.lower()
    if dict[word] == []:
        dict[word] = [tag]
        continue
    n = 0
    for t in dict[word]:
        if t == tag:
            break
        n += 1
        if len(dict[word]) == n:
            dict[word].append(tag)
            break


        # 2. For the word with the greatest number of distinct tags,
            # print out sentences from the corpus containing the word,
            # one for each possible tag. (15 Punkte)


# Übung 5
    # 1. Write code to produce two trees, one for each reading
        # of the phrase "old men and women"
grammar1 = nltk.CFG.fromstring("""
    PHRASE -> AdjP | NP CON NP
    NP -> Adj N | N
    AdjP -> Adj Obj
    Obj -> N CON N
    Adj -> 'old'
    N -> 'men' | 'women'
    CON -> 'and'
""")

sent1 = [("old"), ("men"), ("and"), ("women")]

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(sent1):
    print(tree)

# Lesart 1: old men and old women (das Adjektiv wird auf beide Nomen bezogen und
    # dominiert die Nomen = steht im Baum oben).
# Lesart 2: die Phrase besteht aus zwei "unabhängigen Nomen", nämlich alten Männern
    # und Frauen aller Altersstufen.

    # 5.2
        # Encode any of the trees presented in this chapter
        # as a labeled bracketing and use nltk.Tree() to check
        # that it is well-formed. Now use draw() to display the tree.
tree1 = nltk.Tree('NP', ['Mary'])
tree2 = nltk.Tree('NP', ['Bob'])
tree3 = nltk.Tree('V', ['saw'])
tree4 = nltk.Tree('VP', [tree3, tree2])
tree5 = nltk.Tree('S', [tree1, tree4])
print(tree5)
tree5.draw()

# ODER
sent3 = Tree('S', [Tree('NP', ['Mary']), Tree('VP', [Tree('V', ['saw']), Tree('NP', ['Bob'])])])
print(sent3)
sent3.draw()

    # 5.3
grammar2 = nltk.CFG.fromstring("""
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

sent2 = "The woman saw a man last Thursday".split()

rd_parser = nltk.RecursiveDescentParser(grammar2)

for tree in rd_parser.parse(sent2):
    print(tree)

# Lesart 1: Sie sah ihn zuletzt Dienstag.
# Lesart 2: Sie sah ihn letzten Dienstag.
# Lesart mit saw = sägen: überprüft, aber da Vergangenheit vorliegt, keine
    # Lesart möglich, weil saw im Präsens (Vergangenheit sawed) keinen Sinn ergibt

#Aufgabe 25
    # Tipp Karlova:
        # Finden Sie zuerst den längsten Satz in den von Ihnen ausgewählten Texten (3-5).
        # Versuchen Sie diesen Satz zu parsen (optional).

# urllist = ["http://www.gutenberg.org/ebooks/1659.txt.utf-8", "http://www.gutenberg.org/ebooks/48371.txt.utf-8", "http://www.gutenberg.org/ebooks/3102.txt.utf-8"]
# textlist = []
# text1 = ""
# text2 = ""
# text3 = ""
# for each in [text1, text2, text3]:
    # each = request.urlopen(urllist[x]).read().decode('utf8')
# for x in range(0, 3):
    # textlist.append(request.urlopen(urllist[x]).read().decode('utf8'))

gutenb1 = open('CountryDoctor_deBalzac.txt')
text1 = gutenb1.read()

gutenb2 = open('ChangedHeart_Fleming.txt')
text2 = gutenb2.read()

gutenb3 = open('HauntedMan_Dickens.txt')
text3 = gutenb3.read()

# texts_all = textlist[0] + textlist[1] + textlist[2]

texts_all = text1 + text2 + text3
texts_cleaned = re.sub(r'\n', ' ', texts_all)

text_sum = nltk.sent_tokenize(texts_cleaned)

longest_len = max([len(s) for s in text_sum])   # len(s): length of a string (single sentence)
sent4 = [s for s in text_sum if len(s) == longest_len]
print(sent4)

# Output: 'Ever to look beyond the present moment, to foresee the ways of
#Destiny, to care so little for power that he only retains it because he is
#conscious of his usefulness, while he does not overestimate his strength;
#ever to lay aside all personal feeling and low ambitions, so that he may always
#be master of his faculties, and foresee, will, and act without ceasing; to
#compel himself to be just and impartial, to keep order on a large scale, to
#silence his heart that he may be guided by his intellect alone, to be neither
#apprehensive nor sanguine, neither suspicious nor confiding, neither grateful
#nor ungrateful, never to be unprepared for an event, nor taken unawares by an
#idea; to live, in fact, with the requirements of the masses ever in his mind,
#to spread the protecting wings of his thought above them, to sway them by the
#thunder of his voice and the keenness of his glance; seeing all the while not
#the details of affairs, but the great issues at stake--is not that to be
#something more than a mere man?'

# Dieser Satz besteht aus einer komplexen Aneinanderreihung und Verschachtelung
# von Haupt- und Nebensätzen. Zum Teil kommt es auch zu aufzählungsähnlichen
# Abfolgen, zum Beispiel in "to be neither apprehensive nor sanguine, neither
# suspicious nor confiding, neither grateful nor ungrateful, never to be
# unprepared for an event, nor taken unawares by an idea".
# Die Teilsätze an sich weisen keine besonders prägnanten oder ungewöhnlichen
# Strukturen auf.
