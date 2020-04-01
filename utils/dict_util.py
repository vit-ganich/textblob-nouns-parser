from collections import defaultdict

from utils.csv_util import read_file


def create_dict_from_csv(nouns_csv: str) -> dict:
    """
    Get list [[ID, noun], [ID, noun]] and convert it to dict {ID: [noun, noun]}
    :param nouns_csv: list [ID, noun]
    :return: dict {ID: [noun, noun]}
    """
    nouns_list = read_file(nouns_csv)
    nouns_dict = convert_list_to_dict(nouns_list)
    return count_words_in_dict(nouns_dict)


def merge_nouns_dicts(title: dict, abstract: dict) -> list:
    """
    Get two dicts like {ID:[noun:count, noun:count]} and merge them
    :param title: first dict
    :param abstract: second dict
    :return: merged dict
    """
    result = []
    for key_t in title.keys():
        if key_t in abstract.keys():
            for item_t in title[key_t]:
                item_t = item_t.split(':')
                for item_a in abstract[key_t]:
                    item_a = item_a.split(':')
                    if item_t[0] == item_a[0]:
                        result.append([key_t, item_t[0], item_t[1], item_a[1]])
                    else:
                        result.append([key_t, item_a[0], item_t[1], 0])
        else:
            items_t = title[key_t]
            for item in items_t:
                item = item.split(':')
                result.append([key_t, item[0], 0, item[1]])
        for key_a in abstract.keys():
            if key_a not in title.keys():
                items_a = abstract[key_a]
                for item in items_a:
                    item = item.split(':')
                    result.append([key_a, item[0], 0, item[1]])

    return result


def convert_list_to_dict(nouns_list: list) -> dict:
    """
    Get list with lists with ID and noun.
    Convert to dictionary
    :param nouns_list: list like [ID, noun]
    :return: dictionary like {ID: [noun, noun]}
    """
    template = {'': []}
    for item in nouns_list:
        if item[0] not in template.keys():
            template[item[0]] = [item[1]]
        else:
            template[item[0]].append(item[1])
    return template


def count_words_in_dict(nouns: dict) -> dict:
    """
    Counts each word occurrence and adds ':<number>' to each word
    :param nouns: dictionary with words
    :return: modified dictionary like {ID: [word:count, word:count]}
    """
    for key in nouns.keys():
        value = []
        for item in nouns[key]:
            count = nouns[key].count(item)
            value.append(f'{item}:{count}')
        nouns[key] = list(set(value))
    return nouns


def merge_dicts(first: dict, second: dict) -> dict:
    """
    Get two dictionaries and merge them
    :param first: first dict
    :param second: second dict
    :return: merged dict
    """
    merged = defaultdict(list)
    for d in (first, second):
        for key, value in d.items():
            merged[key].append(value)
    return merged


if __name__ == '__main__':
    pass
