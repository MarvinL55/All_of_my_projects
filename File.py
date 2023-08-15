import os


def find_files_on_desktop():
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    print("Files on your desktop:")

    for filename in os.listdir(desktop_path):
        if os.path.isfile(os.path.join(desktop_path, filename)):
            print(filename)


if __name__ == "__main__":
    find_files_on_desktop()
