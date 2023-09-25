import random
import string

def speak_like_yoda(sentence):
    sentence = sentence.lower()
    for p in string.punctuation.replace("'", ''):
        sentence = sentence.replace(p, '')
    words = sentence.split()
    random.shuffle(words)
    new_sent = ' '.join(words)

    print('\nYour Yodenglish sentence: ')
    print(new_sent.capitalize())

if __name__ == '__main__':
    print('Enter your sentence: ')
    sentence = str(input())
    speak_like_yoda(sentence)