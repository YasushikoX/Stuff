import os

folder = r"path/to/directory" # Path to the folder where you want to delete sonthing

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if filename.endswith('.LRV'): # What ever you want to delete
            os.unlink(file_path)
    except Exception as e:
        print(f'Failed to delete {file_path}: {e}')
