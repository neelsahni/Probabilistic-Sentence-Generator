# Probabilistic Sentence Generator

## Functionality

The program functions similarity to a Markov chain model. In a traditional Markov chain, the probability of transitioning from one state to another depends solely on the current state and is uninfluenced by the history of transitions. 

In this program, the weighting mechanism is a result of observing frequencies or counts of transitions between words (states). The more frequently a connection between two words occurs, the higher the weight assigned to that connection. 

When the user inputs a text file, a weighted graph, outlined by the mechanism above, is used to probabilistically compose sentences.

As an example, consider the current state to be the word "I" and that the only 2 words that follow "I" in the entire text file are "am" and "want." "I am" occurs once in the text file and "I want" occurs thrice. This would make the edge between "I" and "am" have a weight of 1 and the edge between "I" and "want" have a weight of 3. As a result, when the program begins generating sentences, given that "I" is outputted, there is a 25% chance (1/(3+1)) that "am" follows and a 75% chance (3/(3+1)) that "want" follows.

Note: Only one text file was used in this program for the sake of example. To use your own text, replace 'Lord_Of_The_Rings.txt' with a different text file.

## Looking Ahead

Admittedly, some of the sentences are unclear. In the future, I'd look to modify my program to produce proper sentences by adding some grammar and punctuation checks.
