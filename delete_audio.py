import os

# Directory where WAV files are located
lib = "audio/"

# List all files in the directory
file_list = os.listdir(lib)

# Iterate through the files and delete WAV files
for file in file_list:
    if file.endswith(".wav"):
        file_path = os.path.join(lib, file)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
