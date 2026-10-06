# import os.path, time
# print(time.ctime(os.path.getatime("test.txt")))
# print(time.ctime(os.path.getctime("text.txt")))
import os
import time

file_path = "example.txt"

# Get modification time
mod_time_raw = os.path.getmtime(file_path)
print("Last modified:", time.ctime(mod_time_raw))

# Get creation time (Windows) or last metadata change time (Linux)
creation_time_raw = os.path.getctime(file_path)
print("Created/Metadata changed:", time.ctime(creation_time_raw))