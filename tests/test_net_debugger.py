from bugjar.net import Debugger
from bugjar.main import local, ArgumentParser
from collections import namedtuple
import argparse
import pytest


@pytest.mark.skip()
@pytest.fixture
def local_setup():
    "Run a Bugjar session on a local process"
    parser = ArgumentParser(
        description='Debug a python script with a graphical interface.',
    )

    parser.add_argument(
        "-p", "--port",
        metavar='PORT',
        help="Port number to use for debugger communications (default=3742)",
        action="store",
        type=int,
        default=3742,
        dest="port"
    )

    parser.add_argument(
        'filename',
        metavar='script.py',
        help='The script to debug.'
    )
    parser.add_argument(
        'args', nargs=argparse.REMAINDER,
        help='Arguments to pass to the script you are debugging.'
    )

    options = parser.parse_args()

    # Start the program to be debugged
    proc = subprocess.Popen(
        ["bugjar-net", options.filename] + options.args,
        stdin=None,
        stdout=None,
        stderr=None,
        shell=False,
        bufsize=1,
        close_fds='posix' in sys.builtin_module_names
    )
    # Pause, ever so briefly, so that the net can be established.
    time.sleep(0.1)

    # Create a connection to the debugger instance
    debugger = Debugger('localhost', options.port, proc=proc)
    Return_Args = namedtuple('Return_Args', ['hostname', 'port', 'proc'])
    return_args = Return_Args(options.hostname, options.port, None)
    return return_args


@pytest.mark.skip
@pytest.mark.timeout(10)
def test_import(local_setup):
    args = local()
    debugger = Debugger(args.hostname, args.port, args.proc)
