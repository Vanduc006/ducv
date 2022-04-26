import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
print(Fore.RED + 'some red text', file=stream)
print(Back.GREEN + 'and with a green background', file=stream)
print(Style.RESET_ALL, file=stream)
print('back to normal now', file=stream)