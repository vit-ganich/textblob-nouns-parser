from textblob import TextBlob


def extract_noun_phrases(text: str) -> TextBlob:
    """
    Extract noun phrases via TextBlob
    :param text: text to perform extraction
    :return: extracted noun phrases
    """
    blob = TextBlob(text)
    return blob.noun_phrases


if __name__ == '__main__':
    pass
