from stats import get_num_words, get_char_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as file:
        return file.read()


def main() -> None:
    path_to_file = "books/frankenstein.txt"
    book_text: str = get_book_text(path_to_file)
    num_words: int = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    num_chars: dict = get_char_count(book_text)
    print(num_chars)


main()
