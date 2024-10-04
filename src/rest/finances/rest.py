from fastapi import APIRouter, HTTPException

from src.infrastructure.llm.service import LLMService
from src.rest.finances import contracts

router = APIRouter()

llm_service = LLMService()


@router.get("/finances")
async def get_finances_answer(question: str) -> contracts.FinancesResponse:
    try:
        tldr_response = await llm_service.generate_tldr_response(question)
        detailed_response = await llm_service.generate_detailed_response(
            question
        )
        return contracts.FinancesResponse(
            tldr=tldr_response.get("content"),
            detailed=detailed_response.get("content"),
        )
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
