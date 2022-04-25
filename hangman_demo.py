
import random
import time

class Hangman:

    def __init__(self, word_list, num_lives=5):
        '''This magic method, __init__, creates an instance of the class, 
        with the following attributes.'''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.gapped_word = []
        for letter in range(len(self.word)):
            self.gapped_word.append("_")
        self.num_letters_remaining = len(set(self.word)) 
        self.num_lives = num_lives
        self.list_letters_already_tried = []
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
        
        print(f'The mystery word has {self.num_letters_remaining} unique characters.')
        print(f'You have {self.num_lives} lives.')
        print(f'{self.gapped_word}')

    def check_letter(self, letter):
        '''This method checks whether the letter is in the word.'''
        letter = str.lower(letter)
        if letter in self.word:
            self.num_letters_remaining -= 1
            self.list_letters_already_tried.append(letter)
            
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
            self.list_letters_already_tried.append(letter)
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

    def ask_letter(self):
        '''This method asks the user for a letter. To be accepted, it must be: 
        only one character and it can't have been chosen before.'''
        while True: 
            letter = input('Guess a letter: ')
            if len(letter) > 1:
                print('Please enter just one character.')
            elif len(letter) == 1 and letter in self.list_letters_already_tried:
                print(f'{str.upper(letter)} was already tried. Try another.')
            elif len(letter) == 1 and letter not in self.list_letters_already_tried:
                print('Ok, let\'s see.')
                time.sleep(1)
                break 
            else: 
                print('Please guess a letter.') 
        self.check_letter(letter)

def play_game(word_list):
    '''This function creates an instance of the Hangman class 
    and controls the stages of the game.'''
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was {game.word}.')
            break
        elif game.num_letters_remaining > 0:
            game.ask_letter()
        else: 
            print('Congratulations! You won!')
            break

if __name__ == '__main__':
    word_list = ['python', 'vscode', 'function', 'method', 'github', 'class']
    play_game(word_list)
# %%
