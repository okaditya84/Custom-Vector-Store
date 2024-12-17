import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, storage_path='vector_store.pkl'):
        self.vector_data = {}  # a dictionary to store the vectors
        self.vector_index = {}  # a dictionary to store the index of the vectors for retrieval
        self.storage_path = storage_path
        self.load_store()

    def add_vector(self, vector_id, vector):
        """
        Add a vector to the store
        Args:
            vector_id(str or int): the id of the vector
            vector (numpy array): the vector to be stored
        """
        self.vector_data[vector_id] = vector
        self._update_index(vector_id, vector)
        self.save_store()

    def get_vector(self, vector_id):
        """
        Get the vector from the store
        Args:
            vector_id(str or int): the id of the vector
            
        Returns:
            numpy array: the vector
        """
        return self.vector_data.get(vector_id)

    def _update_index(self, vector_id, vector):
        """
        Update the index of the vector
        Args:
            vector_id(str or int): the id of the vector
            vector (numpy array): the vector to be stored
        """
        for exist_id, exist_vector in self.vector_data.items():
            similarity = np.dot(vector, exist_vector) / (np.linalg.norm(vector) * np.linalg.norm(exist_vector))
            if exist_id not in self.vector_index:
                self.vector_index[exist_id] = {}
            self.vector_index[exist_id][vector_id] = similarity

    def find_similar_vectors(self, query_vector, num_results=5):
        """
        Find the most similar vectors to the query vector
        Args:
            query_vector(numpy array): the query vector
            num_results(int): the number of similar vectors to return
            
        Returns:
            list of tuples: a list of tuples with the vector id and similarity score
        """
        results = []
        for vector_id, vector in self.vector_data.items():
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            results.append((vector_id, similarity))

        # sort the similarity scores in descending order
        results.sort(key=lambda x: x[1], reverse=True)
        # return the top num_results
        return results[:num_results]

    def save_store(self):
        """
        Save the vector store to a file
        """
        with open(self.storage_path, 'wb') as f:
            pickle.dump((self.vector_data, self.vector_index), f)

    def load_store(self):
        """
        Load the vector store from a file
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'rb') as f:
                self.vector_data, self.vector_index = pickle.load(f)