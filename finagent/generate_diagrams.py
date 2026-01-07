import base64
import requests
import os

def generate_mermaid_diagrams():
    """Converts Mermaid code to PNG using mermaid.ink."""
    diagrams = {
        "architecture-diagram": """
graph TB
    subgraph "Market Monitoring"
        A[News Stream] --> B[Sentiment Engine]
        C[Market Data] --> D[Price Monitor]
    end
    
    subgraph "FinAgent Core"
        B --> E[Signal Aggregator]
        D --> E
        E --> F[Rebalancing Strategy]
    end
    
    subgraph "Execution Layer"
        F --> G[Portfolio Tracker]
        G --> H[Trade Execution]
    end
    
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef agent fill:#00b894,stroke:#006266,color:white;
    class F,E agent;
        """,
        "workflow-flow": """
sequenceDiagram
    participant News as News/Social Stream
    participant Agent as FinAgent Analyst
    participant Port as Portfolio Manager
    
    News->>Agent: Market Context (NLP)
    Agent->>Agent: Sentiment Injection
    Agent->>Port: Weighted Signals
    Port->>Port: Execute Rebalancing
    Port-->>News: Performance Logging
        """
    }

    os.makedirs("images", exist_ok=True)

    for name, code in diagrams.items():
        encoded = base64.b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        print(f"Fetching diagram: {name}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{name}.png", 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved images/{name}.png")
        else:
            print(f"Failed to fetch diagram {name}: {response.status_code}")

if __name__ == "__main__":
    generate_mermaid_diagrams()
