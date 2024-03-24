print("Owned By Emin INC.")
print("Google Play Gift Code Generator And Checker 1.0")
import random
import string
import requests

def generate_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=length))
    formatted_code = '.'.join([code[i:i+4] for i in range(0, len(code), 4)])
    return formatted_code

def check_code(code):
    url = f"https://play.google.com/redeem={code}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def main():
    num_codes = int(input("Kaç kod üretmek istiyorsunuz? "))
    code_length = int(input("Her kod kaç haneli olsun? "))

    for _ in range(num_codes):
        generated_code = generate_code(code_length)
        print("Üretilen Kod:", generated_code)
        if check_code(generated_code):
            print("Kod geçerli!")
        else:
            print("Kod geçerli değil!")

if __name__ == "__main__":
    main()
