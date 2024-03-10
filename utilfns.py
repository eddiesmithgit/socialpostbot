import datetime
import os
import random
import shutil
import subprocess
from datetime import datetime, timedelta
import zipfile
def get_hashtags(lenth=28):
    try:
        file_path='hastags.txt'
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into a list of words
            words = content.split()

            # Ensure that there are at least 30 words in the file
            if len(words) < lenth:
                raise ValueError("The file should contain at least 30 words.")

            # Randomly select 30 words
            random_words = random.sample(words, lenth-5)

            # Join the selected words into a string
            result_string = ' '.join(random_words)
            result_string += ' '+'#patreon'+' '+'#patreonmodel'+' '+'#eddieartsai'

            return result_string
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


    
def get_captions():
    try:
        file_path='captions.txt'
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into a list of sentences
            sentences = [sentence.strip() for sentence in content.split('\n\n') if sentence]

            # Ensure that there are at least 1 sentence in the file
            if len(sentences) < 1:
                raise ValueError("The file should contain at least 1 sentence.")

            # Randomly select 1 sentence
            random_sentence = random.choice(sentences)

            return random_sentence
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

# Replace 'your_file.txt' with the path to your text file



def getdatefrusr():
    user_input = input("Enter a date from which you want to start scheduling (dd-mm-yyyy): ")
    input_format = "%d-%m-%Y"
    # output_format = "%m/%d/%Y"
    current_date = datetime.strptime(user_input, input_format)
    return current_date

def get_schedule_date(dt):
    output_format = "%m/%d/%Y"
    return dt.strftime(output_format)



def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


def delete_files_in_directory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def move_images_to_temp(extraction_folder, featured_folder, temp_folder, num_extraction=4):
        # Move the first 'num_extraction' images from the extraction folder to temp folder
        extraction_files = os.listdir(extraction_folder)[:num_extraction]
        for filename in extraction_files:
            source_path = os.path.join(extraction_folder, filename)
            destination_path = os.path.join(temp_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} from extraction folder to temp folder")

        # Move one image from the featured folder (if exists) to the temp folder
        featured_files = os.listdir(featured_folder)
        if featured_files:
            source_path = os.path.join(featured_folder, featured_files[0])
            destination_path = os.path.join(temp_folder, featured_files[0])
            shutil.move(source_path, destination_path)
            print(f"Moved {featured_files[0]} from featured folder to temp folder")

def mv_to_folders(zip_files,directory_path,extraction_path,featured_images_folder):
    # Get the path of the first .zip file
    first_zip_path = os.path.join(directory_path, zip_files[0])
    print("Path of the first .zip file:", first_zip_path)
    with zipfile.ZipFile(first_zip_path, 'r') as zip_ref:
        # Specify the directory where you want to extract the contents
        zip_ref.extractall(extraction_path)
        print(f"Contents of {first_zip_path} extracted to {extraction_path}")

    extracted_files = os.listdir(extraction_path)
    files_to_move = [file for file in extracted_files if file.startswith("0am")]
    if files_to_move:
    # Create the "featured_images" folder if it doesn't exist
        if not os.path.exists(featured_images_folder):
            os.makedirs(featured_images_folder)

        # Move the files to the "featured_images" folder
        for file_to_move in files_to_move:
            source_path = os.path.join(extraction_path, file_to_move)
            destination_path = os.path.join(featured_images_folder, file_to_move)
            shutil.move(source_path, destination_path)
    else:
        print("No files starting with '0am' found in the extracted folder.")

def add_prefix_to_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.startswith('0am'):
            # Skip files starting with '0am'
            continue
        
        # Construct the new filename by adding '1' as a prefix
        new_filename = '1' + filename
        
        # Get the full paths for the old and new filenames
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)

test ="test\ntest"
write_to_clipboard(test)