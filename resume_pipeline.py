import os
import pandas as pd
from preprocess import clean_text
from similarity import embed_text, calculate_similarity

def rank_resumes(job_text, resume_folder):
    job_clean = clean_text(job_text)
    job_vec = embed_text(job_clean)

    results = []

    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            path = os.path.join(resume_folder, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                resume_text = f.read()

            resume_clean = clean_text(resume_text)
            resume_vec = embed_text(resume_clean)

            score = calculate_similarity(job_vec, resume_vec)
            results.append([file, round(score, 4)])

    df = pd.DataFrame(results, columns=["Resume", "Similarity_Score"])
    df = df.sort_values(by="Similarity_Score", ascending=False)
    return df