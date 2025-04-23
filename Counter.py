import re

SPAM_WORDS = [
    "free", "win", "click", "offer", "winner", "buy", "limited",
    "guarantee", "urgent", "claim", "prize", "cash", "now", "exclusive",
    "risk-free", "trial", "act now", "credit", "cheap", "save", "instant"
]

def extract_email_features(text):
    words = re.findall(r'\b\w+\b', text)
    total_words = len(words)

    links = len(re.findall(r'(http[s]?://|www\.)\S+', text))

    capital_words = sum(1 for word in words if word.isupper() and len(word) > 1)

    spam_word_count = sum(1 for word in words if word.lower() in SPAM_WORDS)

    return {
        "words": total_words,
        "links": links,
        "capital_words": capital_words,
        "spam_word_count": spam_word_count
    }
