from pprint import pprint
from dockerfile_parse import DockerfileParser
import logging


logger = logging.getLogger("main.utilities.dockerfile_parser")


def test_parser():
    dfp = DockerfileParser()
    dfp.content = """\
    From  base
    LABEL foo="bar baz"
    USER  me"""

    # Print the parsed structure:
    # pprint(dfp.structure)
    # pprint(dfp.json)
    # pprint(dfp.labels)

    # Set a new base:
    # dfp.baseimage = 'centos:7'

    # Print the new Dockerfile with an updated FROM line:
    # print(dfp.content)


def parse_dockerfile(content):
    dfp = DockerfileParser()
    dfp.content = content

    #pprint(dfp.structure)
    #pprint('-------------------------------------------------------------------------------------------------------------')
    #pprint(dfp.json)
    #pprint(dfp.labels)
    return dfp
