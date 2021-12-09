Mountains = {"Mount Everest": "8848", "K2": "8611", "Kangchenjunga": "8586", "Lhotse": "8516", "Makalu": "8485"}

for key_name, value_name in Mountains.items():
    print(key_name) # The key is stored in whatever you called the first variable.

for key_name, value_name in Mountains.items():
    print(value_name) # The value associated with that key is stored in your second variable.

for key_name, value_name in Mountains.items():
    print(key_name + " is " + value_name + " meters tall.")
