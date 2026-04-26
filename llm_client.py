import os
from pathlib import Path

from google.genai import types
from google import genai


gemini_api_key=os.getenv("LLM_API_KEY")

llm_client = genai.Client(api_key=gemini_api_key)

def get_prompt(file_path: str):
    base_dir =  Path.cwd()
    template_path = base_dir / "prompts" / file_path
    template = Path(template_path).read_text()
    return template
def generate_ans(data: str, prompt_path: str):
    prompt = get_prompt(prompt_path)

    input_text = f"""
    {prompt}
    ##input
    {data}
    """

    response = llm_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=input_text,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",  # 🔥 IMPORTANT
        ),
    )
    return response.text