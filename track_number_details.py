import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

#Enter number
number=input("Enter the phone number with country code:")
phoneNumber =phonenumbers.parse(number)
##for time zone
timeZone=timezone.time_zones_for_number(phoneNumber)
print("timezone:"+str(timezone))
##for location

geolocation=geocoder.description_for_number(phoneNumber,"en")
print("location:"+geolocation)
## for services provider
services=carrier.name_for_number(phoneNumber,"en")
print("services provider:"+services)
