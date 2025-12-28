# Resume Screener AI 🤖📄

An AI-powered Resume Screening System that ranks resumes against a job description using **NLP**, **Sentence Transformers**, and **skill matching**.

---

##  Features
- Semantic resume ranking using transformer embeddings
- Skill-based keyword matching
- Cleaned & preprocessed text using NLP
- Resume ranking exported to CSV
- Visual comparison of top resumes
- Jupyter Notebook based implementation

---

##  Tech Stack
- Python
- spaCy
- Sentence Transformers
- Scikit-learn
- Pandas
- Matplotlib


---


---

## ⚙️ How It Works
1. Load job description
2. Preprocess resumes
3. Convert text to embeddings
4. Calculate similarity score
5. Extract matched skills
6. Rank resumes
7. Export results to CSV

---

## Output Example
| Resume | Similarity Score | Matched Skills |
|------|------------------|---------------|
| resume1.txt | 0.24 | Python, NLP |
| resume2.txt | 0.21 | SQL, Cloud |

---




#  PUSH CODE TO GITHUB (COMMANDS)

Open terminal **inside project folder** and run:

```bash
git init
git add .
git commit -m "Initial commit: AI Resume Screener"
git branch -M main
git remote add origin https://github.com/Skarangayake/Resume-Screener-AI.git
git push -u origin main

## ▶️ Run the Project
```bash
pip install -r requirements.txt
jupyter notebook resume_screener.ipynb
