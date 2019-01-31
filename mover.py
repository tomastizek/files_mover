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
    arg_parser.add_argument("--operation", help="all - sort files by type and move it to corresponding folder,"
                                                "one - sort files with entered type and move in to destination folder")
    return arg_parser.parse_args()


def move_file(type, source, dest):

    try:
        os.makedirs("{}".format(dest))
    except:
        print("folder already exist")

    for file in tqdm(glob.glob("{}/*{}".format(source, type))):
        shutil.move(file, "{}".format(dest))
    print("{} files was moved successfully".format(type))


def sort_and_move(source, dest):

    list_of_dirs = []

    for d in os.listdir(source):
        list_of_dirs.append(d.split(",")[-1].split(".")[1])
    for dir in list_of_dirs:
        try:
            os.makedirs("{}/{}s".format(dest, dir))
        except:
            print("folder allready exist")

        for f in tqdm(glob.glob("{}/*{}".format(source,dir))):
            shutil.move(f, "{}/{}s".format(dest, dir))
        print("files was moved successfully")


def main():

    args = parse_args()

    type = args.type
    source = args.source
    dest = args.dest
    operation = args.operation

    if operation =="all":
        sort_and_move(source, dest)
    elif operation == "one":
        move_file(type, source, dest)
    else:
        print("wrong operation")


if __name__ == "__main__":
    main()




