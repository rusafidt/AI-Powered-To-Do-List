import spacy

# Load spaCy's small English model (includes tokenizer, POS tagger, lemmatizer, etc.)
nlp = spacy.load("en_core_web_sm")

# Define categories and the keywords that hint at them
CATEGORIES = {
    "Shopping": ["buy", "purchase", "order", "milk", "grocery", "shop"],
    "Work": ["email", "report", "meeting", "project", "deadline"],
    "Health": ["exercise", "run", "gym", "doctor", "medicine"],
    "Personal": ["call", "visit", "family", "friend", "birthday"],
}

def auto_tag(task: str) -> str:
    """
    Assign a simple category tag to a task description.
    Uses keyword matching with spaCy lemmatization 
    (so 'buying' matches 'buy', 'ran' matches 'run', etc.)
    """
    # Convert text to spaCy Doc (tokenized + lemmatized)
    doc = nlp(task.lower())
    
    # Check each token in the task
    for token in doc:
        # See if the lemmatized form matches any category keywords
        for category, keywords in CATEGORIES.items():
            if token.lemma_ in keywords:
                return category  # Return first matching category
    
    # If no keyword matched, fallback to "Other"
    return "Other"


# Demo usage
if __name__ == "__main__":
    tasks = [
        "Buy milk and bread",
        "Finish project report",
        "Go to the gym",
        "Call mom about birthday",
        "Book flight tickets"
    ]

    for t in tasks:
        print(f"Task: {t} → Tag: {auto_tag(t)}")
