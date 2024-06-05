from random import shuffle, choice

sentence = "This is digital media"
sentence = sentence.replace("digital", "analog")
words = sentence.split(" ")
words.sort()

print(sentence)
print(words)

words.sort(key=len)
#sort by word length
words.reverse()
#reverse words

some_word = choice(words)
#choose random word

last_word = words[-1]

#Ideas:
#Make haikus out of a mechanical manual? No, that would require counting syllables
#Could I just count the number of vowels in a sentence? Sure, that would work for some words
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
    
