# import modules
import re
import sys

################################################################################

# print program header
print("***** Anagram Finder *****")

################################################################################

# try/except block
try: #find lexicon file
    with open("EnglishWords.txt", "r") as words_file:
        words_file = words_file.read().splitlines() #read all lines of file and split lines at \n
        skip_lines = words_file.index("START") #lines to skip until "START" is found
        words_file = words_file[skip_lines:] #only include lines from "START" to end of file

except FileNotFoundError: #if lexicon file not found, print error message and exit program
    print("Sorry, could not find file 'EnglishWords.txt'.")
    sys.exit(1)

################################################################################
    
# get user input word
input_word = input("Enter a word: ").lower() #ensure input word is in lower case.
print("") #automarker requires newline

################################################################################

# alphabet list
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# initialize empty list of lists to track letter frequencies
freq = [[] for letter in range(len(alphabet))] 

################################################################################

# letter match function
def letter_match(word, alphabet=alphabet, freq=freq):
    """
    function that tracks and matches each letter in the alphabet also found in the word
    parameters: input word, list of letters in the alphabet and empty freq list for each letter in the alphabet
    """

    word = list(word) #convert word to list of letters
    i = 0 #iterable
    
    #nested for loop to find matching letters 
    for letter_alphabet in alphabet:
        for letter_word in word:
            if letter_word == letter_alphabet: #find matching letters
                freq[i].append(letter_alphabet) #track all matching letters
            else:
                pass
        i += 1
    return freq #return list of lists with matching letters

################################################################################

# letter_count function
def letter_count(freq, alphabet=alphabet):
    """
    function that counts frequencies of each letter in the alphabet
    parameters: freq list containing matching letters, and list of letters in the alphabet
    """

    my_freq_dict = {} #initialize empty dictionary to hold letter:frequency
    i = 0 #iterable
    
    # for loop to track counts of letters
    for i in range(len(freq)):
        counts = len(freq[i]) #count occurance of each letter
        my_freq_dict[alphabet[i]] = counts
        i += 1
    return my_freq_dict #retun dictionary of letter:frequency
   
################################################################################

# find frequencies of letters given an input word
letter_match(input_word, alphabet, freq)
input_word_counts = letter_count(freq, alphabet)

################################################################################

# find_anagrams function
def find_anagrams(input_word, input_word_counts, alphabet=alphabet, lexicon=words_file):
    """
    function that counts frequencies of each letter in the lexicon
    parameters are the input word, counts of each letter in the word, alphabet list and lexicon file
    """
    
    anagrams = [] #initialize empty list to attach matched anagrams
    
    #for loop to find anagrams of input word
    for word in words_file:
        word = word.strip() #remove trailing white spaces \n
        freq = [[] for letter in range(len(alphabet))] #initialize empty list of 26*lists for each word in lexicon
        letter_match(word, alphabet, freq) #letter_match function
        counts = letter_count(freq, alphabet) #letter_count function
        
        #a match is found if dictionary of lexicon letter counts = dictionary of input word's letter counts
        if counts == input_word_counts and not(re.match("".join(word), input_word)): #do not include the input word
            anagrams.append(word) #append anagram to anagrams list
        else:
            pass
    
    #sort anagrams list in alphabetical order
    anagrams.sort() 
    
    #return list of anagrams, where freq of letters in input word = freq of letters in lexicon words
    #If anagrams list is empty, return error message
    return anagrams if len(anagrams) > 0 else "Sorry, anagrams of '%s' could not be found." %input_word

################################################################################

# use find_anagrams function to get anagrams of input word
list_anagrams = find_anagrams(input_word, input_word_counts, alphabet, words_file)
print(list_anagrams) #print list of anagrams

################################################################################



    
        
    
    
    
    
    
    
    
    
    

