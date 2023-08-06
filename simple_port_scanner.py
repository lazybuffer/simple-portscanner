import socket # for connecting
from colorama import init, Fore

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

# manual text colored
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_port_open(host, port):
    """
    determine whether `host` has the `port` open
    """
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        # return false
        return False
    else:
        # the connection was established, port is open!
        return True

# get the host from the user
host = input("\n[ "+bcolors.HEADER+" # "+bcolors.ENDC+" ] "+bcolors.BOLD+"Enter the host: "+bcolors.ENDC)
# iterate over ports, from 1 to 1024
for port in range(1, int(input("\n[ "+bcolors.HEADER+" # "+bcolors.ENDC+" ] "+bcolors.BOLD+"Range of Port: "+bcolors.ENDC))):
    if is_port_open(host, port):
        print(bcolors.BOLD+bcolors.WARNING+f"\n[ warnning ] {host}:{port} is open", end="\r"+bcolors.ENDC)
    else:
        print(bcolors.BOLD+f"\n{GRAY}[ error ] {host}:{port} is closed", end="\r"+bcolors.ENDC)

