import WordVectors
import NounList

class Guess:
    def __init__(self, word):
        self.word = word
        self.isNoun = self.is_noun()
        self.isInVector = self.is_in_vector()
        self.vectorIndex = self.get_vector_index()

    def is_noun(self):
        if self.word in NounList.allNouns:
            return True
        else:
            return False

    def is_in_vector(self):
        if self.word in WordVectors.WordVectors:
            return True
        else:
            return False

    def get_vector_index(self):
        if self.isNoun and self.isInVector:
            i = WordVectors.WordVectors.index(self.word)
            return i
        else: 
            return -1

    def __str__(self):
        return self.word
        #return f"{self.word}, noun: {self.isNoun}, vector: {self.isInVector}, vector index: {self.vectorIndex}"

        

    
