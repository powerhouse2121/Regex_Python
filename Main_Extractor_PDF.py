from All_Patterns_Functions import Pattern_REGEX
from PyPDF2 import PdfReader 
import json
from selenium import webdriver
import time
import logging
import logger_file
import pandas as pd

class regex_main_function:
    """This is Regex main class"""
    #Call load_config function
    def __init__(self,config_file="config_regex.json"):    
        self.config=self.load_config(config_file)

    #load_config(config_file) : It includes config_file to load     
    def load_config(self,config_file):          
        with open(config_file) as config_file:
            return json.load(config_file)

    #download_pdf() function : I use the selenium package to download PDF file using url
    #and store in passed directory
    #To download PDF,i use webdriver.get(url) of particular url

    #Here i put sleep function,because it takes more than a second to download when we not use sleep() method then it will not download
    #i split the strings with / because i want file_name then i iterate -1
    #then i append to the list file_names
    #Change default directory for downloads
    #Retrieve base_urls from config_regex.json file
        
    def download_pdf(self):
        try:
            file_names=[]
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {
            "download.default_directory": "D:\\Python Files\\Python_New_REGEX", 
            #"download.prompt_for_download": False,  #Do not download
            #"download.directory_upgrade": True,    #To auto download the file
            "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome 
            })
            
            driver = webdriver.Chrome(options=options)
            #pdf_url = 'https://assets.airtel.in/teams/simplycms/web/docs/Draft-Annual-Return-FY-2021-22.pdf'
            for pdf_url in self.config["base_urls"]:
                driver.get(pdf_url)
                time.sleep(10)
                files=pdf_url.split("/")
                file=files[-1]
                file_names.append(file)
            return file_names
    
            logging.info("Successfully Downloaded All The Files")
            
        except Exception as e:
            logging.error(f"Error in downloading : {e}")

    #In main() function, Call to download_pdf() and get the result as a list of files and iterate one by one
    #fisrtly i get empty lists for all the functions to append the returned result page-wise
    #and display all the lists with their cnt for each page
    #In all functions,they returns 2 values - matched_patterns and count of each page of matched pattern
    #It returns in list within a tuple because i use unpacking method
            
    def main(self):
        try:
            files=self.download_pdf()
            dict1={}
            for file in files:
                print(f"\n\n-----------------------------------------This is {file}-----------------------------------------")

##                all_CIN=[]
##                all_Mails=[]
##                all_Phones=[]
##                all_PANS=[]
##                all_Dates=[]
##                all_Websites=[]
                
                reader = PdfReader(file) 
                no_of_pages=self.config["no_of_pages"]
                for i in range(no_of_pages):
                    print(f"\nPage No: {i+1}\n")
                    page = reader.pages[i]   
                    
                    text = page.extract_text()

                    dict1={
                        "CIN_Nos":Pat.CIN_Pattern(text,i),        
                        "Mail_IDs":Pat.Mail_Pattern(text,i),
                        "Phone_Nos":Pat.Phone_Pattern(text,i),
                        "PAN_Nos":Pat.PAN_Pattern(text,i),
                        "All_Date":Pat.Date_Pattern(text,i),
                        "All_Websites":Pat.Website_Pattern(text,i)}

                    print(dict1)
                    
                #df=pd.DataFrame()
##                print("\nAll CIN Nos : \n",all_CIN)
##                #print("All CIN Count : \n",len(all_CIN))
##            
##                print("\nAll MailID's : \n",all_Mails)
##                print("\nAll Phone Nos : \n",all_Phones)
##                print("\nAll PAN Nos : \n",all_PANS)
##                print("\nAll Dates : \n",all_Dates)
##                print("\nAll Websites : \n",all_Websites)
##                
            logging.info(f"Successfully Run All {files}")                    
        except Exception as e:
            logging.error(f"Error Occured In {file} : {e}")
                
        
if __name__=="__main__":
    Pat=Pattern_REGEX()

    main_class=regex_main_function()
    main_class.main()
    



