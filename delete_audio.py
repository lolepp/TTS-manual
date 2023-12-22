import os

# Directories where audio files are located
libs = ["audio/wav/", "audio/mp3/"]

# List all files in the directory
for lib in libs:
    file_list = os.listdir(lib)

    # Iterate through the files and delete files
    for file in file_list:
        if file.endswith(".wav") or file.endswith(".mp3"):
            file_path = os.path.join(lib, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
