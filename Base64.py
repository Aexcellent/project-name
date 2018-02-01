
import base64

#要编码的二进制数据不是三的倍数
#Base64用\x00字节在末尾补足再在编码末尾加上1或2个=号
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHNOcmluZw==')


#由于标准的Base64编码后可能出现字符+和/
#在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64edecode('abcd--__')
