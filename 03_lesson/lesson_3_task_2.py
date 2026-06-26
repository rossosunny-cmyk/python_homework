from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79001234567"),
    Smartphone("Samsung", "Galaxy S24", "+79007654321"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79005553535"),
    Smartphone("Huawei", "P60 Pro", "+79001112233"),
    Smartphone("Google", "Pixel 8", "+79004445566"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
