#! /usr/bin/env python3
from bs4 import BeautifulSoup
import re
import requests

# - Define a string s = 'colorless'. Write a Python statement that changes this to "colourless" using only the slice and concatenation operations.
s = 'colorless'
print(s[:4] + 'u' + s[4:])

# - We can use the slice notation to remove morphological endings on words. For example, 'dogs'[:-1] removes the last character of dogs, leaving dog. Use slice notation to remove the affixes from these words (we've inserted a hyphen to indicate the affix boundary, but omit this from your strings): dish-es, run-ning, nation-ality, un-do, pre-heat.
words = ['dishes', 'running', 'nationality', 'undo', 'preheat']
for word in words:
    if word.endswith('es'):
        print(word[:-len('es')])
    if word.endswith('ing'):
        # nn, ll, etc.
        if word[-5] == word[-4]:
            print(word[:-4])
        else:
            print(word[:-len('ing')])
    if word.endswith('ality'):
        print(word[:-len('ality')])
    if word.startswith('un'):
        print(word[len('un'):])
    if word.startswith('pre'):
        print(word[len('pre'):])

# - We saw how we can generate an IndexError by indexing beyond the end of a string. Is it possible to construct an index that goes too far to the left, before the start of the string?
foo = [1, 2, 3]
print(len(foo))
print("creating an IndexError:")
try:
    print(foo[len(foo)])
except IndexError as e:
    print(e)

print("creating an IndexError by going too far to the left:")
try:
    print(foo[-len(foo) - 1])
except IndexError as e:
    print(e)

# - We can specify a "step" size for the slice. The following returns every second character within the slice: monty[6:11:2]. It also works in the reverse direction: monty[10:5:-2] Try these for yourself, then experiment with different step values.

# - What happens if you ask the interpreter to evaluate monty[::-1]? Explain why this is a reasonable result.

# - Describe the class of strings matched by the following regular expressions.
#     [a-zA-Z]+
#     [A-Z][a-z]*
#     p[aeiou]{,2}t
#     \d+(\.\d+)?
#     ([^aeiou][aeiou][^aeiou])*
#     \w+|[^\w\s]+

# Test your answers using nltk.re_show().


# - Write regular expressions to match the following classes of strings:
#
#         A single determiner (assume that a, an, and the are the only determiners).
def single_determiner(s):
    return re.search(r'\ban?\b|\bthe\b', s)


#         An arithmetic expression using integers, addition, and multiplication, such as 2*3+8.
def arithmetic_expression(s):
    return re.search(r'\d+([+*]\d+)+', s)


# - Write a utility function that takes a URL as its argument, and returns the contents of the URL, with all HTML markup removed. Use from urllib import request and then request.urlopen('http://nltk.org/').read().decode('utf8') to access the contents of the URL.
def url_text(url):
    print("""This function is a bad idea, because it always needs to fetch the text from the URL first. It would be much better to fetch the HTML text once, save it to a variable, then use BeautifulSoup to make it pretty.""")
    raw_html = requests.get(url).text
    return BeautifulSoup(raw_html, 'html.parser').get_text()


# - Save some text into a file corpus.txt. Define a function load(f) that reads from the file named in its sole argument, and returns a string containing the text of the file.
#     Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. Use one multi-line regular expression, with inline comments, using the verbose flag (?x).
#     Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; dates; names of people and organizations.
#
# - Rewrite the following loop as a list comprehension:


# sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# result = []
# for word in sent:
#     word_len = (word, len(word))
#     result.append(word_len)
# [('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]

# - Define a string raw containing a sentence of your own choosing. Now, split raw on some character other than space, such as 's'.

# - Write a for loop to print out the characters of a string, one per line.

# - What is the difference between calling split on a string with no argument or with ' ' as the argument, e.g. sent.split() versus sent.split(' ')? What happens when the string being split contains tab characters, consecutive space characters, or a sequence of tabs and spaces? (In IDLE you will need to use '\t' to enter a tab character.)

# - Create a variable words containing a list of words. Experiment with words.sort() and sorted(words). What is the difference?

