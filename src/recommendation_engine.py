from typing import List, Dict, Any
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .knowledge_base import Vendor

class RecommendationEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.vendor_vectors = None
        self.vendors: List[Vendor] = []

    def fit(self, vendors: List[Vendor]):
        """
        'Trains' the engine by vectorizing the vendor descriptions.
        """
        self.vendors = vendors
        descriptions = [v.description for v in vendors]
        self.vendor_vectors = self.vectorizer.fit_transform(descriptions)
        print(f"Engine fitted with {len(vendors)} vendors.")

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Searches for vendors matching the query string.
        Returns a list of dictionaries with vendor info and score.
        """
        if not self.vendors or self.vendor_vectors is None:
            return []

        # Vectorize the query
        query_vector = self.vectorizer.transform([query])

        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(query_vector, self.vendor_vectors).flatten()

        # Get top_k indices
        # argsort sorts in ascending order, so we take the last k and reverse them
        related_docs_indices = cosine_similarities.argsort()[:-top_k-1:-1]

        results = []
        for match_index in related_docs_indices:
            score = cosine_similarities[match_index]
            if score > 0.0: # Filter out completely irrelevant results
                vendor = self.vendors[match_index]
                results.append({
                    "vendor": vendor,
                    "score": float(score)
                })
        
        return results
