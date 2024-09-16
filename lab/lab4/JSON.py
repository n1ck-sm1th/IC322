#Nicholas Smith
#265904

import requests
from bs4 import BeautifulSoup
import json

alpha = input("Please input your alpha: ")
url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"
h = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101Firefox/130.0", 
"Accept":
"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5" ,
"Accept-Encoding": "gzip, deflate, br, zstd" , 
"Content-Type": "application/x-www-form-urlencoded" , 
"Content-Length": "192",
"Origin": "https://mids.usna.edu",
"Connection": "keep-alive",
"Referer": "https://mids.usna.edu/ITSD/mids/drgwq010$.startup",
"Cookie": "f5_cspm=1234; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; WSG$DRGWQ010$URL2=/ITSD/mids/drgwq010$mids.queryview?K_MIDS_ID=75769&K_SECOF_ID=192664&P_ALPHA=&P_LAST_NAME=&P_MICO_CO_NBR=&P_SECOF_COOF_SEBLDA_AC_YR=&P_SECOF_COOF_SEBLDA_SEM=&P_SECOF_COOF_SEBLDA_BLK_NBR=&P_MAJOR_CODE=&P_NOMI_FORMATTED_NAME=&Z_EXECUTE_QUERY=&Z_START=1&Z_ACTION=&Z_CHK=25218; WSG$DRGWQ010$CAP2=Schedule; _ga=GA1.1.1485736831.1725991820; _ga_LY79N0FLBS=GS1.1.1726097850.2.0.1726097852.0.0.0; BIGipServermids_prod=!or5GczShenEThFFHrP/1DhKiDM7x/vxMXV45/13NR5ukSm0f3oLUf3jbcdwpZckJtYEuzJh6YkCJOA==; f5avraaaaaaaaaaaaaaaa_session_=NJGDKONKAGPDJOHNEIDHDGHKBALLPHEBFIMOKACJKLIOAPBKEBJAHKLBENFFHHCMLEODBNCBKLDLBHNACAJAFCNGAIPEJNKDDGENHGHBBPABOBDJHOGOIBANPFDGNFCB; OAMAuthnCookie_mids.usna.edu:443=pDhu6U88La9%2BApB5L5bcyC0keKlBtj%2Fm9sO8kthx7iXOuFeEOZOR55OJGc6QlWSrx5i3L5HiP7NXDJedCVr4uw101rZBVfWP83tgwHpJxnCqHZIuEpVFNcP0as0y%2BHjwOBkw4PzEZhit1h1x8LdhG1TVgF4MDhB%2Fs46lAdNfle51vb7n2ONqOkyNeDkS%2FKiNUl3xeT%2BFJqdQrfYtC2NodyAO4c0FIZjwcsibv8ESczxhRw3P4cPIPwc%2FUvlsEG4ZKyY%2F17H6VixAbqKdzTCbGufdo2miiFbXpMBUQj73WNkzxjLenoWHr%2B2kPMOlS0zKCYgWeSu7LxHIPfyY%2FjbHYGt%2BywksVYyN0YB4Cq%2F%2FcFnQop0i5IkuRx3ny6r7IRqJNXm2C0E3g4rZqvW9I2WnrvQQ66n04i1JNKK9izk%2FW5Rd%2FE325Vhy8ppqXA2yBQDgyeFsXMfpBVsTiT703Aw8sqQkXhRecM5se5qkh7LG%2BcYRKfRL3vOXIhoKeb7cBYqQewn2E9zrczIOwghqAFBOA13qEvFbnbB1GNu0oWlTqNpbKX2sqe4TjzKU32mCl0mZuEZv%2FO%2Fgl%2F0RnRVN5vmOtg%3D%3D",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate" ,
"Sec-Fetch-Site": "same-origin" ,
"Sec-Fetch-User": "?1",
"Priority": "u=0, i"
}

payload = {
  "P_ALPHA": f"{alpha}",
  "P_LAST_NAME": "",
  "P_MICO_CO_NBR": "",
  "P_SECOF_COOF_SEBLDA_AC_YR": "2025",
  "P_SECOF_COOF_SEBLDA_SEM": "FALL",
  "P_SECOF_COOF_SEBLDA_BLK_NBR": "1",
  "P_MAJOR_CODE": "",
  "P_NOMI_FORMATTED_NAME": "",
  "Z_ACTION": "QUERY",
  "Z_CHK": "0" 
}

#Now we are changing it so that we can get information from user input. 
response = requests.post(url, data = payload, headers = h)
htmlData = response.content
#We use our nice data and use the parsing method to extract class, schedules, & 
#instructor names. 
parsedData = BeautifulSoup(htmlData, "html.parser")
elements = parsedData.body.find_all('tr', attrs = {'class':'cgrldatarow'})
#Print out each data element. 
for elem in elements:
  print(elem.text)