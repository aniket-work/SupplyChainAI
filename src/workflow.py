import sys
import os

# Ensure we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.knowledge_base import KnowledgeBase
from src.recommendation_engine import RecommendationEngine

def main():
    print("--- Starting SupplyChainAI Recommendation Engine ---")

    # 1. Initialize Knowledge Base
    kb = KnowledgeBase()
    vendors = kb.get_all_vendors()
    print(f"Loaded {len(vendors)} vendors from Knowledge Base.")

    # 2. Initialize and Fit Recommendation Engine
    engine = RecommendationEngine()
    engine.fit(vendors)

    # 3. Define Test Queries
    queries = [
        "Need a fast logistics provider for frozen goods in Europe",
        "Sustainable packaging for electronics",
        "High quality precision manufacturing for chips",
        "Automated assembly line robots",
        "Cloud hosting for healthcare data"
    ]

    # 4. Run Queries
    print("\n--- Running Search Queries ---")
    for query in queries:
        print(f"\nQuery: '{query}'")
        results = engine.search(query)
        
        if not results:
            print("  No matching vendors found.")
        else:
            for res in results:
                vendor = res['vendor']
                score = res['score']
                print(f"  > [{score:.4f}] {vendor.name} ({vendor.location}) - {vendor.category}")
                print(f"    Desc: {vendor.description[:80]}...")

    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    main()
