

# Install the required libraries
!pip install sentence-transformers numpy scikit-learn matplotlib plotly
# Basic imports
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "I love programming in Python",
    "Python is a great programming language",
    "I enjoy cooking Italian food",
    "Pasta is my favorite Italian dish",
    "Machine learning is fascinating",
    "I prefer fried momos over regular",
    "Pubg Game is not interesting one anymore",
    "Labrador's are friendly dogs",
    "The sun rises in the east every morning",
    "Watching movies is my favorite weekend activity",
    "Reading novels helps me relax after work",
    "Basketball is more exciting than cricket to me",
    "I like to listen to music while studying",
    "Traveling to new places inspires creativity",
    "Online shopping is convenient but addictive",
    "Cloud computing is changing the tech industry",
    "Healthy eating habits improve your lifestyle",
    "Gardening is a peaceful hobby for many people",
    "Chocolate ice cream is better than vanilla",
    "Learning a new language is a great challenge",
    "Social media can be both helpful and harmful",
    "I find math puzzles really engaging",
    "Walking in the rain is a unique experience",
    "The Himalayas are breathtakingly beautiful",
    "My dog loves playing fetch in the park",
    "Mobile games help me pass the time on commutes",
    "Robotics will shape the future of automation",
    "Photography captures memories forever",
    "Group projects teach teamwork and patience",
    "Summer vacations are always memorable"
]

# Generate embeddings
embeddings = model.encode(sentences)
print(f"Shape of embeddings: {embeddings.shape}")
print(f"First embedding (truncated): {embeddings[0][:10]}...")

def calculate_similarity_matrix(sentences, embeddings):
    """Calculate cosine similarity between all pairs of sentences"""
    similarity_matrix = cosine_similarity(embeddings)

    # Create a readable similarity report
    print("Semantic Similarity Matrix:")
    print("-" * 60)

    for i, sent1 in enumerate(sentences):
        for j, sent2 in enumerate(sentences):
            if i < j:  # Only show upper triangle to avoid duplicates
                similarity = similarity_matrix[i][j]
                print(f"'{sent1[:30]}...' vs '{sent2[:30]}...': {similarity:.3f}")

    return similarity_matrix

# Calculate similarities
similarity_matrix = calculate_similarity_matrix(sentences, embeddings)

def get_closest_match(sentence, embeddings):
    ls = []

    sentence = model.encode([sentence])
    sentence = np.squeeze(sentence)
    sentence = sentence.reshape(1, 384)
    print(sentence.shape)
    for emb in embeddings:
        emb=emb.reshape(1, 384)
        print(emb.shape)
        similarity = cosine_similarity(sentence, emb)
        ls.append(similarity[0][0])

        #rint(sentence, "versus", emb, similarity)
    print(ls)
    return sentences[ls.index(max(ls))]

get_closest_match("pubg",embeddings)

