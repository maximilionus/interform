from argparse import ArgumentParser, Namespace

from serialix import JSON_Format


# Default dictionary, that will be used later
prog_default_dict = {
    'version': '2020.11'
}


def parse_input_args() -> Namespace:
    """Parse script input arguments with argparse module"""
    arg_parser = ArgumentParser(description='Simple CLI example with serialix package')

    subparsers = arg_parser.add_subparsers(dest='command')

    get_parser = subparsers.add_parser('get', help='get the option value')
    get_parser.add_argument('option', action='store', type=str, help='name of the option to read')

    set_parser = subparsers.add_parser('set', help='set the option value')
    set_parser.add_argument('option', action='store', type=str, help='name of the option')
    set_parser.add_argument('value', action='store', help='value of the option')

    remove_parser = subparsers.add_parser('remove', help='remove the option from configuration file')
    remove_parser.add_argument('option', action='store', type=str, help='name of the option')

    subparsers.add_parser('clear', help='clear the configuration file')

    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_input_args()  # Parse input arguments

    # Prepare the configuration object
    cfg = JSON_Format(
        'settings.json',   # Path to where local file will be located
        prog_default_dict  # Default dictionary, that will be used to
    )                      # fill the file on first creation

    if args.command == 'get':
        # Get value from configuration file with `.get` method.
        # This method works exactly as `dict.get()`, so the second argument
        #     of this function will be returned if key doesn't exist in config.
        value = cfg.get(args.option, 'option does not exist!')
        print(value)

    elif args.command == 'set':
        # Add or overwrite the key in configuration file with value
        cfg[args.option] = args.value
        # Commit the changes to local file
        cfg.commit()

        print('successfully added the new value')

    elif args.command == 'remove':
        # Pop the option from configuration dictionary.
        # This method works exactly as `dict.pop()`, so if the key exists,
        #    it will be removed from dictionary. Second argument of this method will
        #    be returned, if key doesn't exist.
        result = cfg.pop(args.option, None)

        if result is not None:
            # If key exists in configuration dictionary -> commit the changes to local file
            cfg.commit()
            print('successfully removed option "{}" from configuration file'.format(args.option))
        else:
            print('no such option in configuration file!')

    elif args.command == 'clear':
        # Clear the object configuration and commit changes to file
        cfg.clear()
        cfg.commit()
        print('successfully removed everything from configuration file')
