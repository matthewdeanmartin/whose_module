# noinspection PyPep8
"""whose_module/StackOverflow Pip
Not associated with PyPA, nor StackOverflow.

Usage:
  whose_module <folder>
  whose_module (-h | --help)
  whose_module --version

Options:
  -h --help                    Show this screen.
  -v --version                 Show version.
  --verbose                    Show logging
  --quiet                      No informational logging

"""
import logging
import sys

import docopt

from whose_module import _version as meta

# from whose_module import settings as settings

# Do these need to stick around?
LOGGERS = []

LOGGER = logging.getLogger(__name__)


def main() -> int:
    """Get the args object from command parameters"""
    arguments = docopt.docopt(__doc__, version=f"whose_module {meta.__version__}")
    print(arguments)
    LOGGER.debug(arguments)
    return 0


if __name__ == "__main__":
    sys.exit(main())
