import os, hashlib, binascii # binascii needed for hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)  
password = 'password'
# encrypt the password we provided as 32 character string
md5 = hashlib.md5()
md5.update('password')
print 'md5: '+ md5.hexdigest() #this will show you the encrypted value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!

# shorter ways to write it:
print 'md5: '+ hashlib.md5('password').hexdigest()

# a much stronger hash:
print 'sha224: '+ hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

# even stronger:
print 'sha256: '+ hashlib.sha256("Nobody inspects the spammish repetition").hexdigest()

print 'sha1: '+ hashlib.sha1("Can you possibly guess this?").hexdigest()

# yet even stronger:
print 'sha256: '+ binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000))

print 'sha512: '+ hashlib.sha512("Can you possibly guess this?").hexdigest()
