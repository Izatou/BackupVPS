from Pyfhel import Pyfhel, PyPtxt, PyCtxt
import tempfile
import numpy as np

#Inisialisasi Homomorphic python
HE = Pyfhel()
HE.contextGen(p=65537,flagBatching=True,base=3)
HE.keyGen()
#HE.rotateKeyGen(60)
#HE.relinKeyGen(60, 4)
vector1 = [ 1, 2, 3, 4, 5, 6]
simpan=[]
test = '11 @Halo cuy'
for ch in test:
   simpan.append(ord(ch))
print(simpan)

HE.saveContext('context')
HE.savepublicKey('pubs.key')
HE.savesecretKey('pub1.key')
#HE.saverelinKey(tmp_dir.name + "/relin.key")
#HE.saverotateKey(tmp_dir.name + "/rotate.key")

HE2 = Pyfhel()
HE2.restoreContext('context')
HE2.restorepublicKey('pubs.key')
HE2.restoresecretKey('pub1.key')
#HE2.restorerelinKey(tmp_dir.name + "/relin.key")
#HE2.restorerotateKey(tmp_dir.name + "/rotate.key")

#with open('lila.txt','rb') as user:
#    users = user.read()

en1 = HE.encryptBatch(simpan)
en1.save("en1.txt")
en3 = HE.decryptBatch(en1)
print(en1)

decodedMessage = ""
#print(en3)
for item in en3:
   decodedMessage += chr(item)

print ("Decoded message:", decodedMessage)

