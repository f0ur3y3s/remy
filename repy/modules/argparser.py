import argparse


def range_limited_port(arg) -> int:
    min_port = 1025
    max_port = 65535

    try:
        port = int(arg)

        if min_port <= port <= max_port:
            return port
        else:
            raise argparse.ArgumentTypeError(
                f"Port must be between {min_port} and {max_port} (inclusive). Got {port}."
            )
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid port number: {arg}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )

    parser.add_argument(
        "-l",
        "--logfile",
        type=str,
        default="default.log",
        help="Specify the log file name for file logging. Will not duplicate console logging.",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=range_limited_port,
        default=1337,
        help="Specify the port for the server.",
    )

    parser.add_argument(
        "-a",
        "--address",
        type=str,
        default="127.0.0.1",
        help="Specify the address for the server.",
    )

    return parser.parse_args()
