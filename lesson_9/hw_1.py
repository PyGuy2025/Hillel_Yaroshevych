from collections import Counter


def popular_words(text:str, words:list) -> dict:
    words_dict = Counter(text.lower().split())
    result = {word: words_dict.get(word, 0) for word in words}
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')