import array
add=str(input("Enter the Address to be determined = "))
print("The entered address is = ", add)
#slicing ip class
def classaddr(add):
    halt=[]
    for i in range(len(add)):
        if(add[i]== '.'):
            halt.append(i)
            print(i)
            break
    return halt
stop= classaddr(add)

ipclass= add[0:stop]
ipclass= int(ipclass)
#finding class of the ipaddress
def findclass(ipclass):
    if(ipclass>1 and ipclass< 128):
        print('This Ip is from class A')
    elif(ipclass>127 and ipclass <192):
        print('This Ip is from Class B')
    elif(ipclass>191 and ipclass <224):
        print('This Ip is from class C')
    elif(ipclass>224 and ipclass< 239):
        print('This Ip is from class D')
        print('This host id is not defined')
    else:
         print('This Ip is from class E')
findclass(ipclass)
