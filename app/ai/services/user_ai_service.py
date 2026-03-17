from app.ai.db.chroma_client import user_collection
from app.ai.embeddings.gemini_embed import get_embedding

# 🔹 Convert user data into a single text
def build_user_text(user):
    return f"""
    Name: {user['name']}
    Role: {user['role']}
    Interests: {', '.join(user['interests'])}
    """

# 🔹 Store user embedding
def add_user_embedding(user):
    text = build_user_text(user)
    embedding = get_embedding(text)

    user_collection.add(
        ids=[user["id"]],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"email": user["email"]}]
    )

# 🔹 Find similar users
def find_similar_users(query_text: str, top_k: int = 3):
    embedding = get_embedding(query_text)

    results = user_collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]