import csv

from utils.parse_util import extract_noun_phrases
from utils.regex_util import extract_article_id


def read_file(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        return [row for row in rows if row]


def write_merged_nouns_list(final_list: list, output_file: str, encoding='utf-8'):
    """
    Method writes list of nouns from Title and Abstracts with words counts
    :param output_file: csv-file to write merged list
    :param final_list:  merged list with nouns
    :param encoding:    default - utf-8
    """
    with open(output_file, 'w', encoding=encoding, newline='') as out_csv_file:
        csv_writer = csv.writer(out_csv_file, delimiter=',')
        csv_writer.writerow(['Article ID', 'Noun Phrase', 'FoundInTitle', 'FoundInAbstract'])
        for row in final_list:
            csv_writer.writerow(row)


def write_nouns(in_file: str, out_file: str, cell_num_to_extract: int):
    """
    Extracts nouns from specified cell of the input csv file
    :param in_file:  csv file with raw data
    :param out_file: file with extracted nouns
    :param cell_num_to_extract: number of cell with nouns to extract
    """
    with open(in_file, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        with open(out_file, 'w', encoding='utf-8', newline='') as out_csv_file:
            csv_writer = csv.writer(out_csv_file, delimiter=',')
            # csv_writer.writerow(['Article ID', 'Noun Phrase'])
            for row in rows:
                if not row:
                    continue
                article_id = extract_article_id(row[0])
                if not article_id:
                    continue

                print('Processing for article ID: %s' % article_id)

                noun_phrases = extract_noun_phrases(row[cell_num_to_extract])
                print('Total noun phrases found: %d' % len(noun_phrases))

                for noun_phrase in noun_phrases:
                    csv_data = [str(article_id), ','.join(noun_phrase.split(' '))]
                    csv_writer.writerow(csv_data)


def write_dict_with_counters(input_dict: dict, file: str):
    """
    Write to csv file the dictionary with nouns and occurrence counts
    :param input_dict: dictionary with nouns and occurrence counts
    :param file: csv file to write data
    """
    with open(file, 'w', encoding='utf-8', newline='') as out_csv_file:
        csv_writer = csv.writer(out_csv_file, delimiter=',')
        csv_writer.writerow(['Article ID', 'Noun Phrase', 'Count'])
        for key, value in input_dict.items():
            for item in value:
                # Remove unnecessary duplicated title
                if key == 'Article ID':
                    continue
                item = item.split(':')
                csv_writer.writerow([key, item[0], item[1]])


if __name__ == '__main__':
    pass
