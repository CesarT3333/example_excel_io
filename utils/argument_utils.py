import constans
from entity.configuration import Configuration

import argparse

import exception


def process_arguments(configuration: Configuration):
    parser = argparse.ArgumentParser()

    parser.add_argument("--env", "-e", help="set environment")
    parser.add_argument("--inputFile", "-i", help="set input file path")

    args = parser.parse_args()

    if args.env:
        configuration.env = args.env

    if args.inputFile:
        configuration.input_file_path = args.inputFile
    else:
        raise exception.MandatoryArgumentError(constans.ARGUMENT_INPUT_FILE_MANDATORY_ERROR)
