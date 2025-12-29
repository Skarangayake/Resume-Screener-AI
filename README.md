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

##  Web App
The project includes a Streamlit-based web interface that allows recruiters to:
- Paste job descriptions
- Automatically rank resumes
- View matched skills
- Download ranked results as CSV



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



# AI Resume Screener

AI-powered resume screening application built with **Streamlit & NLP**.

---

## Live Demo
https://resume-screener-ai-zptqc7brkzfnhgcwk8p9jg.streamlit.app/

---

##  Application Interface
The AI Resume Screener with clean and intuitive interface where users can enter or paste a job description and upload multiple resume files. The layout is designed for simplicity, allowing recruiters to quickly start the screening process with minimal steps.
<img width="938" height="772" alt="Interface" src="https://github.com/user-attachments/assets/fa4a7121-38bc-43eb-87a8-e40addbe10eb" />


##  Result Resumes
After submitting the job description and resume files, the system processes the data and displays the screening results. The output shows which resumes are relevant to the job description along with matched skills, helping users understand how well each resume aligns with the job requirements.
<img width="841" height="755" alt="Result 1" src="https://github.com/user-attachments/assets/c09467b9-b469-474a-be04-d613d5f46823" />

<img width="617" height="679" alt="Result 2" src="https://github.com/user-attachments/assets/ff498680-16c4-4706-bc24-1c424930c98c" />

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
