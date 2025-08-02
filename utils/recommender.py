from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_text, jobs_collection, top_n=5):
    jobs = list(jobs_collection.find())
    job_texts = [job['description'] for job in jobs]
    titles = [job['title'] for job in jobs]

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(job_texts + [resume_text])
    similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()

    top_indices = similarity.argsort()[-top_n:][::-1]
    return [{"title": titles[i], "score": round(similarity[i]*100, 2)} for i in top_indices]
