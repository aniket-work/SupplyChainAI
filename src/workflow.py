import logging
from src.document_loader import DocumentProcessor
from src.knowledge_base import ContextRetriever
from src.agents import ProposalDrafter, ComplianceOfficer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(name)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("Orchestrator")

class RFPOrchestrator:
    def __init__(self):
        self.loader = DocumentProcessor()
        self.retriever = ContextRetriever()
        self.drafter = ProposalDrafter()
        self.compliance = ComplianceOfficer()

    def run(self, rfp_path: str):
        logger.info(f"🚀 Starting RFP Process for {rfp_path}")
        
        # Step 1: Ingest
        requirements = self.loader.process_rfp(rfp_path)
        
        final_proposal = []
        
        # Step 2: Process Loop
        for i, req in enumerate(requirements, 1):
            logger.info(f"--- Processing Requirement {i}/{len(requirements)} ---")
            
            # Retrieve
            context = self.retriever.retrieve(req)
            
            # Draft
            draft = self.drafter.draft_section(req, context)
            
            # Review Loop
            approved = False
            attempts = 0
            while not approved and attempts < 3:
                is_valid, feedback = self.compliance.review_draft(draft)
                if is_valid:
                    approved = True
                    final_proposal.append(draft)
                else:
                    logger.info(f"Iterating on draft due to feedback: {feedback}")
                    draft = draft + " [Corrected]" # Simulating fix
                    attempts += 1
            
            if not approved:
                logger.error("Failed to generate compliant draft after 3 attempts.")
                final_proposal.append("[MANUAL REVIEW REQUIRED]")
                
        logger.info("✅ Final Proposal Generated Successfully")
        return final_proposal
