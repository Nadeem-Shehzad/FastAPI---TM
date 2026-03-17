from app.ai.db.chroma_client import user_collection
from app.ai.embeddings.gemini_embed import get_embedding


# 🔹 Step 1: Add users to vector DB
def add_test_users():
    users = [
        {"id": "1", "text": "Backend Developer AI FastAPI Databases"},
        {"id": "2", "text": "Machine Learning Engineer AI Python Deep Learning"},
        {"id": "3", "text": "Frontend Developer React UI UX"}
    ]

    for user in users:
        embedding = get_embedding(user["text"])

        user_collection.add(
            ids=[user["id"]],
            documents=[user["text"]],
            embeddings=[embedding],
            metadatas=[{"id": user["id"]}]  # <-- store IDs here
        )

    print("✅ Users added to Chroma")

# 🔹 Step 2: View stored data
def view_data():
    data = user_collection.get(include=["documents", "metadatas"])

    print("\n📦 Stored Data in Chroma:")

    # Safely get IDs from metadatas
    ids = [m["id"] for m in (data["metadatas"] or [])]
    print("IDs:", ids)
    print("Documents:", data["documents"])

# 🔹 Step 3: Test similarity search
def test_similarity():
    query = "React"

    query_embedding = get_embedding(query)

    results = user_collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    print("\n🔍 Query:", query)
    print("✅ Similar Results:")
    print(results["documents"])


# 🔥 Run everything
if __name__ == "__main__":
    add_test_users()
    view_data()
    test_similarity()