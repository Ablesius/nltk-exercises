#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Übungsblatt_4.py
#  Copyright 2015 Alexander Blesius <onkel-pflaume@web.de>
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
#
#
import nltk

# Übung 3
# Tokenize and tag the following sentence:
# They wind back the clock, while we chase after the wind.
# What different pronunciations and parts of speech are involved?
tokens = nltk.wordpunct_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(tokens)

# Übung 34
# There are 264 distinct words in the Brown Corpus having exactly three possible tags.
	# 1. Print a table with the integers 1..10 in one column,
	# and the number of distinct words in the corpus having
	# 1..10 distinct tags in the other column.
from nltk.corpus import brown

	# 2. For the word with the greatest number of distinct tags,
	# print out sentences from the corpus containing the word,
	# one for each possible tag. (15 Punkte)

# Übung 5
	# 1. Write code to produce two trees, one for each reading
	# of the phrase "old men and women"

	# 2. Encode any of the trees presented in this chapter
	# as a labeled bracketing and use nltk.Tree() to check
	# that it is well-formed. Now use draw() to display the tree.
from nltk.tree import Tree

	# 3. As in (a) above, draw a tree for
	# "The woman saw a man last Thursday". (7 Punkte)

# Übung 25
# Download several electronic books from Project Gutenberg.
	# Write a program to scan these texts for any extremely long sentences.

	# What is the longest sentence you can find?

	# What syntactic construction(s) are responsible
	# for such long sentences? (10 Punkte)
