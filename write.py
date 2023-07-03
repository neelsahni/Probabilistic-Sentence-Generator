import string
import random
from graph import Graph, Vertex


def get_words(text_path):
    """
    Iterate through the inputted text file and split the sentences up into words, which will later be converted to
    nodes.
    """

    # Open up text file
    with open(text_path, 'r') as f:
        text = f.read()

        # As we read through text file, split by spaces
        text = ' '.join(text.split())
        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    return words


def make_graph(words):
    """
    Using separated words, create a graph of sentences with higher weights for repeated words
    """
    grph = Graph()

    # Initially, no previous word to check for
    previous_word = None

    # Iterate through separate words
    for word in words:

        # If word not in graph, add it
        word_vertex = grph.get_vertex(word)

        # If previous word exists, create new edge for it, else increment edge weight
        if previous_word:
            previous_word.increase_weight(word_vertex)

        previous_word = word_vertex

    # New map created after all words read through
    grph.create_probability_map()

    return grph


def compose(grph, words, length=50):
    """
    Generate random composition of text by selecting a starting word from the words list, and then using the g graph to
    select the next word based on the probability of the words following the current word.
    """
    composition = []

    # Selects random word from graph
    word = grph.get_vertex(random.choice(words))

    # Iterate through length and add word to composition and graph
    for unit in range(length):
        composition.append(word.value)
        word = grph.get_next_word(word)

    return composition


def main():
    """
    Primary function that starts program and creates sentences
    """

    # Accept input file
    words = get_words('Lord_Of_The_Rings.txt')

    grph = make_graph(words)

    # Create a sentence composition based on parameters
    composition = compose(grph, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    print(main())
