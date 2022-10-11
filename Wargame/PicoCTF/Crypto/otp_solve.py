from pwn import *

conn = remote('mercury.picoctf.net', 41934)
print(conn.recvuntil('What data would you like to encrypt?'))

remaining_bytes = 50000-32 # flag 는 32바이트? (flag 64줄.. hex 값.. -> 32바이트?)
i = 1
while remaining_bytes >= 1000:
    print('[+] Sending 1000 bytes ... ')
    conn.send('a' * 1000 + '\n')
    remaining_bytes -= 1000
    print("stage : ", i)
    conn.recvuntil('What data would you like to encrypt?')
    i += 1

# for문 빠져나왔다면 remaining_bytes 는 0~1000 바이트 아닌가..?
print('[+] Sending {} bytes ... '.format(remaining_bytes)) #
conn.send('a' * remaining_bytes + '\n')
print(conn.recvuntil('What data would you like to encrypt?'))

print('Key Offset is at 0. Sending bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...')
conn.send('b' * 32 + '\n')
print(conn.recvuntil('What data would you like to encrypt?'))

conn.close()
print("Done.")
