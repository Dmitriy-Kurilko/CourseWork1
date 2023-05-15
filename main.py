from random import *


def morse_encode(word):
    res = ''
    for i in word:
        for j in diction:
            if i == j:
                res += diction[j]
    return res


def get_word(list_with_words_for_encode):
    while True:
        res = choice(list_with_words_for_encode)
        if res not in dont_repeat_words:
            dont_repeat_words.append(res)
            return res


def print_statistics(list_with_answers):
    print(f'\nВсего задачек: {len(list_with_answers)}')
    print(f'Отвечено верно: {list_with_answers.count(True)}')
    print(f'Отвечено неверно: {list_with_answers.count(False)}')


answers = []
words_for_encode = ['list', 'small', 'language', 'python', 'flask', 'skyeng', 'easy', 'west', 'east', 'north', 'south']
dont_repeat_words = []

diction = {"0": "-----",
          "1": ".----",
          "2": "..---",
          "3": "...--",
          "4": "....-",
          "5": ".....",
          "6": "-....",
          "7": "--...",
          "8": "---..",
          "9": "----.",
          "a": ".-",
          "b": "-...",
          "c": "-.-.",
          "d": "-..",
          "e": ".",
          "f": "..-.",
          "g": "--.",
          "h": "....",
          "i": "..",
          "j": ".---",
          "k": "-.-",
          "l": ".-..",
          "m": "--",
          "n": "-.",
          "o": "---",
          "p": ".--.",
          "q": "--.-",
          "r": ".-.",
          "s": "...",
          "t": "-",
          "u": "..-",
          "v": "...-",
          "w": ".--",
          "x": "-..-",
          "y": "-.--",
          "z": "--..",
          ".": ".-.-.-",
          ",": "--..--",
          "?": "..--..",
          "!": "-.-.--",
          "-": "-....-",
          "/": "-..-.",
          "@": ".--.-.",
          "(": "-.--.",
          ")": "-.--.-"
           }

input('Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем')

try:
    for i in range(int(input(f'Выбери, сколько слов ты хочешь отгадать (от 1 до {len(words_for_encode)}) '))):
        any_word = get_word(words_for_encode)
        print(f'Слово {i+1} - {morse_encode(any_word)}')
        if input() == any_word:
            print(f'Верно, {any_word}!')
            answers.append(True)
        else:
            print(f'Неверно, {any_word}!')
            answers.append(False)

    print_statistics(answers)
    print('\nКонец игры')
except ValueError:
    print('\nТы не хочешь со мной играть(')
