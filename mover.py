import os
import shutil
import glob
import argparse
from tqdm import tqdm


def parse_args():
    """
        Parse and return arguments.
    """
    arg_parser = argparse.ArgumentParser(prog="files_mover")
    arg_parser.add_argument("--type", help="type of files, which should be moved")
    arg_parser.add_argument("--source", help="source path")
    arg_parser.add_argument("--dest", help="destination path")
    return arg_parser.parse_args()


def move_file(type, source, dest):

    try:
        os.makedirs("{}".format(dest))
    except:
        print("folder already exist")

    for file in tqdm(glob.glob("{}/*{}".format(source, type))):
        shutil.move(file, "{}".format(dest))
    print("{} files was moved successfully".format(type))


def main():

    args = parse_args()

    type = args.type
    source = args.source
    dest = args.dest

    move_file(type, source, dest)


if __name__ == "__main__":
    main()




