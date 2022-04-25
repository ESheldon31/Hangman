
import random
import time

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.gapped_word = []
        for letter in range(len(self.word)):
            self.gapped_word.append("_")
        self.num_letters = len(set(self.word)) 
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
        print(f'You have {self.num_lives} lives.')
        print(f'{self.gapped_word}')

    def check_letter(self, letter):
        letter = str.lower(letter)
        if letter in self.word:
            self.num_letters -= 1
            self.list_letters.append(letter)
            idx = self.word.index(letter)
            del self.gapped_word[idx]
            self.gapped_word.insert(idx, letter)
            try: 
                count = idx
                for i in range(len(self.word)):
                    idx = self.word.index(letter, count)
                    del self.gapped_word[idx]
                    self.gapped_word.insert(idx, letter)
                    count += 1
            except:
                pass
            print(f'Nice! {str.upper(letter)} is in the word!')
            time.sleep(1)
            print(f'{self.gapped_word}')
        else: 
            self.num_lives -= 1
            self.list_letters.append(letter)
            print(f'Sorry, {letter} is not in the word.')
            time.sleep(1)
            print(f'{self.diagram[self.num_lives]}')
            time.sleep(1)
            if self.num_lives == 1:
                print(f'You now have {self.num_lives} life left.')
            elif self.num_lives == 0:
                pass
            else:
                print(f'You now have {self.num_lives} lives left.')
            time.sleep(1)
        pass

    def ask_letter(self):
        while True: 
            letter = input('Guess a letter: ')
            if len(letter) > 1:
                print('Please enter just one character.')
            elif len(letter) == 1 and letter in self.list_letters:
                print(f'{str.upper(letter)} was already tried. Try another.')
            elif len(letter) == 1 and letter not in self.list_letters:
                print('Ok, let\'s see.')
                time.sleep(1)
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
    word_list = ['python', 'vscode', 'function', 'method', 'github', 'class']
    play_game(word_list)
# %%
