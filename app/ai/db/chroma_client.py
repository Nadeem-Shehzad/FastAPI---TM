import chromadb
from chromadb.config import Settings


# Create persistent DB (stored on disk)
client = chromadb.Client(
    Settings(
        persist_directory="app/ai/chroma_storage"  # folder auto-created
    )
)

user_collection = client.get_or_create_collection(
    name="users_collection"
)