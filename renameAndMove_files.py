import os
import time
from watchdog.events import FileCreatedEvent


directory = []

track_input = input("Provide a path for folder to track\n")
destination_input = input("Provide a destination path\n")

folder_to_track = '/Users/Sinan/Desktop/' + track_input
folder_destination = '/Users/Sinan/Desktop/' + destination_input


def move():
    for filename in os.listdir(folder_to_track):
        src = folder_to_track + '/' + filename
        destination = folder_destination + '/' + filename
        file_created = FileCreatedEvent(folder_to_track)
        if file_created:
            os.rename(src, destination)


def rename_files():
    i = 0
    path = 'C:/Users/Sinan/Desktop/test'
    try:
        for filename in os.listdir(path):
            directory.append(filename)
            ex = filename.split('.')[1]
            new_name = 'test_file_' + str(i) + '.' + ex
            source = path + filename
            new_name = path + new_name
            os.rename(source, new_name)
            i += 1
        if len(directory) == 0:
            print("Directory has no file in it.")

    except FileExistsError:
        print("File or files already exists")


if __name__ == '__main__':
    try:
        while True:
            move()
            time.sleep(5)
    except KeyboardInterrupt:
        exit()
