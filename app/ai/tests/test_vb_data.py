from app.ai.db.chroma_client import users_collection
from app.ai.embeddings.gemini_embed import get_embedding

query_text = "Looking for Media professionals"
query_embedding = get_embedding(query_text)

# 🔹 Use $in operator for list matching
where_filter = {"domain": {"$in": ["Media"]}}

results = users_collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    where=where_filter
)

# 🔹 Process results
users = []
for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    users.append({
        "user_text": doc,
        "email": meta.get("email"),
        "role": meta.get("role"),
        "skills": meta.get("skills"),
        "domain": meta.get("domain")
    })

print(users)