from repy.modules.logger import Logger
from repy.modules.argparser import parse_args

if __name__ == "__main__":
    args = parse_args()
    logger_manager = Logger(verbose=args.verbose, logfile=args.logfile)
    clog, flog = logger_manager.get_loggers()
    clog.debug(args)

    status = "enabled" if args.verbose else "disabled"
    color = "green" if args.verbose else "red"
    clog.info(f"Debug logging is [{color}]{status}[/{color}].")
