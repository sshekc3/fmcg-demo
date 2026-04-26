from llm_client import generate_ans
from pipeline.parse_and_fill import parse_and_fill


def score_article(full_text:str):
    response = generate_ans(data=full_text,prompt_path='score_system.md')
    return parse_and_fill(response)