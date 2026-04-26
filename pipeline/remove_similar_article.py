from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')


def remove_similar_article(df):
    df['description'] = df['description'].fillna('')
    embeddings = model.encode(df['description'].tolist(), convert_to_tensor=True)
    df['description_embedding'] = embeddings.cpu().numpy().tolist()
    similarity_matrix = util.cos_sim(embeddings, embeddings)

    threshold = 0.8
    to_remove = set()

    for i in range(len(df)):
        if i in to_remove:
            continue

        for j in range(i + 1, len(df)):
            if similarity_matrix[i][j] > threshold:
                to_remove.add(j)

    df= df.drop(index=list(to_remove)).reset_index(drop=True)
    return df