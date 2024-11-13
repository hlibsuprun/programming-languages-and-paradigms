import re
from collections import Counter

text = """Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji analizy tekstu.
Tekst ten powinien zliczać liczbę słów, zdań i akapitów, a także wykluczać stop words i transformować niektóre wyrazy."""
stop_words = {"i", "a", "the", "to", "w", "z", "na", "o", "że", "jest", "się", "wtedy", "ale"}


def count_elements(text):
    paragraphs = [p for p in text.split('\n') if p.strip()]
    paragraph_count = len(paragraphs)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    return paragraph_count, sentence_count, word_count


def process_words(text):
    words = re.findall(r'\b\w+\b', text)
    processed_words = [
        word[::-1] if word.lower().startswith('a') else word
        for word in words if word.lower() not in stop_words
    ]
    word_counter = Counter(processed_words)
    return word_counter.most_common(10)


def analyze_text(text):
    paragraph_count, sentence_count, word_count = count_elements(text)
    most_common_words = process_words(text)
    result = (
            f"Number of paragraphs: {paragraph_count}, Number of sentences: {sentence_count}, Number of words: {word_count}\n"
            f"Most common words: " + ", ".join([f"{word}: {count}" for word, count in most_common_words])
    )
    print(result)


analyze_text(text)
