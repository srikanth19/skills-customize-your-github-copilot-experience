# Starter Code: Python Text Processing

from collections import Counter
import re
import string


def read_text_file(file_path):
    """Read and return text from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_for_counting(text):
    """Lowercase text and remove punctuation for cleaner word counts."""
    translation_table = str.maketrans("", "", string.punctuation)
    return text.lower().translate(translation_table)


def text_stats(text):
    """Return character, word, and line counts."""
    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    return characters, words, lines


def most_common_words(text, top_n=5):
    """Return the top N most common words from text."""
    cleaned = normalize_for_counting(text)
    word_list = re.findall(r"\b\w+\b", cleaned)
    return Counter(word_list).most_common(top_n)


def process_text(text):
    """Apply required text transformations and return processed text."""
    lowered = text.lower()
    cleaned_lines = [line.strip() for line in lowered.splitlines()]
    normalized_spaces = [re.sub(r"\s+", " ", line) for line in cleaned_lines]
    return "\n".join(normalized_spaces)


def save_text(file_path, text):
    """Write processed text to an output file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    input_file = "sample.txt"
    output_file = "processed_output.txt"

    text = read_text_file(input_file)

    characters, words, lines = text_stats(text)
    print("Character count:", characters)
    print("Word count:", words)
    print("Line count:", lines)

    print("\nTop 5 words:")
    for word, count in most_common_words(text, top_n=5):
        print(f"{word}: {count}")

    processed = process_text(text)
    save_text(output_file, processed)
    print(f"\nProcessed text saved to {output_file}")


if __name__ == "__main__":
    main()
