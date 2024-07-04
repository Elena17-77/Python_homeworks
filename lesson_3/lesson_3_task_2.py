from smartphone import Smartphone

catalog = []

phone1 = Smartphone("samsung", "A71", "89063157575")
phone2 = Smartphone("infinix", "Hot40", "89271112233") 
phone3 = Smartphone("honor","X8A", "89045789885")
phone4 = Smartphone("redmi", "10C", "89600111111")
phone5 = Smartphone("xiaomi", "13T", "89374565233")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
   print(f"{phone.brand} - {phone.model}. {phone.phone_number}")