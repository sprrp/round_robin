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
    destination_path = r'test/'
    source_path = r'test/'
    file_list = get_source_file(source_path)
    destination_list = get_destination_dir(destination_path)
    logger.info(f"File list :{file_list}")
    logger.info(f"estination directory list :{destination_list}")

    for file, folder in zip(file_list, itertools.cycle(destination_list)):
        if file is not None:
            shutil.move(source_path+file, folder)
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

# def get_destination_dir(destination_path):
#     # folder path with sorted empty destination folder
#     destination_folder_list = []
#     # Iterate destination folder
#     for path in sorted(os.listdir(destination_path)):
#         # check if current path is a file
#         if os.path.isdir(os.path.join(destination_path, path)):
#             logger.info("size of path", path)
#             destination_folder_list.append(path)
#     data = []
#     for i in destination_folder_list:
#         data_list = {}
#         No_of_files = len([entry for entry in os.listdir(destination_path+i) if os.path.isfile(os.path.join(destination_path+i, entry))])
#         if No_of_files == 0:
#             data.append(destination_path+i)
#     logger.info(f"list of sorted destination {data}")
#     return data


def get_destination_dir(destination_path):
    # folder path with sorted destination output
    destination_folder_list = []
    # Iterate destination folder
    for path in sorted(os.listdir(destination_path)):
        # check if current path is a file
        if os.path.isdir(os.path.join(destination_path, path)):
            print("size of path", path)
            destination_folder_list.append(path)
    data = []
    for i in destination_folder_list:
        data_list = {}
        No_of_files = len([entry for entry in os.listdir(destination_path+i) if os.path.isfile(os.path.join(destination_path+i, entry))])
        data_list["destination"] = destination_path+i
        data_list["no_files"] = No_of_files
        data.append(data_list)
    data.sort(key=lambda x: x['no_files'], reverse=False)
    logger.info(f"sorted destination: {data}")
    sorted_destination = [data[i]["destination"] for i in range(len(data))]
    logger.info(f"list of sorted destination {sorted_destination}")
    return sorted_destination

    
round_robin()
while True:
    event_schedule.enter(30, 1, round_robin)
    event_schedule.run()
