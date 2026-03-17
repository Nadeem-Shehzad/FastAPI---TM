from app.ai.db.chroma_client import users_collection
from app.ai.embeddings.gemini_embed import get_embedding

# 🔹 Convert user data into a single text
def build_user_text(user):
    role = str(user['role']).split('.')[-1]

    return f"""
    Name: {user['name']}
    Role: {role}
    Skills: {', '.join(user['skills'])}
    """

# 🔹 Store user embedding
def add_user_embedding(user):

    print("🔥 Inside add_user_embedding")

    text = build_user_text(user)
    print("TEXT:", text)

    embedding = get_embedding(text)
    print("✅ Embedding created")

    users_collection.add(
        ids=[user["id"]],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "email": user["email"],
                "role": user["role"],
                "skills": user.get("skills",[])
            }
        ]
    )

    print("✅ Added to Chroma")
