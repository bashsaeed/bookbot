def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as file:
        return file.read()
def main() -> None:
    path_to_file = "books/frankenstein.txt"
    book_text: str = get_book_text(path_to_file)
main()
