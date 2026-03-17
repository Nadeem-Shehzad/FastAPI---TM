import chromadb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ NEW WAY (no Settings, no chroma_db_impl)
client = chromadb.PersistentClient(
    path=os.path.join(BASE_DIR, "chroma_storage")
)

# ✅ consistent naming
users_collection = client.get_or_create_collection(
    name="users"
)