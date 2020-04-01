import re


def extract_article_id(text: str) -> str:
    """
    Extract article ID
    :param text: line with raw article
    :return: article
    """
    article_id = __parse_single_text(r'(?i)(\d+)', text)
    return article_id


def __parse_single_text(pattern: str, text: str) -> re:
    match = re.search(pattern, text)
    if match and len(match.groups()) > 0:
        return match.group(1)
    return ''


if __name__ == '__main__':
    pass
