import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Sample dataset
data = {
    "skills": [
        "Python Machine Learning Flask",
        "Python SQL Statistics",
        "Java Spring SQL",
        "HTML CSS JavaScript React",
        "Python Deep Learning AI"
    ],

    "job_role": [
        "ML Engineer",
        "Data Scientist",
        "Backend Developer",
        "Frontend Developer",
        "AI Engineer"
    ]
}

df = pd.DataFrame(data)

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["skills"])

y = df["job_role"]

# Train model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

# Save model
pickle.dump(model, open("job_model.pkl", "wb"))

# Save vectorizer
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully")