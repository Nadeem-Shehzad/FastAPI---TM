# app/ai/tests/test_vector_db.py

from app.ai.db.chroma_client import users_collection

def view_vector_db():
    data = users_collection.get(include=["documents", "metadatas"])
    
    print("🔥 DEBUG START")

    if not data["documents"]:
        print("❌ No documents found in Chroma DB")
        return

    for doc, meta in zip(data["documents"], data["metadatas"]):
        print("Doc:", doc)
        print("Meta:", meta)
        print("-" * 40)

if __name__ == "__main__":
    view_vector_db()