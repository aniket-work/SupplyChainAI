import logging
import time

class ProposalDrafter:
    """
    Simulates an LLM agent that drafts content.
    """
    def __init__(self):
        self.logger = logging.getLogger("ProposalDrafter")

    def draft_section(self, requirement: str, context: str) -> str:
        self.logger.info(f"Drafting response for: {requirement[:20]}...")
        time.sleep(0.5) # Simulate LLM latency
        return f"Responsive Statement: We fully comply. {context} (Drafted by AI)"

class ComplianceOfficer:
    """
    Simulates an agent that checks against business rules.
    """
    def __init__(self):
        self.logger = logging.getLogger("ComplianceOfficer")

    def review_draft(self, draft: str) -> tuple[bool, str]:
        self.logger.info("Reviewing draft for compliance...")
        
        forbidden_terms = ["guarantee 100%", "no downtime ever", "free of charge"]
        
        for term in forbidden_terms:
            if term in draft:
                self.logger.warning(f"Compliance violation found: '{term}'")
                return False, f"Remove forbidden term: {term}"
        
        if "AI" not in draft: # Arbitrary rule
             self.logger.warning("Compliance check: Missing AI attribution.")
             return False, "Add AI attribution."

        self.logger.info("Draft approved.")
        return True, "Approved"
