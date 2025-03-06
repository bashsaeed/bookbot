def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as file:
        return file.read()


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    path_to_file = "books/frankenstein.txt"
    book_text: str = get_book_text(path_to_file)
    num_words: int = count_words(book_text)
    print(f"{num_words} words found in the document")


main()
