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

instfrn="Follow my fellow AI artists -\n@plankcba\n@lazyart007\n@silents.ai\n@thelargestbrasize\n@darkarts._.ai\n@im.ai.gin.ai.tion\n@shinybabes.ai\n@rdf.ai.art"

directory_path = "images"
extraction_path = "images/eximages"
featured_images_folder = "images/featured_images"
temp_folder = "images/temp"
url="https://publish.buffer.com/calendar/week"


# Creating a 2D array with 2 rows and 3 columns




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
    
    

    while extraction_images or featured_images:
        if extraction_images or featured_images:
            browser.implicitly_wait(10)
            browser.get(url)
            
            utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder,3)
            remfiles = os.listdir(extraction_path)
            browser.switch_to.window(browser.current_window_handle)
            time.sleep(2)
            pyautogui.press('esc')
            time.sleep(2)
            browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div[2]/div/main/header/span/div[4]/div/button").click()
            time.sleep(2)
            #captions
            time.sleep(1)
            utilfns.write_to_clipboard(utilfns.get_captions())
            shts.paste()
            pyautogui.press('enter')
            time.sleep(1)
            #hashtags
            pyautogui.write(utilfns.get_hashtags(6))

            time.sleep(2)

            
            #image uploads
            browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div[2]/section[3]/div/div/div[1]/div[1]/div[2]/div/div/button").click()
            time.sleep(1)
            temppth=os.path.join(os.getcwd(), temp_folder)
            shts.gofolder(temppth)
            pyautogui.press('enter')
            time.sleep(1)
            shts.slt_all()
            pyautogui.press('enter')

            #schedule 
            schedulebtn=browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div[2]/section[3]/div/div/div[1]/div[1]/div[2]/div/div/button")
            time.sleep(2)
            count=0
            while(schedulebtn.value_of_css_property('cursor')!='pointer'):
                time.sleep(5)
                count+=1
                if(count==5):
                    print('Unable to Schedule, terminating bot')
                    sys.exit(0) 
            time.sleep(2)
            #customise for each network
            browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div[2]/section[4]/div/button").click()
            
            #edit insta caption
            time.sleep(2)
            browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div[2]/section[3]/div[2]/div[1]").click()
            shts.slt_all()
            utilfns.write_to_clipboard(utilfns.get_captions())
            shts.paste()
            pyautogui.press('enter')
            time.sleep(1)
            #mentons
            utilfns.write_to_clipboard(instfrn)
            shts.paste()
            pyautogui.press('enter')
            time.sleep(1)
            #hashtags
            pyautogui.write('#model '+utilfns.get_hashtags(3)+' #eddieartsai')
            # pyautogui.write('#model #eddieartsai #fashion #hollywood #candidphotography')
            time.sleep(2)
           
            #add queue
            browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div[2]/section[4]/div/div[2]/div/div/div/button/div").click()      
            time.sleep(7)
            # increment date
            utilfns.delete_files_in_directory(temp_folder)
            
        extraction_images = [file for file in os.listdir(extraction_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        featured_images = [file for file in os.listdir(featured_images_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    else:
        print("No images found in the extraction or featured folders.")

        



        # browser.quit()
else:
    print("No .zip files found in the directory.")
