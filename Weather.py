import requests
from bs4 import BeautifulSoup

#Enter city name
city_name = input("Enter city name: ")

#Get the response from Google 
url = "https://www.google.com/search?q="+city_name+"+weather"
response = requests.get(url)

#Parse the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

#Fetch the weather information 
weather_info = soup.find("div",attrs={"class":"BNeawe iBp4i AP7Wnd"}).text

#Print the weather information
print(weather_info)