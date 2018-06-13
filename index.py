import random
class Markov:
    def __init__(self, order):
        self.order = order
        self.group_size = self.order + 1
        self.text = None
        self.graph = {}
        return 

    def train(self, filename):
        self.text = file(filename).read().split()
        self.text = self.text+self.text[:self.order]
        for i in range (0, len (self.text) - self.group_size):
            key = tuple (self.text [i : i + self.order] )
            value = self.text [i + self.order] 
            if key in self.graph:
                self.graph [key] .append (value)
            else:
                self.graph [key] = [value]
        return
    def generate (self,length):
        index = random.randint (0, len (self.text) - self.order)
        result = self.text[index : index + self.order]
        for i in range (length):
            state = tuple (result [len (result) - self.order : ] )
            next_word = random.choice (self.graph[state])
            result.append (next_word)
        return " ".join (result [self.order : ] )

m = Markov(2)
m.train('util/robert_frost.txt')
print m.generate(100)