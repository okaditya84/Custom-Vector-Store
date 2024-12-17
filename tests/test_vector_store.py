import unittest
import numpy as np
from vector_store.vector_store import VectorStore

class TestVectorStore(unittest.TestCase):

    def setUp(self):
        self.store = VectorStore()
        self.vector1 = np.array([1, 2, 3])
        self.vector2 = np.array([4, 5, 6])
        self.store.add_vector('vector1', self.vector1)
        self.store.add_vector('vector2', self.vector2)

    def test_add_vector(self):
        self.assertIn('vector1', self.store.vector_data)
        self.assertIn('vector2', self.store.vector_data)

    def test_get_vector(self):
        vector = self.store.get_vector('vector1')
        np.testing.assert_array_equal(vector, self.vector1)

    def test_find_similar_vectors(self):
        query_vector = np.array([1, 2, 3])
        similar_vectors = self.store.find_similar_vectors(query_vector, num_results=2)
        self.assertEqual(len(similar_vectors), 2)
        self.assertEqual(similar_vectors[0][0], 'vector1')

if __name__ == '__main__':
    unittest.main()