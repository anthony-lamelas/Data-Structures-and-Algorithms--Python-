s1 = CompactString('aaaaaaacccaaaaa')
s2 = CompactString('aaaaaaacccaaaa') 

print(s1 > s2) #true

c1 = CompactString('aaaaabbbaaac')
c2 = CompactString('aaaaaaacccaaaa')

print( c1 <= c2) #false




d1 = CompactString('aaaaa')
d2 = CompactString('aaaaa')

print(d1 <= d2) #true
