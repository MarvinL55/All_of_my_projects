import logging
import os
import shutil
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

source_dir = "C:\\Users\\marvi\\Downloads"
dest_dir_sfx = "C:\\Users\\marvi\\Sound"
dest_dir_music = "C:\\Users\\marvi\\Music"
dest_dir_video = "C:\\Users\\marvi\\Downloads Video"
dest_dir_image = " C:\\Users\\marvi\\Downloads Image"


def makeUnique(path):
    def move(dest, entry, name):
        file_exists = os.path.exists(dest + "/" + name)
        if file_exists:
            unique_name = makeUnique(name)
            os.rename(entry, unique_name)
        shutil.move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_site < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    shutil.move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_video
                elif name.endswith('.jpg') or name.endswith('jpeg') or name.endswith('.png') or name.endswith('.WEBP'):
                    dest = dest_dir_music
                    shutil.move(dest, entry, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
