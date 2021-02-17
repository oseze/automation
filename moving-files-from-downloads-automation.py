#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:25:18 2020

@author: osezeiyore
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folderorigin):
            src = folderorigin + "/" + filename
            new_destination = folderdestination + "/" + filename
            os.rename(src, new_destination)

folderorigin = "/Users/osezeiyore/Desktop/myFolder" 
folderdestination = "/Users/osezeiyore/Desktop/myFolder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folderorigin, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()