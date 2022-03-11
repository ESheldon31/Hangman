
import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = []
        for letter in range(len(self.word)):
            self.word_guessed.append("_")
        self.num_letters = len(set(list(self.word))) #typecasting to list first is not necessary. set() works on any iterable.
        self.num_lives = num_lives
        self.list_letters = []
        self.diagram = [
'''
    ____
    |   |
    |   O
    |  \|/
    |  / \ 
    |____
 ''', '''
    ____
    |   |
    |   O
    |  \|/
    |
    |____
 ''', '''
    ____
    |   |
    |   O
    |   |
    |
    |____
 ''', '''
    ____
    |   |
    |   O
    |   
    |
    |____
 ''', 
 '''
    ____
    |   |
    |
    |
    |
    |____
 ''']
        
        print(f'The mystery word has {self.num_letters} unique characters.')
        print(f'{self.word_guessed}')
        pass

    def check_letter(self, letter):
        letter = str.lower(letter)
        if letter in self.word:
            self.num_letters -= 1
            self.list_letters.append(letter)
            idx = self.word.index(letter)
            del self.word_guessed[idx]
            self.word_guessed.insert(idx, letter)
            try: 
                count = idx
                for i in range(len(self.word)):
                    idx = self.word.index(letter, count)
                    del self.word_guessed[idx]
                    self.word_guessed.insert(idx, letter)
                    count += 1
            except:
                pass
            print(f'Nice! {str.upper(letter)} is in the word!')
            print(self.word_guessed)
        else: 
            self.num_lives -= 1
            self.list_letters.append(letter)
            print(f'Sorry, {letter} is not in the word.')
            print(f'{self.diagram[self.num_lives]}')
            print(f'You now have {self.num_lives} lives left.')

        pass

    def ask_letter(self):
        while True: 
            letter = input('Guess a letter: ')
            if len(letter) > 1:
                print('Please, enter just one character.')
            elif len(letter) == 1 and letter in self.list_letters:
                print(f'{str.upper(letter)} was already tried. Try another.')
            elif len(letter) == 1 and letter not in self.list_letters:
                print('Ok, let\'s see.')
                break 
            else: 
                print('Please guess a letter.') 
        self.check_letter(letter)
        pass

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was {game.word}.')
            break
        elif game.num_letters > 0:
            game.ask_letter()
        else: 
            print('Congratulations! You won!')
            break
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
