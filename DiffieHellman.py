import hashlib, random
print("#                               Commun                                #")
a = hashlib.sha256(b"sacha")
b = hashlib.sha256(b"sacha")
print("Alice ",a.hexdigest(), "\nBob   ",b.hexdigest())
print("#                               Secret                                #")
b = b.hexdigest() + hashlib.sha256(bytes(str(random.randint(100000, 10000000000000000000)), 'utf-8')).hexdigest()
a = a.hexdigest() + hashlib.sha256(bytes(str(random.randint(100000, 10000000000000000000)), 'utf-8')).hexdigest()
reg_b = b
reg_a = a
print("Alice ",a, "\nBob   ",b)
print("#                               Exchange                              #")
trans = b
b = a
a = trans
print("Alice ",a, "\nBob   ",b)
print("#                               Final                                 #")
b = hashlib.sha256(bytes(reg_b + b, 'utf-8')).hexdigest()
a = hashlib.sha256(bytes(a + reg_a, 'utf-8')).hexdigest()
print("Alice ",a, "\nBob   ",b)
if a == b:
    print("Secret is shared")
else:
    print("Secret is not shared")
print("End")
