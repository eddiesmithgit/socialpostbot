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




# Delete all files in the extraction folder
utilfns.delete_files_in_directory(extraction_path)

# Delete all files in the "featured_images" folder
utilfns.delete_files_in_directory(featured_images_folder)

# Delete all files in the "temp" folder
utilfns.delete_files_in_directory(temp_folder)


# Get a list of files in the directory
files = os.listdir(directory_path)

# Filter for files with a .zip extension
zip_files = [file for file in files if file.endswith(".zip") and file == "sfw.zip"]


# Check if there are any .zip files
if zip_files:
    # Get the path of the first .zip file
    utilfns.mv_to_folders(zip_files,directory_path,extraction_path,featured_images_folder)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    browser = webdriver.Chrome(options=options)
    

        # Function to move images from the extraction and featured folders to the temp folder
    

    # Check if there are images in the extraction and featured folders
    extraction_images = [file for file in os.listdir(extraction_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    featured_images = [file for file in os.listdir(featured_images_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    
    start_date = utilfns.getdatefrusr()

    if extraction_images or featured_images:
        pscount=int(input('Enter time slot (0/1) :' ))
        if extraction_images or featured_images:
            browser.implicitly_wait(10)
            browser.get(url)
            
            utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder)
            remfiles = os.listdir(extraction_path)
            if(len(remfiles)<4):
                utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder)

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
else:
    print("No .zip files found in the directory.")
