import json


EXPECTED_KEYS = {
    "is_relevant": False,
    "relevance_score": 0,
    "confidence_score": 0.0,
    "deal_type": "none",
    "fmcg_entities": [],
    "keywords": [],
    "summary": "",
    "reason": ""
}
def parse_and_fill(response_text):
    try:
        data = json.loads(response_text)
    except:
        data = {}

    for key, default in EXPECTED_KEYS.items():
        if key not in data or data[key] is None:
            data[key] = default

    return data