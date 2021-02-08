import time
#stop watch for checkig the time
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("The packets is being sent in has taken ---->", round(elapsed)) 
        time.sleep(1)
    return elapsed    
#defining calss called packets
class packets:
    def _init_(self, data, seqno, ackno,sess, delay):
        self.data= data
        self.seqno= seqno
        self.ackno= ackno
        self.delay= delay

#defining class called sender
class sender(packets):
    flag=0
    sent = True
    def sender_check(delay):
        flag=0
        delay= delay
        s= 5
        sess= int(s)
        n= int(stopwatch(delay))
        if n<=sess:
            sent= True
        else:
            sent= False
        return sent
                
#defining class called receiver
class receiver(packets):
    flag=1
    received= False
    def receiver_check(ackno, delay):
        ackno= int(ackno)
        delay= int(delay)
        s= 5
        sess= int(s)
        n= int(stopwatch(ackno)+ delay) 
        if n<=sess:
            received= True
        else:
            received= False
        return received
#checks whether the packet is send or not.
def checker(a, flag):
    if a==True and flag==0:
        print("The data has been Send ")
    elif a==False and flag==0:
        print(" The data needs to be resend ")
    elif a==True and flag== 1:
        print("The cumulative acknoledgement has  been sent  ")
    else:
        print("The cumulative acnkoledgement has been failed to sent ")

#Staring to send the packets
n=int(input("Enter the total number of packets to be sent  "))
p1= packets
p1.delay=int(input("Enter the Delay of data sent = "))
p1.ackno=input("Enter the acknoledgement time of data to be sent  =")
p1.data=input("Enter the data to be sent = ")
def start(n):
    for i in range(n):
        for i in range(3):
            p1= packets
            p1.seqno=print("The seqno is = ", i)
            n=sender.sender_check(p1.delay)
            flag=0
            checker(n, flag)
        flag=1
        n=receiver.receiver_check(p1.ackno, p1.delay)
        checker(n, flag)

start(n)
