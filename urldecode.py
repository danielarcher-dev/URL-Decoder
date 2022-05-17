from ast import parse
from distutils.command.clean import clean
from urllib.parse import unquote
import argparse


def clean_url(encoded_string):
    clean_url = unquote(encoded_string)

    return clean_url


def main():


    # do work
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', help="this is the string to URL decode", required=True)

    args = parser.parse_args()

    print(clean_url(args.a))

if __name__ == "__main__":
    main()
