import random
import os 
#Ahmed Demirezen FEEZX1
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass_list=[]
data=open("data.caz","r+")
k=data.read()
pass_l=open("passwords"+str(k)+".txt","w")
print(int(k)+1)
new_value=int(k)+1
data.close()
os.remove("data.caz")
new_data=open("data.caz","w")


new_data.write(str(new_value))
new_data.close()
def rand(s,passlen,n):
    for i in range(n):
        p =  "".join(random.sample(s,passlen ))
        pass_list.append(p)
print("Creating passwords. It may take some time.")        
rand(s,8,99999)
rand(s,9,99999)
rand(s,10,99999)
rand(s,11,99999)
rand(s,12,99999)
rand(s,13,99999)
rand(s,14,99999)
rand(s,15,99999)
rand(s,16,99999)
rand(s,17,99999)
rand(s,18,99999)
rand(s,19,99999)
rand(s,20,99999)
for i in range(len(pass_list)):
    pass_l.write(pass_list[i]+"\n")
    
pass_l.close()
