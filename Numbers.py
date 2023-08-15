import phonenumbers
from myNumbers import number
from phonenumbers import geocoder, carrier

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
region = carrier.name_for_number(pepnumber, "en")
print(location)
print(region)