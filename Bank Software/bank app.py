
# coding: utf-8

# In[ ]:


from random import randint
ac_no = randint(1000,13400)
s = ac_no


# In[ ]:


acq = int(input("Enter Number 4 for Admin Panel "))
if acq == 4:
    pswd = int(input("Enter the password"))
    if pswd == 1234:
        #info=d.get(acc,"Invalid Account Number")
        for var1,var2 in d.items():
            print('\n', var1,'-->\n')
            for var3,var4 in var2.items():
                print(var3, ' : ',var4)
    else:
        print("Sorry Sir, Wrong Input")


# In[ ]:


acq = int(input("Enter Number 6 for Add Account "))
if acq == 6:
    d={}
    ch=input("Do You Want To Add Account:").lower()
    while(ch=='yes'):
        name,mob_nu,aadhar,money=input("Name Mobile_no Aaddhar_No Money").split()
        if (len(mob_nu) == 10 and len(aadhar)== 12) and int(money) >= 0:
            s+=1
            d[s]={'name':name,'mob_nu':mob_nu,'aadhar':aadhar,'money':money}
            ch=input("Do You Want To Add Account:").lower()
        else:
            print('Wrong Input')
else:
        print("Sorry Sir, Wrong Input")


# In[ ]:


d


# In[ ]:


info=d.get(acc,"Invalid Account Number")
for var1,var2 in info.items():
    print(var1,':',var2)


# In[1]:


from getpass import getpass
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
print("*"*50)
print('!Welcome!'.center(50,' '))
speak.Speak("welcome")
print("*"*50)
string="""
1.Withdrawl
2.Deposit
3.Account Updation
4.Admin Panel
5. Loan Request
6.Add Account"""
print(string)
speak.Speak("Choose the Number..")
acq = int(input("Choose the Number.. "))
if acq == 1:
    speak.Speak("Enter the account Number")
    aca = int(input("Enter the account number "))
    if aca in d:
        speak.Speak("Enter the money")
        amo = int(input("Enter the money "))
        if amo > 0 and int(d[aca]['money'])-amo>0:
            d[aca]['money']=str(int(d[aca]['money'])-amo)
            speak.Speak("Successful Withdrawl of amount Rs")
            print("Successful Withdrawl of amount Rs.",amo)
            speak.Speak(amo)
            speak.Speak("you want to show Your account information So Press yes or no")
            aa = input("you want to show Your account information So Press yes or no ")
            if aa == 'yes':
                for var1,var2 in d[aca].items():
                    print(var1, ":", var2)
            else:
                exit()
        else:
            speak.Speak("Guruji Wrong Input")
            print("Guruji Wrong Input")
    else:
        speak.Speak("Invalid Account Number")
        print("Invalid Account Number")
elif acq == 2:
    speak.Speak("Enter the account number")
    aca = int(input("Enter the account number "))
    if aca in d:
        speak.Speak("Enter the money ")
        amo = int(input("Enter the money "))
        d[aca]['money']=str(int(d[aca]['money'])+amo)
        speak.Speak("Successful deposit of amount Rs")
        print("Successful deposit of amount Rs. ",amo)
        speak.Speak(amo)
    else:
        speak.Speak("Invalid Account Number")
        print("Invalid Account Number")
if acq == 3:
    speak.Speak("Enter the account number")
    aca = int(input("Enter the account number"))
    if aca in d:
        speak.Speak("Do you want to Continue Press Yes or No")
        aa = input("Do you want to Continue Press Yes or No ").lower().strip()
        if aa == 'yes':
            speak.Speak("What do you want to change Aadhar Number so press 1 or 2 for Mobile Number")
            ad = input('What do you want to change Aadhar Number so press 1 or 2 for Mobile Number ').lower().strip()
            if ad == '1':
                speak.Speak("Enter the New Aadhar Number")
                sl = int(input("Enter the New Aadhar Number "))
                d[aca]['aadhar']=str(sl)
                speak.Speak("Success")
                print("Success")
            elif ad == '2':
                speak.Speak("Enter the New Mobile Number")
                sl = int(input("Enter the New Mobile Number "))
                d[aca]['mob_nu']=str(sl)
                speak.Speak("Success")
                print("Success")
            else:
                speak.Speak("Wrong Input")
                print("Wrong Input")
        else:
            speak.Speak("Wrong Input")
            print('Wrong Input')
