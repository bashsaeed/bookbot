from stats import get_num_words, get_char_count, sort_dict_by_value


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as file:
        return file.read()


def generate_report(path_to_file: str) -> None:
    book_text: str = get_book_text(path_to_file)
    num_words: int = get_num_words(book_text)
    num_chars: dict = get_char_count(book_text)
    sorted_chars: list[dict[str, int]] = sort_dict_by_value(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main() -> None:
    path_to_file = "books/frankenstein.txt"
    generate_report(path_to_file)


main()
