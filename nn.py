from matrices import Matrix, add, multiply, fromVector
import math as m
import copy as c

class NeuralNetwork:

    def __init__(self, inputs, hidden, outputs):
        self.num_input_nodes = inputs
        self.num_hidden_nodes = hidden
        self.num_output_nodes = outputs

        self.weights_i = Matrix(self.num_hidden_nodes, self.num_input_nodes, True)
        self.weights_h = Matrix(self.num_output_nodes, self.num_hidden_nodes, True)
        self.bias_i = Matrix(self.num_hidden_nodes, 1, True)
        self.bias_h = Matrix(self.num_output_nodes, 1, True)

    def activation(self, x):
        return 1/(1+m.exp(-1*x))

    def feedForward(self, input):
        input = fromVector(input)
        hidden = add(multiply(self.weights_i, input), self.bias_i)
        hidden.mapOver(self.activation)
        output = add(multiply(self.weights_h, hidden), self.bias_h)
        output.mapOver(self.activation)
        return output
    
    def createCopy(self):
        return c.deepcopy(self)
