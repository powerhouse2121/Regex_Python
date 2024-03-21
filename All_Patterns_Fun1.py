from PyPDF2 import PdfReader 
import re  

class Pattern_REGEX:
    
    #test_string='L65900MH2016PLC284869 L72400GA2004PLC147094 U74120MH2012PLC230380 '
    #CIN_Number Structure : 1-Listing Status(1-Character) : Listing in stock exchange then i will (L) else (U)
    #2-Industry Code 5-digit
    #3-State Code : 2-Alphabets
    #4-Year Of InCorporation : 4-digits
    #5-Type Of The Company : 3-characters
    #6-Company Registration Number : 6-digits
    #\b[UL]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}
    #In CIN_Pattern, i use list for state_code and company_type that i used in pattern using join method
    #append the result in list result_cin and return the list and count for each page
    #In this pattern,some state_codes are used according to pdf's CIN nos,actually they are not proper cin nos(country_codes : TZ)
    
    def CIN_Pattern(self,text,i):
        try:
            result_cin=[]
            
            state_code=['AN','AP','AD','AR','AS','BH','CH','CT','DN','DD','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LD','MP','MH','MN','ME','MI','NL','OR','PN','PY','PB','RJ','SK','TN','TS','TR','TG','TZ','UP','UT','WB']
            company_type=['FLC','FTC','GAP','GAT','GOI','NPL','PLC','PTC','SGC','ULL','ULT']
            pattern_cin=re.compile(r"[UL]{1}[0-9]{5}(" + "|".join(state_code) + ")[0-9]{4}(" + "|".join(company_type) + ")[0-9]{6}")
            CIN_CODES=pattern_cin.finditer(text)
            cnt=0
            for CIN in CIN_CODES:
                result_cin.append(CIN.group())
                cnt+=1
            return result_cin,cnt
    #        print(f"Count Of CIN in page{i+1} is {cnt}")
            logging.info("Successfully Run CIN_Pattern")
        except Exception as e:
            logging.error(f"Error Occured In CIN_Pattern : {e}")

    #In Mail_Pattern, I use findall() to find all the occurences of mail_pattern in the file
    #append the result in list result_mail and return the list and count for each page
    
    def Mail_Pattern(self,text,i):
        try:
            result_mail=[]
            pattern_mail = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}')
            emails = pattern_mail.findall(text)
            cnt=0
            for email in emails:
                cnt+=1
                result_mail.append(email)
            #print(f"Count Of Mails in page{i+1} is {str(cnt)}")
            return result_mail,cnt
            logging.info("Successfully Run Mail_Pattern")
        except Exception as e:
            logging.error(f"Error Occured In Mail_Pattern : {e}")

    # random_text = """
    #Here are some numbers: (+91)9876543210,+91 9876543210, 011-12345678, 9876543230, +91 98765 43240.
    #But also consider these: 1234-567890, 98765-43220, 01234567890 (012)22222222, (012) 22222222.
    #"""            
    #In Phone_Pattern, checks all the mobile numbers or std code landline phone numbers and checked in the text
    #append the result in list result_phone and return the list and count for each page
    
    def Phone_Pattern(self,text,i):
        try:
            result_phone=[]
            pattern_phone = re.compile(r'\b\(?\+91\)?[\s\S][6789]\d{9}\b|\b(?:\+91|0)?\s[6789]{1}\d{4}[-\s]\d{5}\b|\b[6789]{1}\d{9}|[0-9]{3}[-\s]\d{8}\b|\b\(?[0-9]{3}\)?\s?\d{8}\b')
            phone=pattern_phone.findall(text)
            cnt=0
            for ph in phone:
                cnt+=1
                result_phone.append(ph)
            #print(f"Count Of Phone_Nos in page{i+1} is {str(cnt)}")
            return result_phone,cnt
            logging.info("Successfully Run Phone_Pattern")
        except Exception as e:
            logging.error(f"Error Occured In Phone_Pattern : {e}")

    #In PAN_Pattern, check all the PAN nos in the text using pattern
    #append the result in list result_pan and return the list and count for each page
    
    def PAN_Pattern(self,file_content,i):
        try:
            result_pan=[]
            pattern_pan=re.compile(r'[A-Z]{5}\d{4}[A-Z]')
            Pan=pattern_pan.findall(file_content)
            cnt=0
            for num in Pan:
                result_pan.append(num)
                cnt+=1
            #print(f"Count Of PAN_Nos in page{i+1} is {str(cnt)}")
            return result_pan,cnt
            logging.info("Successfully Run PAN_Pattern")
        except Exception as e:
            logging.error(f"Error Occured In PAN_Pattern : {e}")

    #In Date_Pattern, using the date_pattern iterates all the dates from the text
    #append the result in list result_date and return the list and count for each page
            
    def Date_Pattern(self,text,i):
        try:
            result_date=[]
            pattern=re.compile(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}')

            #pattern1=re.compile(r"\d\d\/(d\d)\/(\d\d\d\d)")
            Dates=pattern.findall(text)
            cnt=0
            for Date in Dates:
                result_date.append(Date)
                cnt+=1
            #print(f"Count Of Dates in page{i+1} is {str(cnt)}")
            return result_date,cnt
            logging.info("Successfully Run Date_Pattern")
        except Exception as e:
            logging.error(f"Error Occured In Date_Pattern : {e}")

    #Retrieve all the websites from text using pattern
    #append the result in list result_websites and return the list and count for each page
    
    def Website_Pattern(self,text,i):
        try:
            result_website=[]
            pattern=re.compile(r'(https?|http?:\/\/)?w{3}\.\S+\.[A-Za-z-_]{2,}')
            websites = pattern.finditer(text)
            cnt=0
            for website in websites:
                result_website.append(website.group())
                cnt+=1
            #print(f"Count Of Websites in page{i+1} is {str(cnt)}")
            return result_website,cnt
            logging.info("Successfully Run CIN_Pattern")
            
        except Exception as e:
            logging.error(f"Error Occured In CIN_Pattern : {e}")
