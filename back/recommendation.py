import pickle

model = pickle.load(open("job_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def recommend_jobs(skills):

    # Convert list to text
    text = " ".join(skills)

    X = vectorizer.transform([text])

    prediction = model.predict(X)

    return prediction.tolist()