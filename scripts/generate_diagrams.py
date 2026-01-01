import base64
import requests
import os
import sys

# Define the diagrams
diagrams = {
    "title": """
    %%{init: {'theme': 'default', 'themeVariables': { 'mainBkg': '#ffffff', 'textColor': '#000000', 'lineColor': '#000000'}}}%%
    mindmap
      root((Autonomous RFP<br/>Response System))
        (Input Processing)
            ::icon(fa fa-file-pdf-o)
            [Document Loader]
            [Requirement Extractor]
        (Intelligence Layer)
            ::icon(fa fa-brain)
            [Context Retrieval]
            [Vector Database]
        (Agentic Core)
            ::icon(fa fa-users)
            [Proposal Drafter]
            [Compliance Officer]
        (Output)
            ::icon(fa fa-file-text)
            [Final Proposal]
            [Audit Log]
    """,
    
    "architecture": """
    %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ffcc00', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#fff'}}}%%
    graph TB
        subgraph Input Source
            RFP[RFP Document]
            KB[(Company Knowledge Base)]
        end

        subgraph "Autonomous Agent Swarm"
            direction TB
            DP[Document Processor Agent]
            CR[Context Retriever Agent]
            PD[Proposal Drafter Agent]
            CO[Compliance Officer Agent]
            
            DP -->|Extracted Requirements| PD
            KB -->|Technical Context| CR
            CR -->|Relevant chunks| PD
            PD -->|Draft Proposal| CO
            CO -->|Feedback| PD
        end

        subgraph Output
            Final[Final Proposal PDF]
        end

        RFP --> DP
        CO -->|Approved| Final
        
        style RFP fill:#f9f,stroke:#333
        style Final fill:#9f9,stroke:#333
        style DP fill:#fff,stroke:#333
        style CR fill:#fff,stroke:#333
        style PD fill:#fff,stroke:#333
        style CO fill:#fff,stroke:#333
    """,
    
    "sequence": """
    %%{init: {'theme': 'forest'}}%%
    sequenceDiagram
        participant User
        participant Orchestrator
        participant DocProcessor
        participant Retriever
        participant Drafter
        participant Compliance

        User->>Orchestrator: Start Job (RFP File)
        Orchestrator->>DocProcessor: Parse Requirements
        DocProcessor-->>Orchestrator: List[Requirement]
        
        loop For Each Requirement
            Orchestrator->>Retriever: Get Context(Requirement)
            Retriever-->>Orchestrator: Context Chunks
            
            Orchestrator->>Drafter: Draft Response(Req, Context)
            Drafter-->>Orchestrator: Draft Text
            
            Orchestrator->>Compliance: Review(Draft Text)
            alt Violation Found
                Compliance-->>Orchestrator: Feedack (Revision Needed)
                Orchestrator->>Drafter: Revise(Feedback)
            else Approved
                Compliance-->>Orchestrator: Status OK
            end
        end
        
        Orchestrator->>User: Complete Proposal
    """,

    "workflow": """
    %%{init: {'theme': 'neutral'}}%%
    flowchart LR
        Start((Start)) --> Load{Load RFP}
        Load --> |Success| Extract[Extract Req]
        Load --> |Fail| Error[Log Error]
        
        Extract --> Retrieve[Retrieve Context]
        Retrieve --> Draft[Draft Section]
        Draft --> Review{Compliance Check}
        
        Review -->|Pass| Compile[Compile Document]
        Review -->|Fail| Revise[Refine Draft]
        Revise --> Review
        
        Compile --> Stop((End))
    """
}

def generate_diagrams():
    os.makedirs("images", exist_ok=True)
    
    print("🎨 Generating Mermaid diagrams...")
    
    for name, code in diagrams.items():
        try:
            # Encode the diagram
            graphbytes = code.encode("utf8")
            base64_bytes = base64.b64encode(graphbytes)
            base64_string = base64_bytes.decode("ascii")
            
            # Construct URL
            url = f"https://mermaid.ink/img/{base64_string}"
            
            print(f"  - Fetching {name}_diagram.png...")
            response = requests.get(url)
            
            if response.status_code == 200:
                with open(f"images/{name}_diagram.png", 'wb') as f:
                    f.write(response.content)
                print(f"    ✅ Saved to images/{name}_diagram.png")
            else:
                print(f"    ❌ Failed to fetch {name}: {response.status_code}")
                
        except Exception as e:
            print(f"    ❌ Error generating {name}: {str(e)}")

if __name__ == "__main__":
    generate_diagrams()
