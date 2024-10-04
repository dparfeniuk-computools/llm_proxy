import httpx
from httpx import RequestError

from src.config import settings


class LLMService:

    async def generate_tldr_response(self, prompt: str) -> dict:
        if settings.llm_host == "invalid":
            raise ValueError(
                "The llama_endpoint is not set in the configuration."
            )
        try:
            async with httpx.AsyncClient(timeout=200.0) as client:
                response = await client.post(
                    f"{settings.llm_host}/completion",
                    json={"prompt": prompt, "max_tokens": 64},
                )
                return response.json()
        except RequestError as e:
            raise RuntimeError(f"Error interacting with LLM service: {e}")

    async def generate_detailed_response(self, prompt: str) -> dict:
        if settings.llm_host == "invalid":
            raise ValueError(
                "The llama_endpoint is not set in the configuration."
            )
        try:
            async with httpx.AsyncClient(timeout=200.0) as client:
                response = await client.post(
                    f"{settings.llm_host}/completion",
                    json={"prompt": prompt, "max_tokens": 128},
                )
                return response.json()
        except RequestError as e:
            raise RuntimeError(f"Error interacting with LLM service: {e}")
