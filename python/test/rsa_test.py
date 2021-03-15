'''
Author: dingdingtao
Date: 2021-01-12 10:40:15
LastEditTime: 2021-03-15 14:28:24
LastEditors: dingdingtao
Description: 
'''
import rsa
import base64

def create_keys():  # 生成公钥和私钥
    (pubkey, privkey) = rsa.newkeys(1024)
    #输出公钥文件
    pub = pubkey.save_pkcs1()
    with open('C:\\Users\\Administrator\\Desktop\\pub.key', 'wb+')as f:
        f.write(pub)
    # 输出私钥文件
    pri = privkey.save_pkcs1()
    with open('C:\\Users\\Administrator\\Desktop\\pri.key', 'wb+')as f:
        f.write(pri)

#RSA加密，加密文本为base64的字符串
def encrypt(strs):
    with open('C:\\Users\\Administrator\\Desktop\\pub.key', 'rb') as publickfile:
        pub = publickfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(pub)
    crypt_text = rsa.encrypt(strs.encode('utf8'), pubkey)
    encrypt_str = str(base64.b64encode(crypt_text), encoding="utf-8")
    return encrypt_str  # 加密后的密文

#RSA解密，输入字符为base64字符
def decrypt(decrypt_content):
    with open('C:\\Users\\Administrator\\Desktop\\pri.key', 'rb') as privatefile:
        pri = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(pri)
    strs = base64.b64decode(decrypt_content)
    decrypt_str = rsa.decrypt(strs, privkey).decode('utf-8')  # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str
    return decrypt_str


if __name__ == '__main__':
    #create_keys()
    strs = 'helloello'
    enstr = encrypt(strs)
    #destr = decrypt(enstr)
    print(enstr)
    #print(destr)