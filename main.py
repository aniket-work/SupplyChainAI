from src.workflow import RFPOrchestrator
import sys

def main():
    print("==============================================")
    print("   AUTOMOUS RFP RESPONSE SYSTEM - v1.0.0")
    print("==============================================\n")
    
    orchestrator = RFPOrchestrator()
    proposal = orchestrator.run("sample_rfp_govt_project.pdf")
    
    print("\n--- GENERATED PROPOSAL PREVIEW ---")
    for section in proposal:
        print(f"> {section}")
    print("----------------------------------")

if __name__ == "__main__":
    main()
