from src.infrastructure.application import PublicEntity


class CodeAssistanceResponse(PublicEntity):
    tldr: str
    detailed: str
