# PYDLE
#### Video Demo
[Video](https://www.youtube.com/watch?v=D83o551FARc)
---
#### Description
Pydle is a recreation of the popular New York Times game Wordle. In Pydle, players must find a five-letter word within six attempts. The word they are looking for can be a noun, a verb or even an adjective. Unlike Wordle, the words in Pydle can also be in the plural form. In addition, players can guess any combination of five letters containing letters from A to Z.

After winning or losing a round, players have the option of calling up the definition of the word. Afterwards, they can choose whether to finish the game or play another round.

#### How does the game work?
Pydle uses the external library `random-word` and imports `RandomWords`. The library is used to fetch a random word until it has the required length of five letters. After successfully returning a word of length, the imported external library `PyDictionary` is used to check if the word actually exists. If `meaning()` returns a definition, the word is considered suitable for the game and is used to start a round.

The function that hosts the round has a counter variable to keep track of the number of attempts used to find the searched word. At the start of a round the player is asked to enter a guess. The value entered is checked against the built-in library `re`, which stands for `regular expression`. If the test finds the input to be valid, the guess is compared with the searched word. The external `colorama` library is used to colour the characters accordingly. When the comparison is complete, a list of coloured characters is returned.

The round continues until the player either runs out of guesses or finds the searched word and wins. In both cases, the player has the option to find out what the word was and to get a definition using `meaning()`.  Finally, the player can decide to play another round or quit the game.

#### External Libraries
1. [random-word](https://pypi.org/project/Random-Word/)
2. [PyDictionary](https://pypi.org/project/PyDictionary/)
3. [colorama](https://pypi.org/project/colorama/)
