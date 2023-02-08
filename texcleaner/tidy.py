"""Tidy module.
"""
import glob
import os


def move_files(text_file, figure_path, archive_directory):
    with open(text_file, "r") as f:
        texts = f.read().splitlines()

    figure_paths = glob.glob(figure_path + "/*")

    exists_list = []
    for figure_path in figure_paths:
        exists = False
        for text in texts:
            if os.path.basename(figure_path) in text:
                exists = True
                break
        exists_list.append(exists)
    not_exists_list = [not t for t in exists_list]

    figure_paths_to_move = [x for i, x in enumerate(figure_paths)
                            if not_exists_list[i]]

    for path in figure_paths_to_move:
        basename = os.path.basename(path)
        os.rename(path, os.path.join(archive_directory, basename))
