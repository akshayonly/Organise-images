# Importing libraries
import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

# Path which contain images
current_path = '/home/akshayonly/Pictures/TestFolder/'


os.chdir(current_path)

successful = 0
unsuccessful = 0


for file in os.listdir():
    
    file_name, file_extension = os.path.splitext(file)
    
    if file_extension.lower() == '.jpg' or file_extension.lower() == '.jpeg':
                
        image = Image.open(file)

        exif_data = image.getexif()

        for tag_id in exif_data:
            tag_info = TAGS.get(tag_id, tag_id)
            image_data = exif_data.get(tag_id)
            
            if isinstance(image_data, bytes):
                image_data = image_data.decode(errors='ignore')
                
            if tag_info == 'DateTimeOriginal':
                date_time = image_data[:10]
                image_year = date_time[:4]
                image_month = date_time[5:7]
                
        month_dictionary = {'01': 'January',
                    '02': 'February',
                    '03': 'March',
                    '04': 'April',
                    '05': 'May',
                    '06': 'June',
                    '07': 'July',
                    '08': 'August',
                    '09': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'}

        combine_path = image_year + '/' + month_dictionary[image_month] + '-' + image_year

        shifting_path = os.path.join(current_path, combine_path)

        try: 
            os.makedirs(shifting_path, exist_ok = True) 
            successful += 1
            
        except OSError as error: 
            print(f"Directory '{shifting_path}' can not be created") 
            unsuccessful += 1

        source = current_path + '/' + file

        moved_file = shutil.move(source, shifting_path)


print(f"Failed: {unsuccessful}")
print(f"Successful:{successful}")

