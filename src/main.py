
import sys
import os

relative_lib_path = os.path.join(os.path.dirname(__file__), '../plugins/greetings-de/src')
lib_path = os.path.abspath(relative_lib_path)
sys.path.append(lib_path)

from text import say_hello


def main():
    say_hello()

main()
