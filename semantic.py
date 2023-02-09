# Imports the spaCy package
import spacy

# Accesses the language model
nlp = spacy.load('en_core_web_sm')

# Parses three words through the language model  
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Prints comparisons of the words in the form of a decimal between 0 and 1 
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Parses the string and compares every item in the string to every other item
tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

""" 
The comparisons here were, as indicated in the pdf, interesting because the 
cat and monkey were fairly similar but the apple and banana were more similar. 
It would be interesting to know the levels of group they are classified in - 
tree fruit, four-legged land mammal, that sort of thing, to understand the difference in similarity rating.
Apples are not similar to monkeys despite the monkeys having a fruit association
via the banana. I wasn't sure why cats are more similar to bananas (0.22) than they
are to apples (0.20), so that would be interesting to find out.
"""

# My own example for looking at similarities:
tokens2 = nlp("balloon birthday cake biscuit anniversary ")
for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

"""
We weren't asked to comment on our own suggested list, but I thought I'd point out it's strange that
cakes and biscuits are thought of as more similar than birthdays and anniversaries.
"""

# Sets up a sentence and a list of sentences to compare it with for similarity at a sentence level
sentence_to_compare ="Why is my cat on the car"
sentences = [
            "where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"
            ]

# Parses the sentence through the nlp language model
model_sentence = nlp(sentence_to_compare)

# Compares each sentence in the list for similarity with the model sentences and prints result
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)


"""
When I ran the code with the other language model, en_core_web_sm, I got the following User Warning each time .similarity was called:

UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on 
the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models,
 e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word 
 vectors, or use one of the larger models instead if available.
 
 The similarities themselves were very different from the other model, and included some very strange things like a monkey being more 
 similar to an apple (.75) than it is to a cat (.6).
 
 """