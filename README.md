# Hangman
A game of hangman to practise basic python syntax

**Description**

To start, the program chooses a word at random from the word list, and then displays the number of unique characters and the gapped word. E.g. 

		The mystery word has 9 characters.
		['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']

The user is asked for a letter and the program checks if it is in the word. If it is, its position is displayed in the gapped word and the game continues. If it is not, the player loses a life, and the next stage of the hangman diagram is drawn. 

This continues until the player either guesses the word, and therefore wins, or runs out of lives, in which case, they lose. 

This project makes use of Object Oriented Programming. A Hangman class is defined with the following attributes and methods:

	•	attributes:
	  ⁃	word: str. The word to be guessed picked randomly from the word_list.
	  ⁃	word_guessed: list. A list of the letters of the word, with '_' for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', ‘_’]. If the player guesses 'a', the list would be ['a', '_', '_', '_', ‘_’].
	  ⁃	num_letters: int. The number of unique letters in the word that have not been guessed yet.
      ⁃	num_lives: int. The number of lives the player has.
      ⁃	list_letters: list. A list of the letters that have already been tried.
      ⁃	diagram: list. A list containing the stages of the hangman diagram.
	•	methods:
  	  ⁃	check_letter(letter). This checks if the letter is in the word.
  	  ⁃	ask_letter(). This asks the user for a letter, and checks that it is valid, i.e. is only one character and has not been used before.

In the play_game() function, the class is called to create an instance of the game, which the user then interacts with.

**Progress**

Milestone 1: 
This stage involved coding the ask_letter() method. Using a while loop, it asks the user for a letter, assigning it to the variable, letter. With an if-elif-else statement, it then checks that the letter meets the criteria of being a single character. If it does, the while loop breaks. If it doesn’t, the user is asked again for a single character.

<img width="565" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/91407498/157905997-f05d46d5-d767-4771-8574-a35dbe3d8c43.png">

Milestone 2:
Here, using the __init__ constructor, I initialised the attributes as described above. I also included 2 print statements to appear when the game starts, i.e. when an instance of the class is initialised. 

<img width="520" alt="Pasted Graphic 9" src="https://user-images.githubusercontent.com/91407498/157906157-eb9aa0a2-0ee3-4b3f-aca3-88d7274c5200.png">

Now that I had the list_letter attribute, I could amend the ask_letter() method so that it also checks that the letter hasn’t been asked previously.

<img width="480" alt="Pasted Graphic 3" src="https://user-images.githubusercontent.com/91407498/157906221-1113b9bf-f62f-44be-9b6f-ecc54667f8b5.png">

Milestone 3: 
Here, I was coding the check_letter() method. This method needed to check whether the letter is in the word. If it is, it replaces the “_” in the word_guessed list with the letter. If it is not, it reduces the number of lives by 1. In both cases, the letter needed to be added to the list_letters in case the user tried to guess this letter again. 

<img width="473" alt="Pasted Graphic 10" src="https://user-images.githubusercontent.com/91407498/157906311-7a2e7f59-11ea-4e05-b99c-b04d3715b708.png">

This method starts by converting letter to lower case, so it can handle any input from the user. It then runs through an if-else statement. If the letter is in the word, the program:

	1. finds the index of that letter in the word, 
	2. then deletes the “_” at that index in the word_guessed,
	3. before inserting the letter to that index. 

Here, I had to use a try/except statement to deal with the fact that the str.index() method only finds the first occurrence of the argument. In the try statement, the program iterates through the word, looking for the letter. The count variable ensures that the iteration starts from the index of latest occurrence of the letter + 1, not the beginning of the word. The except statement triggers if the word only contains one instance of the letter. If the letter is not in the word, the program moves to the else statement. 

To test this part of the code, I added the check_letter() method into the ask_letter() method. Its position here means it is called when the user enters a valid letter. 

<img width="409" alt="Pasted Graphic 5" src="https://user-images.githubusercontent.com/91407498/157906407-6c57bc99-9199-4b30-85d2-cf826dc558f8.png">

Milestone 4:
The last thing to do was complete the play_game() function. Using a while loop and an if-elif-else statement, the program checks whether the player still has any lives left. If they don’t, they are told they have lost and the game ends. If they do, the game checks to see if there are any unguessed letters left (indicated by num_letters > 0). If there are, the game continues. If not, the player wins. 

Bonus task:
I wanted to include the diagram that appears in the traditional game of Hangman. So, I added in another attribute to the class, called diagram. This is a list of the different stages of the drawing.

<img width="536" alt="Pasted Graphic 8" src="https://user-images.githubusercontent.com/91407498/157906651-64e7ece5-612e-43de-8927-c6b82471173d.png">
<img width="534" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/91407498/157906668-e4c521fb-04cb-42fe-8ad2-2eadc57f1aed.png">

This attribute is then accessed in the else statement of the check_letter() method, that is, if the letter is not in the word. I decided to order the stages of the diagram in reverse so that the index of the stage is equal to the num_lives the player has remaining. 

<img width="501" alt="Pasted Graphic 4" src="https://user-images.githubusercontent.com/91407498/157906833-174f71ec-dae8-494b-aefd-6d0d81598fef.png">
