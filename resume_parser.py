import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_text):
    doc = nlp(resume_text)
    skills = []
    # Logic to find skills based on a predefined list
    target_skills = ["Python", "SQL", "Data Analysis", "Machine Learning"]
    
    for token in doc:
        if token.text in target_skills:
            skills.append(token.text)
            
    return list(set(skills))

if __name__ == "__main__":
    sample_resume = "I am a Data Analyst skilled in Python and SQL."
    print(f"Extracted Skills: {extract_skills(sample_resume)}")
