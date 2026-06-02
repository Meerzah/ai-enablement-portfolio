"""
RAG Tool — Vertex AI Vector Search wrapper for runbook retrieval
"""

import os
from google.cloud import aiplatform
from vertexai.language_models import TextEmbeddingModel

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
INDEX_ENDPOINT_ID = os.environ.get("VERTEX_INDEX_ENDPOINT_ID", "")
DEPLOYED_INDEX_ID = os.environ.get("VERTEX_DEPLOYED_INDEX_ID", "")

_embedding_model = None


def _get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")
    return _embedding_model


def search_runbooks(query: str, top_k: int = 5) -> dict:
    """
    Searches internal IT runbooks for content relevant to the query.

    Args:
        query: The user's natural language question.
        top_k: Number of runbook chunks to retrieve (default 5).

    Returns:
        A dict with 'results' — a list of matching runbook chunks with source and content.
    """
    model = _get_embedding_model()
    embeddings = model.get_embeddings([query])
    query_vector = embeddings[0].values

    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
        index_endpoint_name=INDEX_ENDPOINT_ID
    )

    response = index_endpoint.find_neighbors(
        deployed_index_id=DEPLOYED_INDEX_ID,
        queries=[query_vector],
        num_neighbors=top_k,
    )

    results = []
    for neighbor in response[0]:
        results.append({
            "id": neighbor.id,
            "distance": round(neighbor.distance, 4),
            "content": neighbor.restricts[0].allow_list[0] if neighbor.restricts else "",
        })

    return {"query": query, "results": results, "count": len(results)}
