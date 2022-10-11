'''
import wasmtime.loader
import assembly4
import string
import itertools
def init_flag(pair):
   for i in range(len(flag)):
      assembly4.memory.data_ptr[1072+i]=ord(flag[i])
   for j in range(len(flag_so_far)):
      assembly4.memory.data_ptr[1072+8+j]=ord(flag_so_far[j])
   assembly4.memory.data_ptr[1072+8+len(flag_so_far)]=ord(pair[0])
   assembly4.memory.data_ptr[1072+8+len(flag_so_far)+1]=ord(pair[1])

def print_test_flag():
   g=''
   for j in range(1072,1072+8+2+len(flag_so_far)):
      g=g+chr(assembly4.memory.data_ptr[j])
   print(g)

def count_match():
   count = 0
   while(assembly4.memory.data_ptr[1024+count]==assembly4.memory.data_ptr[1072+count]):
      count=count+1
   return count

flag="picoCTF{0123456789abcdef0123456789abcdef}"
flag_chars=string.ascii_lowercase+"_"+string.digits+"}\x00"
flag_so_far=""
for i in range(24):
   for j in itertools.product(flag_chars,repeat=2):
      init_flag(j)
      assembly4.check_flag()
      if(count_match()>=10+len(flag_so_far)):
         flag_so_far+=(j[0]+j[1])
         print("picoCTF{"+flag_so_far)
         break
'''




import wasmtime.loader # 왜... 경고 뜨는거임...?
import assembly4 #이걸 저장해뒀나 내가...? -> assembly4.wat
import string
import itertools

d_1024 = "\18j|a\118i7IY(\0akLXhY\1c\1awa=\13V'\0ak\1b\05=W@G{?<\15\02\7f_\0c\00"

def init_flag(pair):
    for i in range(len(flag)): #flag 에 주어진 문자열이...?
        assembly4.memory.data_ptr[1072+i] = ord(flag[i])
    for j in range(len(flag_)):
        assembly4.memory.data_ptr[]


def test_flag():



def count_match():