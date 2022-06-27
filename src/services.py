
keywords = ["checkpoint", "avanan", "email", "security"]


def handle_event(text: str) -> dict[str, int]:
    data = {}
    for word in text.lower().split():
        if word in keywords:
            data[word] = data.get(word, 0) + 1
    return data