# - Explore the difference between strings and integers by typing the following at a Python prompt: "3" * 7 and 3 * 7. Try converting between strings and integers using int("3") and str(3).

# - Use a text editor to create a file called prog.py containing the single line monty = 'Monty Python'. Next, start up a new session with the Python interpreter, and enter the expression monty at the prompt. You will get an error from the interpreter. Now, try the following (note that you have to leave off the .py part of the filename):

# from prog import monty
# print(monty)

# This time, Python should return with a value. You can also try import prog, in which case Python should be able to evaluate the expression prog.monty at the prompt.

# - What happens when the formatting strings %6s and %-6s are used to display strings that are longer than six characters?
#
# + Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur. (wh-words in English are used in questions, relative clauses and exclamations: who, which, what, and so on.) Print them in order. Are any words duplicated in this list, because of the presence of case distinctions or punctuation?
#
# + Create a file consisting of words and (made up) frequencies, where each line consists of a word, the space character, and a positive integer, e.g. fuzzy 53. Read the file into a Python list using open(filename).readlines(). Next, break each line into its two fields using split(), and convert the number into an integer using int(). The result should be a list of the form: [['fuzzy', 53], ...].
#
# + Write code to access a favorite webpage and extract some text from it. For example, access a weather site and extract the forecast top temperature for your town or city today.
#
# + Write a function unknown() that takes a URL as its argument, and returns a list of unknown words that occur on that webpage. In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) and remove any items from this set that occur in the Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings.
#
# + Examine the results of processing the URL http://news.bbc.co.uk/ using the regular expressions suggested above. You will see that there is still a fair amount of non-textual data there, particularly Javascript commands. You may also find that sentence breaks have not been properly preserved. Define further regular expressions that improve the extraction of text from this web page.
#
# + Are you able to write a regular expression to tokenize text in such a way that the word don't is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+».
#
# + Try to write code to convert text into hAck3r, using regular expressions and substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to lowercase before converting it. Add more substitutions of your own. Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.
#
# + Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin
#        Write a function to convert a word to Pig Latin.
#        Write code that converts text, instead of individual words.
#        Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

