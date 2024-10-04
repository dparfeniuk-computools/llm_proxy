from fastapi import APIRouter, HTTPException

from src.infrastructure.llm.service import LLMService
from src.rest.research import contracts

router = APIRouter()

llm_service = LLMService()


@router.get("/research")
async def get_research_answer(question: str) -> contracts.ResearchResponse:
    try:
        tldr_response = await llm_service.generate_tldr_response(question)
        detailed_response = await llm_service.generate_detailed_response(
            question
        )
        return contracts.ResearchResponse(
            tldr=tldr_response.get("content"),
            detailed=detailed_response.get("content"),
        )
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
