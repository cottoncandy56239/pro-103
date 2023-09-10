import sys
import os
import shutil
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_directory = "/Users/mridinikulkarni/Downloads"
to_directory = "/Users/mridinikulkarni/c103"

dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
            "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
            "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileEventHandler(FileSystemEventHandler):
    def on_created (self, event):
        print('Hey, ' + {event.src_path} + 'has been created!')
    def on_deleted (self, event):
        print('Oops, someone deleted ' + {event.src_path}) 
    def on_moved (self, event):
        print('Moving ' + {event.src_path} + '...')    
    def on_modified (self, event):
        print({event.src_path} + 'is being modified')

    
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_directory, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print('running...')
except KeyboardInterrupt:
    print('stopped!')
    observer.stop()