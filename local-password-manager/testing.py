import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
# nltk.download('punkt')
# Load the text from a file
with open('wizard.txt', 'r') as file:
    text = file.read()

# Tokenize the text
tokens = word_tokenize(text)

fdist = FreqDist(tokens)

ea_to = 0

for token in tokens:
    if "ea" in token:
        ea_to += 1

ea_ty = 0

for typ in fdist:
    if "ea" in typ:
        ea_ty += 1

print(f"ea in tokens: {ea_to}")
print(f"ea in types: {ea_ty}")