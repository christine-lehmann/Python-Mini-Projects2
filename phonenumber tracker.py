import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers.phonenumberutil import number_type

num = input("Enter the numebr you want to track the location: ")
phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
carier = carrier.name_for_number(phone, 'en')
registration = geocoder.description_for_number(phone, 'en')

print(phone)
print(time)
print("Company Name: ",carier)
print("Country is: ",registration)
