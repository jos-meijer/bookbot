def get_num_words(text: str):
    num_words = len(text.split())
    return num_words

def get_count_char(text: str):
    count = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in count:
            count[lower_char] += 1
        else:
            count[lower_char] = 1

    return count

def get_sorted_char_list(char_counts):
    char_list = []

    for char, count in char_counts.items():
        if not char.isalpha():
            continue

        char_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list


