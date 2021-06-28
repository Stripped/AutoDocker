import os
import codecs
import logging


logger = logging.getLogger("main.utilities.dockerfile_parser")


def get_dockerfiles(path_to_dir):
    docker_list = os.listdir(path_to_dir)
    return docker_list


def get_dockerfiles_content(path_to_file):
    try:
        contents = codecs.open(path_to_file, "r", "utf-8")
        data = contents.read()
        contents.close()
    except IOError as e:
        logger.error("problem with file :"+path_to_file)
        logger.exception("Received error:", e.data)
    return data


def add_to_list_dockerfiles(list_files, path_to_main_dir):
    docker_dict = {}
    for file in list_files:
        try:
            docker_dict[file] = get_dockerfiles_content(os.path.join(path_to_main_dir, file))
        except IOError as e:
            logger.error("Received error:", e.data)
    return docker_dict
