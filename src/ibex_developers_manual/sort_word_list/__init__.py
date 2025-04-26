import os


def read_word_list() -> list[str]:
    with open(os.path.join("doc", "spelling_wordlist.txt"), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def sort_words(words: list[str]) -> list[str]:
    return sorted(words, key=str.casefold)


def write_word_list(words: list[str]) -> None:
    with open(os.path.join("doc", "spelling_wordlist.txt"), "w", encoding="utf-8") as f:
        f.writelines([f"{word}\n" for word in words])
