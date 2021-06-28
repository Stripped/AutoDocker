import logging
import os

import utilities.dockerfile_parser as dockerfile_parser
import utilities.dockerfile_reader as dockerfile_reader
import utilities.visualizer as visualizer


def commandline_parser():
    pass


def setup_logger():
    format_type = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
    logging.basicConfig(format=format_type, filename='application.log', encoding='utf-8')
    logger = logging.getLogger('main')
    logger.setLevel(10)
    return logger


def main():
    logger = setup_logger()
    logger.info("Main started")
    path = os.path.join(os.getcwd(), "sources_dockerfiles")
    dockerfile_parser.test_parser()
    list_docker = dockerfile_reader.get_dockerfiles(path)
    dict_docker = dockerfile_reader.add_to_list_dockerfiles(list_docker, path)

    base_image_info = []

    for key, value in dict_docker.items():
        # print(key, ' : ', value)
        dockerfile_parser.parse_dockerfile(value)
        base_image_info.append(dockerfile_parser.parse_dockerfile(value).baseimage)

    #visualizer.test_visualize()
    #visualizer.visualize_base_images(base_image_info)
    #visualizer.create_base_image_table(base_image_info)


if __name__ == '__main__':
    main()
