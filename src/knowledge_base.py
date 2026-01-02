import dataclasses
from typing import List, Dict

@dataclasses.dataclass
class Vendor:
    id: str
    name: str
    category: str
    description: str
    location: str
    rating: float

class KnowledgeBase:
    """
    Acts as the data retriever / store for our vendors.
    In a real app, this would query a Vector DB or SQL database.
    For this PoC, we hold everything in memory.
    """
    def __init__(self):
        self.vendors: List[Vendor] = []
        self._load_mock_data()

    def _load_mock_data(self):
        """Loads a diverse set of mock B2B vendors."""
        self.vendors = [
            Vendor(
                id="v1", 
                name="SpeedyTrans Logistics", 
                category="Logistics",
                description="Global shipping and freight forwarding with a focus on cross-border e-commerce and rapid customs clearance. Specialized in cold chain logistics.",
                location="Germany",
                rating=4.8
            ),
            Vendor(
                id="v2", 
                name="TechPack Solutions", 
                category="Packaging",
                description="Sustainable packaging materials for electronics and fragile goods. Offers biodegradable bubble wrap and custom-sized boxes.",
                location="USA",
                rating=4.5
            ),
            Vendor(
                id="v3", 
                name="Quantum Chipsets", 
                category="Electronics",
                description="High-performance silicon chips for AI processing units and industrial automation sensors. ISO 9001 certified manufacturer.",
                location="Taiwan",
                rating=4.9
            ),
            Vendor(
                id="v4", 
                name="EuroRail Cargo", 
                category="Logistics",
                description="Reliable rail freight transport across Europe. Efficient bulk transport for heavy machinery and raw materials. Eco-friendly option.",
                location="France",
                rating=4.2
            ),
            Vendor(
                id="v5", 
                name="GreenLeaf Textiles", 
                category="raw_materials",
                description="Organic cotton and hemp fabric supplier for sustainable fashion brands. Certified fair trade and chemical-free processing.",
                location="India",
                rating=4.7
            ),
            Vendor(
                id="v6", 
                name="RapidAssembly Bots", 
                category="Automation",
                description="Robotic arms and assembly line automation systems. Specialized in automotive and consumer electronics assembly.",
                location="Japan",
                rating=4.6
            ),
             Vendor(
                id="v7", 
                name="SecureCloud Host", 
                category="IT Services",
                description="Enterprise-grade cloud hosting and cybersecurity solutions. HIPAA and GDPR compliant data centers.",
                location="UK",
                rating=4.4
            ),
            Vendor(
                id="v8", 
                name="Precise Moulding", 
                category="Manufacturing",
                description="Custom injection moulding for plastic parts. High precision prototyping and mass production capabilities.",
                location="China",
                rating=4.3
            ),
        ]

    def get_all_vendors(self) -> List[Vendor]:
        return self.vendors

    def get_descriptions(self) -> List[str]:
        return [v.description for v in self.vendors]
