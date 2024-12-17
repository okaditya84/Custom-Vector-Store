# Usage

## Basic Example

Here's a basic example of how to use the Custom Vector Store:

```python
from vector_store import VectorStore
import numpy as np

# Initialize the vector store
store = VectorStore()

# Add vectors
store.add_vector('vector1', np.array([1, 2, 3]))
store.add_vector('vector2', np.array([4, 5, 6]))

# Find similar vectors
query_vector = np.array([1, 2, 3])
similar_vectors = store.find_similar_vectors(query_vector, num_results=2)
print(similar_vectors)