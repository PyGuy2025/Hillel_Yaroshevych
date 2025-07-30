def correct_sentence(text: str) -> str:
    result = text[0].upper() + text[1:]
    if result.endswith("."):
        return result
    else:
        return result + '.'