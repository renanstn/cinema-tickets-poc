import string


def default_room_layout():
    return {"cols": 0, "rows": 0}


def alphabet_letters_generator():
    for letter in string.ascii_lowercase:
        yield letter
