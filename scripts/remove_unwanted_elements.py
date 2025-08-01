import re
import sys
from pathlib import Path

def remove_reddit_usernames(text: str) -> str:
    """
    Replace any Reddit username (u/username) with a single space.
    """
    # matches u/ followed by letters, digits, underscores or hyphens
    reddit_pattern = re.compile(r'u/[A-Za-z0-9_-]+')
    return reddit_pattern.sub(' ', text)

def remove_at_entities(text: str, strict: bool = False) -> str:
    """
    Replace any email address or @handle with a single space.
    If strict is False, uses the generic pattern; otherwise uses the stricter one.
    """
    # Option A: generic—remove any non-whitespace chunk that contains '@'
    at_pattern = re.compile(r'\S*@\S+')

    # Option B: stricter—emails OR @usernames
    #   [\w\.-]+@[\w\.-]+\.\w+   matches typical emails
    #   |@\w+                    matches handles like @username
    at_pattern_strict = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+|@\w+')
    
    pat = at_pattern_strict if strict else at_pattern
    return pat.sub(' ', text)

def remove_urls(text: str) -> str:
    """
    Replace any url (starting with https or www) with a single space.
    """
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(' ', text)

def remove_contractions(text: str) -> str:
    """
    Remove any word containing an apostrophe inside of it.
    Catches both common types of aprostrophe (straight and curly).
    e.g. "don't", "l’amour", "d'accord" are removed
    but "'start" or "end’" stay.
    """
    pattern = re.compile(r"\b\w+['’]\w+\b")
    return pattern.sub(" ", text)


def process_file(input_path: str,
                 output_path: str,
                 strict: bool = False) -> None:
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    content = remove_urls(content)
    content = remove_reddit_usernames(content)
    content = remove_at_entities(content, strict=False)
    content = remove_contractions(content)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


if __name__ == "__main__":
     
    if len(sys.argv) < 3:
        print("Usage: python text_merge.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file)