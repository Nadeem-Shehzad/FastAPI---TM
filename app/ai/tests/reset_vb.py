from app.ai.db.chroma_client import users_collection

print("⚠️ Fetching all IDs...")

data = users_collection.get()

ids = data["ids"]

print(f"Deleting {len(ids)} records...")

if ids:
    users_collection.delete(ids=ids)

print("✅ Vector DB cleared")