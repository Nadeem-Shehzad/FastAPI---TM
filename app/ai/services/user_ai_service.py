from app.ai.db.chroma_client import users_collection
from app.ai.embeddings.gemini_embed import get_embedding

# 🔹 Convert user data into a single text
def build_user_text(user):
    role = str(user['role']).split('.')[-1]
    skills = ", ".join(user.get("skills", []))
    domain = detect_domain(user)

    return f"""
    This user is a professional in the {domain} industry.

    Their role is {role}, and they specialize in {skills}.

    They have hands-on experience and expertise in {domain}-related work,
    collaborating with others and solving real-world problems in this domain.
    """

def detect_domain(user):
    skills_list = [s.lower() for s in user.get("skills", [])]
    domains = []

    if any(x in skills_list for x in ["react", "node", "nestjs", "python", "backend", "frontend", "ai"]):
        domains.append("IT")

    if any(x in skills_list for x in ["chef", "cooking", "food", "food analyst"]):
        domains.append("Food")

    if any(x in skills_list for x in ["actor", "singer", "producer", "director"]):
        domains.append("Media")

    if any(x in skills_list for x in ["trader", "analyst"]):
        domains.append("Business")

    return domains if domains else ["Other"]


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
                "skills": user.get("skills",[]),
                "domain": detect_domain(user) 
            }
        ]
    )

    print("✅ Added to Chroma")
