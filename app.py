from vector_store import VectorStore
import numpy as np

# create an instance of the VectorStore class
vector_store = VectorStore()

sentences = ["I love machine learning", "I love deep learning", "I love natural language processing"]

#tokenization and vocabulary creation
vocabulary = set()

for s in sentences:
    tokens=s.lower().split()
    vocabulary.update(tokens)

#assign unique indices to words in the vocab
word_to_index = {word: i for i, word in enumerate(vocabulary)}

#initialize sentence_vectors dictionary
sentence_vectors = {}

#vectorization (this is normally done using the NLTK library)
for s in sentences:
    tokens= s.lower().split()
    vector = np.zeros(len(vocabulary))
    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[s] = vector


#add to the vector store
for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)

#search similarity
query_sentence="machine learning is awesome"
query_vector = np.zeros(len(vocabulary))
query_token = query_sentence.lower().split()
for token in query_token:
    if token in word_to_index:
        query_vector[word_to_index[token]] += 1

similar_vectors = vector_store.find_similar_vectors(query_vector, num_results=2)
print("Query", query_sentence)
print("Similar sentences:")
for s, similarity in similar_vectors:
    print(f"{s}: Similarity: {similarity:.4f}")
