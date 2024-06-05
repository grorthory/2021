#Make haikus out of a mechanical manual
#Count number of nonconsecutive vowels in sentence
#Replace numbers with their word counterparts.
#Remove capitalization and punctuation
#Three-letter or fewer words count as one syllable unless they start with a vowel
#Two vowels in a row should count as one vowel.
#Divide the text into a list (sentences) of lists (words).

#Count 5 syllables from the start of a sentence.
#If it ends on a word, count 7 syllables from there or until the sentence ends.
#If the sentence ends, remember the number of syllables remaining.
#Move on to the next sentence and count the remaining syllables.
#Then do the same for 5 syllables

#To find number of syllables in a word:
#If the word has 3 or less characters, it has 1 syllable.
#Iterate through the word. If a vowel is found, check if the next letter is a vowel.
#If it does, skip that vowel.
#The number of syllables in the word is the number of nonconsecutive vowels.
import random
from helpers import load_text, get_sentences, get_words, get_good_words, get_unique, get_verbs

vowels = ["a", "e", "i", "o", "u", "y"]
vowels_plus_sd = ["a", "e", "i", "o", "u", "y", "s", "d"]
one_syllable_numbers = "one, two, three, four, five, six, eight, nine"
validcharacters = "abcdefghijklmnopqqrstuvwxyz. 0123456789"

source = open("manual.txt").read()
manual = ""
source = source.lower()
source = source.replace("\n", " ")
source = source.replace("fig.", "fig")
for i in range(len(source)):
    if source[i] in validcharacters:
        manual += source[i]
manual = manual.replace("0", "zero ")
manual = manual.replace("1", "one ")
manual = manual.replace("2", "two ")
manual = manual.replace("3", "three ")
manual = manual.replace("4", "four ")
manual = manual.replace("5", "five ")
manual = manual.replace("6", "six ")
manual = manual.replace("7", "seven ")
manual =manual.replace("8", "eight ")
manual = manual.replace("9", "nine ")
manual_sentences = get_sentences(manual)
manual_words = []
for i in range(len(manual_sentences)):
    manual_words.append(get_words(manual_sentences[i]))
#print(manual_words)

def count_syllables(word):
    syllables = 0
    if len(word) <= 3 or word in one_syllable_numbers:
        syllables = 1
    else:
        for i in range(len(word)):
            if word[i] in vowels and word[i-1] not in vowels:
                syllables = syllables + 1
    if 7 >= len(word) > 3 and word not in one_syllable_numbers and word[-1] in vowels_plus_sd and syllables > 1:
        syllables = syllables - 1

    #print(word + " has " + str(syllables) + " syllable(s).")
    return(syllables)

def sentence_syllables(sentence):
    syllables = 0
    for i in range(len(sentence)):
        syllables += count_syllables(sentence[i])
    #print("sentence syllables: " + str(syllables))
    return syllables

def make_haiku(sentence_index):
    haiku = [[], [], []]
    haiku_lengths = [5, 7, 5]
    sentence0 = sentence_syllables(manual_words[sentence_index])
    i = 0
    for j in range(3):
        while sentence_syllables(haiku[j]) < haiku_lengths[j]:
            current_sentence = manual_words[sentence_index]
            if i < len(current_sentence) and count_syllables(current_sentence[i]) <= haiku_lengths[j] - sentence_syllables(haiku[j]):
                haiku[j].append(current_sentence[i])
                i = i+1
            else:
                #print("moving to next sentence...")
                sentence_index = sentence_index + 1
    for k in range(3):
        print(haiku)[k]
    print("")
for i in range(10):
    make_haiku(random.randint(1, len(manual_words)))
