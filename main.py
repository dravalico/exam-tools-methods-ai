import sys
from collections import Counter


def count_words_stream(filepath):
    counter = Counter()
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                words = line.lower().split()
                counter.update(words)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        sys.exit(1)
    return counter.most_common()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.txt>")
        return
    freqs = count_words_stream(sys.argv[1])
    for word, count in freqs[:10]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
