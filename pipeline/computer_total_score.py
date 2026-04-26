def compute_total_score(row):
    deal_weight_map = {
        "acquisition": 10,
        "merger": 9,
        "investment": 8,
        "partnership": 6,
        "none": 0
    }

    deal_weight = deal_weight_map.get(row['deal_type'], 0)
    entities = row['fmcg_entities']
    entity_score = min(len(entities) * 2, 10) if isinstance(entities, list) else 0

    total_score = (
        0.5 * row['relevance_score'] +
        0.2 * (row['confidence_score'] * 10) +
        0.2 * deal_weight +
        0.1 * entity_score
    )

    return round(total_score, 2)
