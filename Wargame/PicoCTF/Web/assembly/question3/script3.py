'''
function copy(a:int, b:int) {
  var c:int = g_a;
  var d:int = 16;
  var e:int_ptr = c - d;
  e[3] = a;                    // string
  e[2] = b;                    // index
  var f:int = e[3];
  if (eqz(f)) goto B_a;             ---> 여기서 만족하면
  var g:int = 4;              // g = 4
  var h:int = e[2];           
  var i:int = 5;              // i = 5
  var j:int = h % i;          // j = e[2] mod 5
  var k:ubyte_ptr = g - j;    // k = g - j = 4 - (e[2]mod5)
  var l:int = k[1067];        // l = d_1067[k] = d_1067[4-(e[2] mod 5)]
  var m:int = 24;             // m = 24
  var n:int = l << m; 
  var o:int = n >> m;         // o = n >> 24 = (l << 24)>>24 = l 이니까 무시해도 됨. 걍 일부러 꼬아놓은듯
  var p:int = e[3];           // p = e[3]
  var q:int = p ^ o;          // q = p ^ o = e[3] ^ o = a ^ l = d_1024 ^ d_1067[4-(e[2] mod 5)]
  e[3] = q;                   
  label B_a:                      ---> 여기로 가라는 소리??
  var r:int = e[3];           // r = e[3] = q = a ^ d_1067[4-(e[2] mod 5)]
  var s:byte_ptr = e[2];      // s -> e[2] = b
  s[1072] = r;                // b[1072] = r ...? 그러니까 d_1067 문자열 다음에 바로 r(답) 을 붙이는 듯
}
'''

d_1024="\x9dn\x93\xc8\xb2\xb9A\x8b\xc2\x90\x8bd\xc7\x9e\xc9\x88b\x95\x91\x90\xdac\xc5\x95\x95\xd82\xc4\xc5\x92\x8ee\x92\x96\x97\x8ca\xc4\x93\x92\x90\x00\x00"
d_1067= "\xf1\xa7\xf0\x07\xed"
flags = ""

print("==== Answer 1 ===")
for i in range(len(d_1024)):
    #print(ord(d_1024[i]), ord(d_1024[i])^ord(d_1067[4-(i%5)]))
    print(chr(ord(d_1024[i])^ord(d_1067[4-(i % 5)])), end="") #인덱스가 4이하니까 d_1067 로 때려맞춤

print("\n==== Answer 2 ====")
for i in range(len(d_1024)):
    tmp = chr(ord(d_1024[i])^ord(d_1067[4-(i % 5)])) #인덱스가 4이하니까 d_1067 로 때려맞춤
    flags += tmp 
    #print(chr(ord()^ord()), "")
print(flags)
