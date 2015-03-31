#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Übungsblatt_4_Denise.py
# Copyright 2015 Alexander Blesius <onkel-pflaume@web.de>, Denise Schmidt <denise.schmidt@lehramt.uni-giessen.de>
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

# imports
import nltk, re
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.tree import Tree
from collections import defaultdict
from tabulate import tabulate
# from urllib import request

# methods
def getMaxKeyValue(dictionary):
    """returns a tuple (key, int) consisting of the key with the greatest number of values in the dictionary"""
    maxlen = 0
    maxkey = ""
    for k in dictionary.keys():
        if len(dictionary[k]) > maxlen:
            maxlen = len(dictionary[k])
            maxkey = k
    return maxlen, maxkey

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

# Übung 34: There are 264 distinct words in the Brown Corpus having exactly three possible tags.
    # 1. Print a table with the integers 1..10 in one column,
            # and the number of distinct words in the corpus having
            # 1..10 distinct tags in the other column.
brown_tagged_dict = defaultdict(list)
for (word, tag) in brown.tagged_words(tagset='universal'):
    word = word.lower()
    if brown_tagged_dict[word] == []:
        brown_tagged_dict[word] = [tag]
        continue
    n = 0
    for t in brown_tagged_dict[word]:
        if t == tag:
            break
        n += 1
        if len(brown_tagged_dict[word]) == n:
            brown_tagged_dict[word].append(tag)
            break

# number of distinct tags a word can have
num_tags = [n for n in set(len(tags) for tags in brown_tagged_dict.values())]

#number of words with distinct tags
num_words = [0]*len(num_tags)
for l in num_tags:
    #i = 0
    for (word, tag) in brown_tagged_dict.items():
        #if len(tag) == num_tags[i]:
        if len(tag) == l:
            num_words[l-1] += 1
    #num_words[i] = len([word for (word, tag) in brown_tagged_dict if len(tag) == num_tags[i]])
            #i += 1
num_result = [([None],[None])]*len(num_tags)
for i in range(0,len(num_tags)):
    num_result[i] = (num_tags[i], num_words[i])

print(tabulate(num_result, headers=["# tags", "# words w/ dist. tags"]))

    # 2. For the word with the greatest number of distinct tags,
        # print out sentences from the corpus containing the word,
        # one for each possible tag. (15 Punkte)

# function to move a whole tagged sentence into a list
sentences = []
sent_tmp = []
for (word, tag) in brown.tagged_words(tagset='universal'):
    sent_tmp.append([(word, tag)])
    if word == '.':
        sentences.append(sent_tmp)
        sent_tmp = []

# print example sentences for the word with the greatest number of distinct tags
query = getMaxKeyValue(brown_tagged_dict)[1]
for tag in brown_tagged_dict[query]:
    for sent in sentences:
        if [(query, tag)] in sent:
            print(tag, ": ", sent)
            break

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

sent1 = ['old', 'men', 'and', 'women']

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
tree_final = nltk.Tree('S', [tree1, tree4])

print(tree_final)

tree_final.draw()

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

longest_sent = max([len(s) for s in text_sum])  # len(s): length of a string (single sentence)

sent4 = [s for s in text_sum if len(s) == longest_sent]

print(sent4)

# Output: 'His dwelling was so solitary and vault-like,—an old, retired part of an ancient endowment for students,
# once a brave edifice, planted in an open place, but now the obsolete whim of forgotten architects;
# smoke-age-and-weather-darkened, squeezed on every side by the overgrowing of the great city, and choked,
# like an old well, with stones and bricks; its small quadrangles, lying down in very pits formed by the streets
# and buildings, which, in course of time, had been constructed above its heavy chimney stalks;
# its old trees, insulted by the neighbouring smoke, which deigned to droop so low when it was very feeble
# and the weather very moody; its grass-plots, struggling with the mildewed earth to be grass,
# or to win any show of compromise; its silent pavements, unaccustomed to the tread of feet,
# and even to the observation of eyes, except when a stray face looked down from the upper world,
# wondering what nook it was; its sun-dial in a little bricked-up corner,
# where no sun had straggled for a hundred years, but where, in compensation for the sun’s neglect,
# the snow would lie for weeks when it lay nowhere else, and the black east wind would spin like a huge humming-top,
# when in all other places it was silent and still.']


# Dieser Satz besteht aus einer komplexen Aneinanderreihung und Verschachtelung
# von Haupt- und Nebensätzen. Zum Teil kommt es auch zu aufzählungsähnlichen
# Abfolgen.
# Die Teilsätze an sich weisen keine besonders prägnanten oder ungewöhnlichen
# Strukturen auf.