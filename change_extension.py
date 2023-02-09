import os

path = r"path/to/directory" # replace this with the actual path to the directory

# get a list of all files in the directory
files = os.listdir(path)

# iterate through the list of files
for file in files:
    # get the file name and extension
    file_name, file_extension = os.path.splitext(file)
    
    # check if the file extension is ".MP4"
    if file_extension == ".MP4":
        # create the new file name
        new_file_name = file_name + ".mp4"
        
        # create the old and new file paths
        old_file_path = os.path.join(path, file)
        new_file_path = os.path.join(path, new_file_name)
        
        # change the file extension
        os.rename(old_file_path, new_file_path)
