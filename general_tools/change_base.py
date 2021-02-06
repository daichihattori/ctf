# def hexToAscii(str):
#     cnt = 0
#     buf=[]
#     ans=[]
#     while cnt < len(str):
#         tmp=str[cnt:cnt+2]
#         buf.append(tmp)
#         cnt=cnt+2

#         ans.append(chr(int('0x'+tmp)))

#     print(buf)
#     print(ans)
    
# a=0b000010100000100100001
# a_hex=format(a,'x')
# print(a_hex)
# hexToAscii("313233")

import binascii
