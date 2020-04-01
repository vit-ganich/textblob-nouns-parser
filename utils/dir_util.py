import os


def create_output_directory(folder='output') -> str:
    """
    Creates a directory for all output csv files
    :param folder: dir name
    :return: string directory name
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder


if __name__ == '__main__':
    pass
