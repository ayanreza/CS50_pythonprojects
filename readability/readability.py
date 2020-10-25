from cs50 import get_string
import re
import math



def letter_count(text):
    total_char = 0
    for char in text:
        total_char += 1
    letters = total_char - text.count(" ")
    return letters


def word_count(text):
    words = text.split(" ")
    
    return len(words)
    


def sentence_count(text):
    sentences = text.count(".") + text.count("!") + text.count("?")
    return sentences


def grade(letters, words, sentences):
    
    l = letters / words * 100
    s = sentences / words * 100
    index = math.floor(0.0588 * l - 0.296 * s - 15.8)
    if index < 1:
        index = "Before Grade 1"
        
    elif index >= 16:
       index = "Grade 16+"
   
    else:
        index = f'Grade {index}'

    return index
        
    
    
    
    
    



def main():
    text = get_string("Text:")
    letters = letter_count(text)
    sentences = sentence_count(text)
    words = word_count(text)
    print(grade(letters, words, sentences))
    

if __name__ == "__main__":
    main()
