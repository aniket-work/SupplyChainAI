import base64
import requests
import os

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

diagrams = {
    "title_diagram": """
    graph TD
    classDef title fill:#000,stroke:#fff,stroke-width:4px,color:#fff,font-size:24px,font-weight:bold;
    classDef sub fill:#000,stroke:#fff,stroke-width:2px,color:#fff,font-size:16px;
    
    T[SupplyChainAI:<br/>Intelligent Vendor Recommendation Engine]:::title
    S[Powered by TF-IDF & Cosine Similarity]:::sub
    
    T --- S
    linkStyle 0 stroke-width:0px;
    """,

    "architecture": """
    graph LR
        User[Procurement Officer] --> Workflow[Orchestrator]
        Workflow --> KB[("Knowledge Base")]
        Workflow --> Engine[("Recommendation Engine")]
        Workflow --> User
        
        KB ---|Load Data| Workflow
        Engine ---|Fit & Search| Workflow
    """,

    "sequence": """
    sequenceDiagram
        participant User as User
        participant WF as Workflow
        participant KB as Knowledge Base
        participant RE as Rec. Engine
        
        User->>WF: Run Application
        activate WF
        WF->>KB: Load Vendor Data
        activate KB
        KB-->>WF: List[Vendor]
        deactivate KB
        
        WF->>RE: fit(vendors)
        activate RE
        RE-->>WF: Model Ready
        deactivate RE
        
        loop Every Query
            User->>WF: "Fast logistics in Europe"
            WF->>RE: search(query)
            activate RE
            RE->>RE: Vectorize Query
            RE->>RE: Calculate Cosine Similarity
            RE-->>WF: Ranked Results
            deactivate RE
            WF-->>User: Display Top Vendors
        end
        deactivate WF
    """,
    "class_diagram": """
    classDiagram
        class Vendor {
            +str id
            +str name
            +str category
            +str description
            +str location
            +float rating
        }
        
        class KnowledgeBase {
            +List~Vendor~ vendors
            +load_mock_data()
            +get_all_vendors()
        }
        
        class RecommendationEngine {
            +TfidfVectorizer vectorizer
            +fit(vendors)
            +search(query)
        }
        
        KnowledgeBase "1" *-- "many" Vendor : contains
        RecommendationEngine ..> Vendor : uses
    """
}

def generate_diagrams():
    print("Generating diagrams...")
    for name, code in diagrams.items():
        try:
            # Basic encoding for mermaid.ink
            graphbytes = code.encode("utf8")
            base64_bytes = base64.b64encode(graphbytes)
            base64_string = base64_bytes.decode("ascii")
            
            # Using basic graph rendering
            url = f"https://mermaid.ink/img/{base64_string}"
            
            # For complex styling or dark mode, sometimes we need parameters, but simple is safer for reliability
            # Let's add a background color if possible or just rely on default
            
            print(f"Fetching {name}...")
            response = requests.get(url)
            
            if response.status_code == 200:
                with open(f"images/{name}.png", 'wb') as f:
                    f.write(response.content)
                print(f"Saved images/{name}.png")
            else:
                print(f"Failed to fetch {name}: {response.status_code}")
        except Exception as e:
            print(f"Error generating {name}: {e}")

if __name__ == "__main__":
    generate_diagrams()
