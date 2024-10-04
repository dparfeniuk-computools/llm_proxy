from fastapi import APIRouter, HTTPException

from src.infrastructure.llm.service import LLMService
from src.rest.code_assistance import contracts

router = APIRouter()

llm_service = LLMService()


@router.get("/code_assistance")
async def get_code_assistance_answer(
    question: str,
) -> contracts.CodeAssistanceResponse:
    try:
        tldr_response = await llm_service.generate_tldr_response(question)
        detailed_response = await llm_service.generate_detailed_response(
            question
        )
        return contracts.CodeAssistanceResponse(
            tldr=tldr_response.get("content"),
            detailed=detailed_response.get("content"),
        )
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
