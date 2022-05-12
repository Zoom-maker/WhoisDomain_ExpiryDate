import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# The class of the domain
class PendantDomain:

    def __init__(self, name, expiry_date):

        self.name = name
        self.expiry_date = expiry_date


# Using the modul bs4 extract the information we require.
def expiry_date(domain_name = 'google.com'):

    count = 0

    url = "https://www.whois.com/whois/" + domain_name

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find_all('div', class_='df-label')
    exp_date = soup.find_all('div', class_='df-value')

    for n in name:

        for d in exp_date:

            if n.text == 'Expires On:':
                count += 1

                if count == 4: return d.text


domain_info = input("Enter the domain name (example.com): ")
domain = PendantDomain(domain_info, expiry_date(domain_info))

print("\nThe domain text is: " + domain.name + "\nThe domain expire on: " + str(domain.expiry_date))