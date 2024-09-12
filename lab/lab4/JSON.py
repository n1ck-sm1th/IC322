#Nicholas Smith
#265904

import requests
import json

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
"Cookie": "f5_cspm=1234; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; WSG$DRGWQ010$URL2=/ITSD/mids/drgwq010$mids.queryview?K_MIDS_ID=75769&K_SECOF_ID=192664&P_ALPHA=&P_LAST_NAME=&P_MICO_CO_NBR=&P_SECOF_COOF_SEBLDA_AC_YR=&P_SECOF_COOF_SEBLDA_SEM=&P_SECOF_COOF_SEBLDA_BLK_NBR=&P_MAJOR_CODE=&P_NOMI_FORMATTED_NAME=&Z_EXECUTE_QUERY=&Z_START=1&Z_ACTION=&Z_CHK=25218; WSG$DRGWQ010$CAP2=Schedule; f5avraaaaaaaaaaaaaaaa_session_=JGEGKJGFFBDHHKCCGMONIOBHOEAKEGBKFEDIFHLDOEFFPINMKHDCAEHOHJHLJMELLJODBFOHPKNINMDHPLIAIOLGNDOAHBPLEDJJKENJICOHLLACJEPJIHHAAPLKLAPM; _ga=GA1.1.210712040.1628270994; _ga_LY79N0FLBS=GS1.1.1725563936.33.0.1725563943.0.0.0; nmstat=8f8b7e0d-39de-dca3-e4f0-69fb171ed374; BIGipServermids_prod=!KLc+DaqlDf9OPPlHrP/1DhKiDM7x/gGOc0bJN/2PwH5H2W+Km9Cpb3qNcPML/tFrVpT6bxLqRUfPCXY=; f5avraaaaaaaaaaaaaaaa_session_=LFHJLNKMGLBNCIHPDCCJJAHJLGCOOLOGLJMFKNEGCOPKALBDLLLLCCDDNABNHMCEEEMDABIGAMHJGGNKIHEAKALFHDKCHBFCFKBPHGGJEFDEAFGIOHAAKDEHEGFLDHAG; OAMAuthnCookie_mids.usna.edu:443=AC8xg1KCYzAC4SoADnaZXRC42ejdiiqBGF63ftktg8XMgKpMnzWuW01oFohDJpNwEP033eDJYTG0h6TOebK008ex0BROKbMVDDw1bOdCuAplu9OymxZRrnwXyYrltibBKvmkejC1M1ERTqQLollmJa4z%2B6%2BalnCnHCnFCWimlidGW6EdN4%2FK7R8%2Fi%2Bma%2FaGc%2BMVTqiuZm%2BwWhqz50hdRwPn%2B7DW64O5biGJ1NjU3lOhJ6pHfIpRTv5xh7KNxo%2Flf7Tb%2B54rwSa%2B0hkgS9XTBxWLmxOE8iae5WhFvt5l3Y9XTPV3b5kwYJ%2FwTowcVCrvTSs%2BUiaC8JYK44EtuNj270uNb1Um%2BOd%2BkCfgi0zthfVAZWrrseQHR%2Bqpxevs2jlrxm8MkhgdTR5tIskad%2FdUbsQ03K2fMhhve7DmZePgkGfAl2D4iSViEG7S0FdeY7X4BaBMSL6JOHO4%2F4Feo4%2FsL8MtkUx8uLcpnfsg77M08kqXE%2BbIrVfI9Vc0iiRw7Piab5x9yyxix4SrQPRfp96HQmAKsIAAtxAq0y3SiaoaMGm1i5guIYU5XLIAWqH%2BOdZK90mpYS1OCe1gpa9LotkSMNA%3D%3D" ,
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate" ,
"Sec-Fetch-Site": "same-origin" ,
"Sec-Fetch-User": "?1",
"Priority": "u=0, i"
}

payload = {
  "P_ALPHA": "265904",
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

response = requests.post(url, data = payload, headers = h)
print(response.text)
