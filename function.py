===== DEF FUNCTION  ======

 
def calculator(num1, num2,op): 
   result=0 
if(op=="+"): 
 result=num1+num2
elif (op=="-"): 
 result= num1 -num2
elif(op == ""): 
 result =num1num2
elif(op=="/"):
 result=num1/num2
else:
 result =0;
return result;

ch="y"
while ch =="y":

number1 =int(input("enter a number :"))
number2 =int(input("enter second numbaer : "))
op=input("enter the operator :")
finalResult =calculator(number1,number2,op);
print(finalResult)
ch= input ("Do you want to continue (y/n) : ")


=====TUPPLE FUCTION FOR SUMATION======

def add(*tup):
 #   l= len(tup)
  #  sum =0
   # for i in range(0,l):
     #   sum=sum+tup[i]
  # ''' print(tup,sum)
#add(12,13,14)
#add(25,12,31,65,)
#add(55,2,12,50,45,65,25,)'''

======TUPPLE FUNCTION FOR EVEN NUMBER======

def add(*a):
   # l=len(a)
    #sum =0
    #for i in range (0,l):
       # if(i%2==0):
          #  sum =a[i] +sum


    #print(a,sum)
# add(12,34,54,46,67)

=====TUPPLE FUCTION FOR SUM OF EVEN NUMBER======

#def sumEle(*a):
   # sum=0
   # for i in range (0,len(a)):
       # if(a[i]%3==0 and a[i]%5==0 and a[i]%7==0):
           #sum= sum+  a[i]

        #else:
             # pass
    #print (a,  sum)

#sumEle(105,67,34,90,210 )

==== TUPPLE FUNCTION FOR ODD NUMBER =====

def sumEle(*a):
    #sum=0
   # for i in range (0,len(a)):
      ##   if(a[i]%3==0 and a[i]%5==0 and a[i]%7==0):
           #sum= sum+  a[i]

         #else:
             # pass
    #print (a,  sum)

#sumEle(105,67,34,90,210 )

