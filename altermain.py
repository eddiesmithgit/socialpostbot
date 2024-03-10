import os
import sys
import time
import zipfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import shortcuts as shts
import datetime
import utilfns



directory_path = "images"
extraction_path = "images/eximages"
featured_images_folder = "images/featured_images"
temp_folder = "images/temp"
url="https://business.facebook.com/latest/composer"


# Creating a 2D array with 2 rows and 3 columns
timearr = [['10', '00', 'a'],
       ['08', '30', 'p']]





utilfns.delete_files_in_directory(temp_folder)
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
browser = webdriver.Chrome(options=options)


    # Function to move images from the extraction and featured folders to the temp folder
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

# Check if there are images in the extraction and featured folders
extraction_images = [file for file in os.listdir(extraction_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
featured_images = [file for file in os.listdir(featured_images_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]


start_date = utilfns.getdatefrusr()


if extraction_images or featured_images:
    pscount=int(input('Enter time slot (0/1) :' ))
    if extraction_images or featured_images:
        browser.implicitly_wait(10)
        browser.get(url)
        
        move_images_to_temp(extraction_path, featured_images_folder, temp_folder)
        remfiles = os.listdir(extraction_path)
        if(len(remfiles)<4):
            move_images_to_temp(extraction_path, featured_images_folder, temp_folder)

        browser.switch_to.window(browser.current_window_handle)
        #image uploads
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/span/div/div/div[2]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div").click()
        time.sleep(1)
        temppth=os.path.join(os.getcwd(), temp_folder)
        shts.gofolder(temppth)
        pyautogui.press('enter')
        time.sleep(1)
        shts.slt_all()
        pyautogui.press('enter')

        time.sleep(2)
        #captions
        txtedit=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]")
        txtedit.click()
        txtedit.click()
        time.sleep(1)
        pyautogui.press('esc')
        utilfns.write_to_clipboard(utilfns.get_captions())
        shts.paste()
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)
        #hashtags
        pyautogui.write(utilfns.get_hashtags())


        #Schedule post
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/input").click()
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input").click()
        pyautogui.press('esc')
        time.sleep(2)
        shts.slt_all()
        pyautogui.write(utilfns.get_schedule_date(start_date))
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div/span").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input").click()
        pyautogui.write(timearr[pscount][0])
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/input").click()
        pyautogui.write(timearr[pscount][1])
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/input").click()
        pyautogui.write(timearr[pscount][2])
        time.sleep(1)
        schedulebtn= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div")
        count=0
        while(schedulebtn.value_of_css_property('cursor')!='pointer'):
            time.sleep(5)
            count+=1
            if(count==5):
                print('Unable to Schedule, terminating bot')
                sys.exit(0)
        schedulebtn.click()      
        # increment date
        utilfns.delete_files_in_directory(temp_folder)
        pscount+=1
        
    start_date += datetime.timedelta(days=1)
else:
    print("No images found in the extraction or featured folders.")

    



    # browser.quit()
