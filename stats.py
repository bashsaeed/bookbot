def get_num_words(text: str) -> int:
    return len(text.split())


def get_char_count(text: str) -> dict[str, int]:
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_dict_by_value(d: dict) -> list[dict[str, int]]:
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
