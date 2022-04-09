#درج تاريخ ميلادي 
import datetime
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

print ('-'*15)

# نوشتن تاربخ به ماه وسال وساعت
import datetime as dt
today_date = dt.date.today()
print(today_date.strftime("The Current Date is :\n\n%A %B %d, %Y"))

print ('^'*15)

# پرسيدن اسم
print ('نام ونام خانوادگي ')
x = input('Enter your name:')
print('Hello, ' + x)


# sen karbar ra migirad and tarikh tavalod ra mydahad
import datetime
now = datetime.datetime.now()
age = float(input('What is your age? '))
year_born =  int(now.year - age)
print ("Awesome! you were born in ", year_born)

print ('-'*10)
print ('متولد چه سالي هستيد؟')
#sal tavalod ra medahim sen karbar ra midahad
import datetime
  
curYear = datetime . datetime .now() . year
userYear = input (' Enter the year you where born : ')
 
diff = curYear - int(userYear)
print ('--------')
print (' شما' ,diff,' داريد ')
print ( 'You are ',diff,'years old.' )
print ('--------')



# ميپرسم بازهم سوال داريد
print (x,'can I help you again?')
print ( 'ميتونم دوباره کمک تون کنم؟ ',x)
input ( 'lease write yes or no  :  ')
#اگرگفت بله بپرسم سوال چيه درغير اين صورت برنامه بسته شه
