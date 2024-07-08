from address import Address
from mailing import Mailing

to_address = Address("111222", "Казань", "Максимова", "3", "15")
from_address = Address("100100", "Нижнекамск", "Мира", "30", "145")
mailing = Mailing(to_address, from_address, "350", "QZ25")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house}, {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")