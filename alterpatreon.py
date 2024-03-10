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
url="https://www.patreon.com/posts/new?postType=image_file"

content_type=int(input("Enter content type \n 0.SFW\n1.NSFW\n"))
# Creating a 2D array with 2 rows and 3 columns
timearr = ['10:00','20:30']



# Delete all files in the extraction folder
utilfns.delete_files_in_directory(extraction_path)

# Delete all files in the "featured_images" folder
utilfns.delete_files_in_directory(featured_images_folder)

# Delete all files in the "temp" folder
utilfns.delete_files_in_directory(temp_folder)


# Get a list of files in the directory
files = os.listdir(directory_path)

# Filter for files with a .zip extension
zip_files = [file for file in files if file.endswith(".zip")]

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
    
    filenumber= 4 if(content_type==0) else 10
    start_date = utilfns.getdatefrusr()

    if extraction_images or featured_images:
        pscount=int(input('Enter time slot (0/1) :' ))
        if extraction_images or featured_images:
            browser.implicitly_wait(10)
            browser.get(url)
            time.sleep(2)
            utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder,filenumber)
            remfiles = os.listdir(extraction_path)
            if(len(remfiles)<10):
                utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder,filenumber)
            utilfns.add_prefix_to_files(temp_folder)
            browser.switch_to.window(browser.current_window_handle)
            browser.maximize_window()

            pyautogui.press('esc')
            pyautogui.press('space')
            time.sleep(2)
            #captions
            titletxt=['SFW Pack '+str(pscount)+' of '+start_date.strftime('%d/%m/%Y') ,'NSFW Pack '+ start_date.strftime('%d/%m/%Y')]
            titleedit=browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[2]/input")
            titleedit.click()
            pyautogui.write(titletxt[content_type])
            time.sleep(1)
            titleedit.click()
            txtedit=browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div").click()
            utilfns.write_to_clipboard(utilfns.get_captions())
            shts.paste()
            time.sleep(2)

            #tags
            tags=["art,aiart,digitalart,sfw,earlyaccess,pack","art,aiart,digitalart,nsfw,ignsfwvariations,pack"]
            browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[4]/div[2]/div/div/div[2]/div/input").click()
            pyautogui.write(tags[content_type])
            time.sleep(2)


            #image uploads
            pyautogui.press('esc')
            browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/button").click()
            time.sleep(2)
            temppth=os.path.join(os.getcwd(), temp_folder)
            shts.gofolder(temppth)
            pyautogui.press('enter')
            time.sleep(1)
            shts.slt_all()
            pyautogui.press('enter')

            

            #nextbtn
            browser.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/main/div[1]/div/div/div/div/nav/div[1]/div[2]/div[2]/button").click()
            time.sleep(2)

            #paid members
            browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[3]/button").click()
            browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/h3").click()
            pyautogui.press('space')

            #Schedule post
            browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div/div[1]/div[5]/div/div/div/div/button").click()
            time.sleep(3)
            #date
            dvalue=start_date.strftime('%Y-%m-%d')
            datex = "/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div/div[1]/div[5]/div/div/div/div[2]/div[1]/div/div/div/input"
            browser.execute_script("date = document.evaluate('"+datex+"', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;   date.value='"+dvalue+"'")
            
            #time
            timex = "/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div/div[1]/div[5]/div/div/div/div[2]/div[2]/div/div/div/input"
            browser.execute_script("date = document.evaluate('"+timex+"', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;   date.value='"+timearr[pscount]+"'")

            schedulebtn= browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/nav/div[1]/div[2]/div[2]/button")
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
