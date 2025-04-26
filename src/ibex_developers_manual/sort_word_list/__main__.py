from ibex_developers_manual.sort_word_list import read_word_list, sort_words, write_word_list


def main() -> None:
    words = read_word_list()
    sorted_words = sort_words(words)
    write_word_list(sorted_words)


if __name__ == "__main__":
    main()
