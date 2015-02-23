import argparse

from .app import app
from .version import __version__

"""
    A server for providing the app anywhere, no need for GAE
"""


def main():
    desc = """
           The youtube-dl API server.
           """

    parser = argparse.ArgumentParser(description=desc)

    default_port = 9191
    port_help = 'The port the server will use. The default is: {}'
    port_help = port_help.format(default_port)
    parser.add_argument('-p', '--port',
                        default=default_port,
                        type=int,
                        help=port_help
                        )

    default_host = 'localhost'
    host_help = 'The host the server will use. The default is: {}'
    host_help = port_help.format(default_host)
    parser.add_argument('-h', '--host',
                        default=default_host,
                        type=str,
                        help=host_help
                        )

    parser.add_argument('--version', action='store_true',
                        help='Print the version of the server')

    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)

    app.run(args.host, args.port)
