from os import path
from argparse import ArgumentParser, Namespace

from . import JSON_Format

try:
    from . import YAML_Format
    yaml_imported = True
except ImportError:
    yaml_imported = False

try:
    from . import TOML_Format
    toml_imported = True
except ImportError:
    toml_imported = False


def convert(from_path: str, from_format: str, dest_path: str, dest_format: str):
    """Convert files between any supported languages

    :param from_path: Path to the file to be converted
    :type from_path: str
    :param from_format: format of the file to be converted
    :type from_format: str
    :param dest_path: desired path to converted file
    :type dest_path: str
    :param dest_format: desired file format
    :type dest_format: str
    """
    from_object = __generate_interform_object(from_path, from_format)
    dest_object = __generate_interform_object(dest_path, dest_format)

    if from_object is not None and dest_object is not None:
        dest_object.dictionary = from_object.dictionary
        dest_object.commit()

        return 'successfully converted "{}" from "{}" to "{}" and saved the result to "{}"'.format(
            path.basename(from_path),
            from_format,
            dest_format,
            dest_path
        )

    else:
        return 'conversion failed, check the output above'


def parse_args() -> Namespace:
    parser_main = ArgumentParser(
        description='command line interface tool for "interform"'
    )
    subparsers = parser_main.add_subparsers(dest='command')

    parser_converter = subparsers.add_parser('convert', help='tool to convert files of supported languages')
    parser_converter.add_argument('from_path', action='store', type=str, help='path to the file to be converted')
    parser_converter.add_argument('from_format', action='store', type=str, help='format of the file to be converted')
    parser_converter.add_argument('dest_path', action='store', type=str, help='desired path to converted file')
    parser_converter.add_argument('dest_format', action='store', type=str, help='desired file format')

    return parser_main.parse_args()


def start():
    args = parse_args()

    if args.command == 'convert':
        print(convert(
            args.from_path, args.from_format,
            args.dest_path, args.dest_format
        ))


def __generate_interform_object(file_path: str, file_lang: str) -> object:
    obj = None

    # TODO: Check for file existance
    if file_lang == 'json':
        obj = JSON_Format(file_path)
    elif file_lang == 'yaml' and yaml_imported:
        obj = YAML_Format(file_path)
    elif file_lang == 'toml' and toml_imported:
        obj = TOML_Format(file_path)
    else:
        print('language "{}" for file "{}" is not supported'.format(file_lang, file_path))

    return obj


if __name__ == "__main__":
    start()
