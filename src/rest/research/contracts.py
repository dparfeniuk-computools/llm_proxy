from src.infrastructure.application import PublicEntity


class ResearchResponse(PublicEntity):
    tldr: str
    detailed: str
