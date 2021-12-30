import sys
import os

from python_pip_template import main
from colorama import init, Fore, Back, Style 

init(autoreset=True) 

# стартовая точка
def run():
    args = sys.argv[1:]

    # вызов команды без параметров
    if len(args) == 0 or args[0] == '-h' or args[0] == '--help':
        cmd_help()
        return

    # проверка версии
    if args[0] == '-v' or args[0] == '--version':
        cmd_version()
        return

    # do smth useful:)
    if args[0] == '-d' or args[0] == '--do':
        main.doSmthUseful()
        return



# ---- здесь можно реализовывать функции поведения для соответствующих команд
def cmd_help():
    print(Style.BRIGHT + Fore.MAGENTA + 'List of available commands:', end='\n\n')

    print(Style.BRIGHT + Fore.RED + '-h  --help        ', end=''); print('how to use it', end='\n\n')
    print(Style.BRIGHT + Fore.RED + '-v  --version     ', end=''); print('package version', end='\n\n')
    print(Style.BRIGHT + Fore.RED + '-l  --list        ', end=''); print('list of available projects in current catalog and its subcatalogs', end='\n\n')
    print(Style.BRIGHT + Fore.RED + '-d  --do          ', end=''); print('command from main.py', end='\n\n')


def cmd_version():
    print('2021.12.30.0')