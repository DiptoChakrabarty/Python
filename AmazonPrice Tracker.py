import requests
from bs4 import BeautifulSoup
# pull individual items of websites

URL="https://www.amazon.in/Grand-Theft-Auto-V-PC/dp/B00LSBDSYA/ref=sr_1_5?keywords=pc+games&qid=1562758220&s=gateway&sr=8-5"
# product to check 
headers= {"User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"}

page=requests.get(URL,headers=headers)
# gets data from website

soup=BeautifulSoup(page.content)

print(soup.prettify)












