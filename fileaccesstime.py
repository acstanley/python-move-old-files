import os
import stat
import time
import datetime
from pathlib import Path
import shutil

# share folder with all files
rootdir = "E:\\Migrate\\"

# new folder to create and move archived files to
copy_to_dir = "E:\\Filesthatarearchived\\"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        full_path = os.path.join(subdir, file)
        fileStatsObj = os.stat(full_path)
        dateAccessTime = datetime.datetime.strptime(time.ctime(fileStatsObj[stat.ST_ATIME]),
                                                    "%a %b %d %H:%M:%S %Y")
        if dateAccessTime < datetime.datetime(2020, 12, 30):
        #if dateAccessTime < datetime.datetime.now() - datetime.timedelta(days=365):
            os.makedirs(os.path.dirname(full_path.replace(rootdir, copy_to_dir)), exist_ok=True)
            shutil.move(full_path, full_path.replace(rootdir, copy_to_dir))
            print("Archived:", full_path.replace(rootdir, copy_to_dir))

for dirpath, dirnames, filenames in os.walk(rootdir, topdown=False):
    if not dirnames and not filenames:
        print(dirpath + " is empty, deleting")
        os.rmdir(dirpath)
        

