import numpy as np
from scipy import spatial
import NounOfTheDay

#source: https://medium.com/analytics-vidhya/basics-of-using-pre-trained-glove-vectors-in-python-d38905f356db#:~:text=Global%20Vectors%20for%20Word%20Representation,in%20a%20high%2Ddimensional%20space.
      
vectors_dictionary = {}

with open("glove.6B.50d.txt", 'r', encoding="utf-8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        vectors_dictionary[word] = vector

def find_closest_word(embedding):
    return sorted(vectors_dictionary.keys(), key=lambda word: spatial.distance.euclidean(vectors_dictionary[word], embedding))

new_noun = NounOfTheDay.noun
if(new_noun in vectors_dictionary):
    WordVectors = find_closest_word(vectors_dictionary[new_noun])
else:
    print("not in word list")





