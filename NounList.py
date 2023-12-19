'''from nltk.corpus import wordnet
# reference: https://www.nltk.org/howto/wordnet.html

def get_nouns():
    nouns = []
    for word in wordnet.all_synsets(wordnet.NOUN):
        for thisWord in word.lemmas():
            noun = thisWord.name()
            # filter out proper nouns and pronouns
            if not noun.islower() or noun == noun.capitalize():
                continue
            # filter out multi-word nouns
            if '_' in noun:
                continue
            nouns.append(noun)
    return nouns'''

def get_common_nouns():
    nouns = ["book", "dog", "cat", "bus", "brick", "computer", "thought", "doctor", "coffee", "cup", "caramel", "perfume", "grass", "wood"]
    return nouns

allNouns = get_common_nouns()
nounList = get_common_nouns()
