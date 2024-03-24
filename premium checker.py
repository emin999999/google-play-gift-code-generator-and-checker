print("Owned By Emin INC.")
print("Google Play Gift Codes Generator And Checker Premium")
import random
import string
import requests

def generate_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    formatted_code = '-'.join([code[i:i+4] for i in range(0, len(code), 4)])
    return formatted_code

def check_code(code):
    url = f"https://play.google.com/redeem?code={code}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def generate_and_check_codes(num_of_codes):
    for _ in range(num_of_codes):
        code = generate_code()
        print(f"Üretilen Kod: {code}")
        if check_code(code):
            print("Bu kod geçerli.")
        else:
            print("Bu kod geçersiz.")

# Kullanıcı girişi
num_of_codes = int(input("Kaç adet kod üretmek istiyorsunuz? "))

generate_and_check_codes(num_of_codes)
