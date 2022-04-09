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

print('-'*30)
# tarekh tavalod and rooz 
Month = [ 'Farvardin','Ordibehesht', 'Khordad','Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Day', 'Bahman', 'Esfand']

Y = int(input('\nEnter year:'))
M = int(input('\nEnter Month:'))
D = int(input('\nEnter Day:'))

end = ['st' ,  'nd' ,  'rd'] + 17*['th'] + [ 'st' , 'nd' , 'rd'] +7 * ['th'] + ['st']

m_index = M-1
d_index = D-1

print (D, end[d_index] ,   ' ' ,  Month [m_index] ,   ' ' ,  Y)

print('-'*30)


# ميپرسم بازهم سوال داريد
print (x,'can I help you again?')
print ( 'ميتونم دوباره کمک تون کنم؟ ',x)
input ( 'lease write yes or no  :  ')
#اگرگفت بله بپرسم سوال چيه درغير اين صورت برنامه بسته شه
