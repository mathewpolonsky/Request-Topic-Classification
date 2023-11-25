import aiohttp

from typing import Dict


async def classificate_text(text: str) -> Dict[str, str]:
    api_url = "https://patient-buck-weekly.ngrok-free.app/classificate"
    payload = {
        "text": text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=payload) as response:
            answer = await response.json()
            return answer