if acq == 4:
    speak.Speak("Enter the Password")
    pswd = int(getpass("Enter the password"))
    if pswd == 1234:
        #info=d.get(acc,"Invalid Account Number")
        for var1,var2 in d.items():
            print('\n', var1,'-->\n')
            for var3,var4 in var2.items():
                print(var3, ' : ',var4)
    else:
        speak.Speak("Sorry Sir, Wrong Input")
        print("Sorry Sir, Wrong Input")
if acq == 5:
    speak.Speak("Enter the account Number")
    aca = int(input("Enter the account Number"))
    if aca in d:
        speak.Speak("Are u student or business man or goverment officer")
        aa = input("Are u student/business/goverment officer").lower().strip()
        if aa == 'student':
            speak.Speak("Sorry ,You are not able to get loan")
            print("Sorry ,You are not able to get loan")
        speak.Speak("Enter the Loan Amount")
        loan = int(input('Enter the Loan Amount '))
        speak.Speak("Enter the Salary")
        salary = int(input("Enter the Salary "))
        if aa == 'business':
            la = (salary*12)//2
            if la >= loan and loan >= 10000:
                speak.Speak("You have just got ")
                print("You have just got ",loan, "of Request Loan for 1 Year")
                speak.Speak(loan)
                speak.Speak("of Request Loan for 1 Year")
            else:
                speak.Speak("You are not suitable for loan application ")
                print('You are not suitable for loan application')
        elif aa == 'goverment job':
            la = (salary*12*80)//100
            if la >= loan and loan >= 10000:
                speak.Speak("You have just got ")
                print("You have just got ",loan, "of Request Loan for 1 Year")
                speak.Speak(loan)
                speak.Speak("of Request Loan for 1 Year")
            else:
                speak.Speak("You are not suitable for loan application ")
                print('You are not suitable for loan application')
        else:
            speak.Speak("Wrong Input")
            print('Wrong Input')
if acq == 6:
    d={}
    speak.Speak("Do You Want To Add Account")
    ch=input("Do You Want To Add Account:").lower().strip()
    while(ch=='yes'):
        speak.Speak("Enter the Name, Mobile Number, Aadhar Number, Money")
        name,mob_nu,aadhar,money=input("Name Mobile_no Aadhar_No Money").split()
        if (len(mob_nu) == 10 and len(aadhar)== 12) and int(money) >= 0:
            s+=1
            d[s]={'name':name,'mob_nu':mob_nu,'aadhar':aadhar,'money':money}
            speak.Speak("Do You Want To Add Account")
            ch=input("Do You Want To Add Account:").lower()
        else:
            speak.Speak("Wrong Input")
            print('Wrong Input')
else:
    speak.Speak("Wrong Input")
    print("Wrong Input")


# In[ ]:


d


# In[ ]:


acq = int(input("Enter Number 3 for Account Updation "))
if acq == 3:
    aca = int(input("Enter the account nu"))
    if aca in d:
        aa = input("Do you want to Continue Press Yes or No ").lower()
        if aa == 'yes':
            ad = input('What do you want to change Aadhar NUmber so press 1 or 2 for Mobile Number ').lower()
            if ad == '1':
                sl = int(input("Enter the New Aadhar Number "))
                d[aca]['aadhar']=str(sl)
                print("Success")
            elif ad == '2':
                sl = int(input("Enter the New Mobile Number "))
                d[aca]['mob_nu']=str(sl)
                print("Success")
            else:
                print("Wrong Input")


# In[ ]:


acq = int(input("Enter Number 5 for Loan Request "))
if acq == 5:
    aca = int(input("Enter the account Number"))
    if aca in d:
        aa = input("are you student/business/goverment job  ").lower()
        if aa == 'student':
            print("Sorry ,You are not able to get loan")
        loan = int(input('Enter the Loan Amount '))
        salary = int(input("Enter the Salary "))
        if aa == 'business':
            la = (salary*12)//2
            if la >= loan and loan >= 10000:
                print("You have just got ",loan, "of Request Loan for 1 Year")
            else:
                print('You are not suitable for loan application')
        elif aa == 'goverment job':
            la = (salary*12*80)//100
            if la >= loan and loan >= 10000:
                print("You have just got ",loan, "of Request Loan for 1 Year")
            else:
                print('You are not suitable for loan application')
        else:
            print('Wrong Input')


# In[15]:


def test(fun):
    def demo():
        print("*"*50)
        s = fun()
        print("*"*50)
        return s
    return demo


# In[18]:


@test
def hello():
    print('welcome'.center(50,' '))
    return 'Exit'


# In[19]:


hello()


# In[ ]:


get_ipython().system(' install gTTS')


# In[1]:


from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")


# In[24]:


import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
s=123
#print(s)
speak.Speak(s)

