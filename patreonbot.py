import os
import sys
import time
import zipfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import shortcuts as shts
import datetime
import utilfns
from selenium.webdriver.common.action_chains import ActionChains



directory_path = "images"
extraction_path = "images/eximages"
featured_images_folder = "images/featured_images"
temp_folder = "images/temp"
url="https://www.patreon.com/posts/new?postType=image_file"

content_type=int(input("Enter content type \n 0.SFW\n1.NSFW\n"))
# Creating a 2D array with 2 rows and 3 columns
timearr = [['02', '00', 'pm'],
       ['04', '45', 'pm']]



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
    actions = ActionChains(browser)

        # Function to move images from the extraction and featured folders to the temp folder
    

    # Check if there are images in the extraction and featured folders
    extraction_images = [file for file in os.listdir(extraction_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    featured_images = [file for file in os.listdir(featured_images_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    filenumber= 3  
    start_date = utilfns.getdatefrusr()
    prelease_date = start_date + datetime.timedelta(days=1)

    while extraction_images:
        pscount=  0 if content_type==0 else 1 
        
        browser.implicitly_wait(10)
        browser.get(url)
        time.sleep(2)
        utilfns.move_images_to_temp(extraction_path, featured_images_folder, temp_folder,filenumber)
        remfiles = os.listdir(extraction_path)
        utilfns.add_prefix_to_files(temp_folder)
        browser.switch_to.window(browser.current_window_handle)
        browser.maximize_window()

        pyautogui.press('esc')
        pyautogui.press('space')
        time.sleep(2)

        
        #captions
        titletxt=['SFW Pack of '+start_date.strftime('%d/%m/%Y') ,'NSFW Pack '+ start_date.strftime('%d/%m/%Y')]
        titleedit=browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[2]/input")
        titleedit.click()
        pyautogui.write(titletxt[content_type])
        time.sleep(1)
        titleedit.click()
        txtedit=browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[2]/div/div[3]/div/p").click()
        utilfns.write_to_clipboard(utilfns.get_captions())
        shts.paste()
        time.sleep(2)

        #tags
        tags=["art,aiart,digitalart,sfw,earlyaccess,pack","art,aiart,digitalart,nsfw,ignsfwvariations,pack"]
        browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/input").click()
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
        time.sleep(6)

        #nextbtn
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/main/div[1]/div/div/div/div/nav/div[1]/div[2]/div[2]/button").click()
        time.sleep(2)

        #paid members
        # browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[3]/button").click()
        browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/h3").click()
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('space')
        time.sleep(1)

        if(content_type==0):
            # SFW Content

            #early access
            pyautogui.click(x=1127, y=370) #- tg button
            time.sleep(3)

            #date
            day = prelease_date.strftime("%d")
            month = prelease_date.strftime("%m")
            year = prelease_date.strftime("%Y")
            pyautogui.click(x=563, y=450) #- day
            pyautogui.write(day)
            pyautogui.click(x=590, y=450) #- month
            pyautogui.write(month)
            pyautogui.click(x=622, y=450) #- year
            pyautogui.write(year)
            time.sleep(2)

            #time
            pyautogui.click(x=842, y=450) #- hour
            pyautogui.write(timearr[pscount][0])
            pyautogui.click(x=862, y=450) #- mins
            pyautogui.write(timearr[pscount][1])
            pyautogui.click(x=890, y=450) #- AM/PM
            pyautogui.write(timearr[pscount][2])




            #Schedule post
            pyautogui.click(x=1121, y=550) #- tg button
            time.sleep(3)

            #date
            day = start_date.strftime("%d")
            month = start_date.strftime("%m")
            year = start_date.strftime("%Y")
            pyautogui.click(x=563, y=605) #- day
            pyautogui.write(day)
            pyautogui.click(x=590, y=605) #- month
            pyautogui.write(month)
            pyautogui.click(x=622, y=605) #- year
            pyautogui.write(year)
            time.sleep(2)

            #time
            pyautogui.click(x=842, y=605) #- hour
            pyautogui.write(timearr[pscount][0])
            pyautogui.click(x=862, y=605) #- mins
            pyautogui.write(timearr[pscount][1])
            pyautogui.click(x=890, y=605) #- AM/PM
            pyautogui.write(timearr[pscount][2])
        
        elif(content_type==1):
            #NSFW Content

            #Schedule post
            pyautogui.click(x=1121, y=475) #- tg button
            time.sleep(3)

            #date
            day = start_date.strftime("%d")
            month = start_date.strftime("%m")
            year = start_date.strftime("%Y")
            pyautogui.click(x=563, y=530) #- day
            pyautogui.write(day)
            pyautogui.click(x=590, y=530) #- month
            pyautogui.write(month)
            pyautogui.click(x=622, y=530) #- year
            pyautogui.write(year)
            time.sleep(2)

            #time
            pyautogui.click(x=842, y=530) #- hour
            pyautogui.write(timearr[pscount][0])
            pyautogui.click(x=862, y=530) #- mins
            pyautogui.write(timearr[pscount][1])
            pyautogui.click(x=890, y=530) #- AM/PM
            pyautogui.write(timearr[pscount][2])

        
        time.sleep(5)
        schedulebtn= browser.find_element(By.XPATH,"/html/body/div/div/div[4]/div/main/div[1]/div/div/div/div/nav/div[1]/div[2]/div[2]/button")
        count=0
        while(schedulebtn.value_of_css_property('cursor')!='pointer'):
            time.sleep(5)
            count+=1
            if(count==5):
                print('Unable to Schedule, terminating bot')
                sys.exit(0)
        time.sleep(2)
        schedulebtn.click()      
        # increment date
        utilfns.delete_files_in_directory(temp_folder)
        
        time.sleep(10)
        browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/button").click()
        time.sleep(5)
            
        start_date += datetime.timedelta(days=1)
        prelease_date = start_date + datetime.timedelta(days=1)
        extraction_images = [file for file in os.listdir(extraction_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    else:
        print("No images found in the extraction or featured folders.")

        



        # browser.quit()
else:
    print("No .zip files found in the directory.")
utilfns.delete_files_in_directory(temp_folder)