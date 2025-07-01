import sys
from collections import defaultdict


def load_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().lower()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{path}': {e}")
        sys.exit(1)


def count_words(text):
    dict_counter = defaultdict(int)
    spitted_text = text.split()
    for word in spitted_text:
        dict_counter[word] += 1
    return sorted(dict_counter.items(), key=lambda x: x[1], reverse=True)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.txt>")
        return
    text = load_text(sys.argv[1])
    freqs = count_words(text)
    for word, count in freqs[:10]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
