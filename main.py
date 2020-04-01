from utils.csv_util import write_nouns, write_dict_with_counters, write_merged_nouns_list
from utils.dict_util import create_dict_from_csv, merge_nouns_dicts
from utils.dir_util import create_output_directory


out = create_output_directory()

# File with data to perform extraction
input_file = f'input/input.csv'
# Files with extracted ID and noun phrases
out_titles = f'{out}/nouns_title.csv'
out_abstract = f'{out}/nouns_abstract.csv'

# Files with extracted ID and noun phrases + words count
out_titles_count = f'{out}/title_counter.csv'
out_abstract_count = f'{out}/abstract_counter.csv'

# File with merged nouns from Abstract and Title
out_merged = f'{out}/nouns_title_abstract_counts.csv'

# Create csv-files with nouns
write_nouns(input_file, out_titles, 1)
write_nouns(input_file, out_abstract, 4)

# Create dicts with noun phrases and it's occurrences numbers
title_nouns_dict = create_dict_from_csv(out_titles)
abstract_nouns_dict = create_dict_from_csv(out_abstract)

# Write nouns with word counters to csv files
write_dict_with_counters(title_nouns_dict, out_titles_count)
write_dict_with_counters(abstract_nouns_dict, out_abstract_count)

# Create a list with nouns and word occurrences
final_lst = merge_nouns_dicts(title_nouns_dict, abstract_nouns_dict)
# Create a csv-file with final nouns list
write_merged_nouns_list(final_lst, out_merged)
