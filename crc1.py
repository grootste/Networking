data=str(input("Enter the data to be send ="))
key=str(input("enter the key of the data ="))
k= len(key)
#appending len(key)-1 number 0's in data
for i in range(k-1):
    data=data+"0"
print("The data after appending 0's is =  ", data)
#converting sting data into integer(binary)
int_data= int(data, 2)
print(int_data)
#Assigning divident as data appended with 0's.
divd= int_data
#converting string key intger(binary) then assigning it into divisor.
divs= key
#Defining XOR of divident and divisor.
def xor(x, y): 
  
    # initialize result 
    res = [] 
  
    #checking all the bit to do XOR operation
    for i in range(1, len(y)): 
        if x[i] == y[i]: 
            res.append('0') 
        else: 
            res.append('1') 
  
    return ''.join(res)
# Performs Modulo-2 division 

def modulo2(divid, divs):
    halt= len(divs)
    sub = divid[0 : halt]
    while halt < len(divid):
        if sub[0] == '1': 
            sub = xor(divs, sub) + divid[halt] 
        else:   
            sub = xor('0'*halt, sub) + divid[halt] 
        halt += 1 
    if sub[0] == '1': 
        sub = xor(divs, sub) 
    else: 
        sub = xor('0'*halt, sub)   
    checkword = sub 
    return checkword 
rem= modulo2(data, key)
print(rem)
print("The reminder after dividing the data with key is = ",rem)
#sender data after adding rem
halt= len(rem)
new_len=len(data)-halt 
data=data[0:new_len]
sender_data=data +rem
print("The data after subtracting the reminder = ",sender_data)
#Dividing the sender data with the divsor.
sender_rem =int(modulo2(sender_data, key), 2)
print("The new reminder of Sender data = ",sender_rem)
#checking in the receiver end.
receiver_data=input("Enter the received data in the other device = ")
receiver_rem=int(modulo2(receiver_data, key), 2)
print("The recieved data is = ", receiver_data)
print("The reminder is = ",receiver_rem)
#checking whether the rem= 0 or not.
if receiver_rem==0:
    print("The Received data has got 0% error")
    print("Hence, The Received data is accepted ")
else:
    print("The code has got some error")
    print("Hence, The recieved data is rejected")