# + Download some text from a language that has vowel harmony (e.g. Hungarian), extract the vowel sequences of words, and create a vowel bigram table.
#
# + Python's random module includes a function choice() which randomly chooses an item from a sequence, e.g. choice("aehh ") will produce one of four possible characters, with the letter h being twice as frequent as the others. Write a generator expression that produces a sequence of 500 randomly chosen letters drawn from the string "aehh ", and put this expression inside a call to the ''.join() function, to concatenate them into one long string. You should get a result that looks like uncontrolled sneezing or maniacal laughter: he  haha ee  heheeh eha. Use split() and join() again to normalize the whitespace in this string.
#
# + Consider the numeric expressions in the following sentence from the MedLine Corpus: The corresponding free cortisol fractions in these sera were 4.53 +/- 0.15% and 8.16 +/- 0.23%, respectively. Should we say that the numeric expression 4.53 +/- 0.15% is three words? Or should we say that it's a single compound word? Or should we say that it is actually nine words, since it's read "four point five three, plus or minus zero point fifteen percent"? Or should we say that it's not a "real" word at all, since it wouldn't appear in any dictionary? Discuss these different possibilities. Can you think of application domains that motivate at least two of these answers?
#
# + Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. Let us define μw to be the average number of letters per word, and μs to be the average number of words per sentence, in a given text. The Automated Readability Index (ARI) of the text is defined to be: 4.71 μw + 0.5 μs - 21.43. Compute the ARI score for various sections of the Brown Corpus, including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences.
#
# + Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word. Do the same thing with the Lancaster Stemmer and see if you observe any differences.
#
# + Define the variable saying to contain the list ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more',
# 'is', 'said', 'than', 'done', '.']. Process this list using a for loop, and store the length of each word in a new list lengths. Hint: begin by assigning the empty list to lengths, using lengths = []. Then each time through the loop, use append() to add another length value to the list. Now do the same thing using a list comprehension.
#
# + Define a variable silly to contain the string: 'newly formed bland ideas are inexpressible in an infuriating
# way'. (This happens to be the legitimate interpretation that bilingual English-Spanish speakers can assign to Chomsky's famous nonsense phrase, colorless green ideas sleep furiously according to Wikipedia). Now write code to perform the following tasks:
#     Split silly into a list of strings, one per word, using Python's split() operation, and save this to a variable called bland.
#     Extract the second letter of each word in silly and join them into a string, to get 'eoldrnnnna'.
#     Combine the words in bland back into a single string, using join(). Make sure the words in the resulting string are separated with whitespace.
#     Print the words of silly in alphabetical order, one per line.
#
# + The index() function can be used to look up items in sequences. For example, 'inexpressible'.index('e') tells us the index of the first position of the letter e.
#     What happens when you look up a substring, e.g. 'inexpressible'.index('re')?
#     Define a variable words containing a list of words. Now use words.index() to look up the position of an individual word.
#     Define a variable silly as in the exercise above. Use the index() function in combination with list slicing to build a list phrase consisting of all the words up to (but not including) in in silly.
#
# + Write code to convert nationality adjectives like Canadian and Australian to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names).
#
# + Read the LanguageLog post on phrases of the form as best as p can and as best p can, where p is a pronoun. Investigate this phenomenon with the help of a corpus and the findall() method for searching tokenized text described in 3.5. http://itre.cis.upenn.edu/~myl/languagelog/archives/002733.html
#
# + Study the lolcat version of the book of Genesis, accessible as nltk.corpus.genesis.words('lolcat.txt'), and the rules for converting text into lolspeak at http://www.lolcatbible.com/index.php?title=How_to_speak_lolcat. Define regular expressions to convert English words into corresponding lolspeak words.
#
# + Read about the re.sub() function for string substitution using regular expressions, using help(re.sub) and by consulting the further readings for this chapter. Use re.sub in writing code to remove HTML tags from an HTML file, and to normalize whitespace.
#
# * An interesting challenge for tokenization is words that have been split across a line-break. E.g. if long-term is split, then we have the string long-\nterm.
#     Write a regular expression that identifies words that are hyphenated at a line-break. The expression will need to include the \n character.
#     Use re.sub() to remove the \n character from these words.
#     How might you identify words that should not remain hyphenated once the newline is removed, e.g. 'encyclo-\npedia'?x
#
# * Read the Wikipedia entry on Soundex. Implement this algorithm in Python.
#
# * Obtain raw texts from two or more genres and compute their respective reading difficulty scores as in the earlier exercise on reading difficulty. E.g. compare ABC Rural News and ABC Science News (nltk.corpus.abc). Use Punkt to perform sentence segmentation.
#
# * Rewrite the following nested loop as a nested list comprehension:
# words = ['attribution', 'confabulation', 'elocution',
#          'sequoia', 'tenacious', 'unidirectional']
# vsequences = set()
# for word in words:
#     vowels = []
#     for char in word:
#         if char in 'aeiou':
#             vowels.append(char)
#     vsequences.add(''.join(vowels))
# sorted(vsequences)
# ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

# * Use WordNet to create a semantic index for a text collection. Extend the concordance search program in 3.6, indexing each word using the offset of its first synset, e.g. wn.synsets('dog')[0].offset (and optionally the offset of some of its ancestors in the hypernym hierarchy).
#
# * With the help of a multilingual corpus such as the Universal Declaration of Human Rights Corpus (nltk.corpus.udhr), and NLTK's frequency distribution and rank correlation functionality (nltk.FreqDist, nltk.spearman_correlation), develop a system that guesses the language of a previously unseen text. For simplicity, work with a single character encoding and just a few languages.
#
# * Write a program that processes a text and discovers cases where a word has been used with a novel sense. For each word, compute the WordNet similarity between all synsets of the word and all synsets of the words in its context. (Note that this is a crude approach; doing it well is a difficult, open research problem.)
#
# * Read the article on normalization of non-standard words (Sproat et al, 2001), and implement a similar system for text normalization.
