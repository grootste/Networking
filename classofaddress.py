#finding class of the ipaddress
def findclass(ipclass):
    if(ipclass>1 and ipclass< 128):
        print('This Ip is from class A')
    elif(ipclass>127 and ipclass <192):
        print('This Ip is from Class B')
    elif(ipclass>191 and ipclass <224):
        print('This Ip is from class C')
        print('The default sub-net mask for class C is 255.255.255.x')
    elif(ipclass>224 and ipclass< 239):
        print('This Ip is from class D')
        print('This host id is not defined')
        print('This class doesn’t have any sub-net mask')
    else:
         print('This Ip is from class E')
         print('This host id is not defined')
         print('This class doesn’t have any sub-net mask')
         

def findclassbin(ipclass):
    ipclass=int(ipclass, 2)
    print(ipclass)
    if(ipclass>1 and ipclass< 128):
        print('This Ip is from class A')
    elif(ipclass>127 and ipclass <192):
        print('This Ip is from Class B')
    elif(ipclass>191 and ipclass <224):
        print('This Ip is from class C')
        print('The default sub-net mask for class C is 255.255.255.x')
    elif(ipclass>224 and ipclass< 239):
        print('This Ip is from class D')
        print('This host id is not defined')
        print('This class doesn’t have any sub-net mask')
    else:
         print('This Ip is from class E')
         print('This class doesn’t have any sub-net mask')
         print('This host id is not defined')

def findclasshex(ipclass):
    ipclass=int(ipclass, 16)
    if(ipclass>1 and ipclass< 128):
        print('This Ip is from class A')
    elif(ipclass>127 and ipclass <192):
        print('This Ip is from Class B')
    elif(ipclass>191 and ipclass <224):
        print('This Ip is from class C')
        print('The default sub-net mask for class C is 255.255.255.x')
    elif(ipclass>224 and ipclass< 239):
        print('This Ip is from class D')
        print('This host id is not defined')
        print('This class doesn’t have any sub-net mask')
    else:
         print('This Ip is from class E')
         print('This class doesn’t have any sub-net mask')
         print('This host id is not defined')

def findclassoct(ipclass):
    ipclass=int(ipclass, 8)
    if(ipclass>1 and ipclass< 128):
        print('This Ip is from class A')
    elif(ipclass>127 and ipclass <192):
        print('This Ip is from Class B')
    elif(ipclass>191 and ipclass <224):
        print('This Ip is from class C')
        print('The default sub-net mask for class C is 255.255.255.x')
    elif(ipclass>224 and ipclass< 239):
        print('This Ip is from class D')
        print('This host id is not defined')
        print('This class doesn’t have any sub-net mask')
    else:
         print('This Ip is from class E')
         print('This class doesn’t have any sub-net mask')
         print('This host id is not defined')

print(" Plese enter the choice for the \n 1.Decimal \n 2. Binary \n 3. Hexadecimal \n 4. octal")
n=int(input())
if(n=="1"):
    findclass(ipclass)
elif(n=='2'):
    findclass(ipclassbin)
elif(n=='3'):
    findclass(ipclasshex)
elif(n=='4'):
    findclass(ipclassoct)
add=str(input("Enter the Address to be determined = "))
print("The entered address is = ", add)
#slicing ip class
def classaddr(add):
    for i in range(len(add)):
        if(add[i]== '.'):
           halt=i
           print(i)
           break
    return halt
stop= classaddr(add)
ipclass= add[0:stop]
ipclass= int(ipclass)
findclass(ipclass)
