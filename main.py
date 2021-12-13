#firstly pip install phonenumbers in terminal, then import it in program as below
import phonenumbers
#create a test.py file and add number with country code then import number
from test import number
#import genercode from phonenumber
from phonenumbers import geocoder
#CH here C stands for country and H stands for history
ch_number = phonenumbers.parse(number, "CH")
#this will print the location of the number
print(geocoder.description_for_number(ch_number,"en"))
#for knowing the service provider import carrier from phonenumbers
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number,"en"))