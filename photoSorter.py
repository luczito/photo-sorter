# Small script to rename all photos in a folder to the date they were taken for QOL.
# Extracts metadata to rename each file.
import json
import os
from PIL import Image, ExifTags
from datetime import datetime

errorCounter = 0
successCounter = 0

# load folder wiht photos
print("Enter path to folder containing photos.")
path = input()

files = os.listdir(path)
# loop over each photo
for file_name in files:
    file_path = os.path.join(path, file_name)

    if os.path.isfile(file_path):
        try:
            # Open the image file
            with Image.open(file_path) as img:
                # Get metadata
                exif = img.getexif()
                if exif:
                    # Make a map with tag names
                    exif = { ExifTags.TAGS[k]: v for k, v in exif.items() if k in ExifTags.TAGS and type(v) is not bytes }
                    print(json.dumps(exif, indent=4))
                    # Grab the date
                    date_obj = datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
                    print(date_obj)
                    successCounter += 1
                    print("Successfully renamed file, total successes: ", successCounter)
                else:
                    errorCounter += 1
                    print("Error extracting metadata, total errors: ", errorCounter)
        except Exception as e:
            print("Error, cant find file")