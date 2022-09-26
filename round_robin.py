import itertools
import os
import shutil
import logging
import sched
import time

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
event_schedule = sched.scheduler(time.time, time.sleep)

def round_robin():
    destination_path = r'/Users/surendra.pandey/Downloads/tmp/test/'
    source_path = r'/Users/surendra.pandey/Downloads/tmp/test/'
    file_list = get_source_file(source_path)
    destination_list = get_destination_dir(destination_path)
    logger.info(f"file list :{file_list}")
    logger.info(f"destination directory list :{destination_list}")

    for file, folder in zip(file_list, itertools.cycle(destination_list)):
        if file is not None:
            shutil.move(source_path+file, destination_path+folder)
            logger.info("move {} to {}".format(file, folder)) 

def get_source_file(source_path):
    # list to store files
    file_list = []
    # Iterate file
    for path in os.listdir(source_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(source_path, path)):
            file_list.append(path)
    return file_list

def get_destination_dir(destination_path):
    # folder path
    destination_folder_list = []
    # Iterate destination folder
    for path in sorted(os.listdir(destination_path)):
        # check if current path is a file
        if os.path.isdir(os.path.join(destination_path, path)):
            print("size of path", path)
            destination_folder_list.append(path)
    return destination_folder_list
    
round_robin()
while True:
    event_schedule.enter(30, 1, round_dobin)
    event_schedule.run()