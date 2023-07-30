import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("path", help="directory containing wav voice files")
parser.add_argument("-d", "--delete-source-files", dest="delete", action="store_true", default=False, help="delete the source files after conversion")
args = parser.parse_args()

path = args.path
deleteSource = args.delete

os.chdir(path)
dirs = os.listdir( path )

for filename in dirs:
    basename, suffix = os.path.splitext(filename)
    print(basename)
    os.system(f"ffmpeg -i '{basename}.wav' -acodec libvorbis '{basename}.ogg'")
    if deleteSource:
        os.remove(filename) 




