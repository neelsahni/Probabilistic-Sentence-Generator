import random


class Vertex(object):
    def __init__(self, value):
        """
        Initialize variables used in function
        """
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge(self, vertex, weight=0):
        """
        Create a weight for the vertex
        """

        self.adjacent[vertex] = weight

    def increase_weight(self, vertex):
        """
        Increment weight for vertex if necessary
        """

        # When repeat occurs, vertex weight will increase by 1
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        """
        Return key of nodes adjacent to a vertex
        """

        return self.adjacent.keys()

    def probability_map(self):
        """
        Create a map of probabilities for vertex weights
        """

        # Iterate through adjacent vertices and weights and add vertex and weight values
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        """
        Randomly decide based off of weight what next word in composition should be
        """

        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph(object):
    def __init__(self):
        """
        Initialize set of vertices
        """
        self.vertices = {}

    def get_vertex_values(self):
        """
        Return the set of vertices and their corresponding values
        """
        return set(self.vertices.keys())

    def add_vertex(self, value):
        """
        Add the a new vertex and its value to the list of vertices
        """
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        """
        Return the value of the vertex
        """

        # Add vertex value if not in list and return
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        """
        Return next value of next vertex word in vertex list
        """

        return self.vertices[current_vertex.value].next_word()

    def create_probability_map(self):
        """
        Iterate through vertices values and generate the map of probabilities accordingly
        """

        # At each vertex value in list, recreate probability map
        for vertex in self.vertices.values():
            vertex.probability_map()
