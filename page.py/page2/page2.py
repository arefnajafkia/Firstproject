# من يک رباتم 
print  ( ' من يک رياط هستم واسمم پايتون9 است ')
print (' I am a robot , My name is python 9 .')

print ('^'*20)
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

print ('-'*20)

# نوشتن تاربخ به ماه وسال وساعت
import datetime as dt
today_date = dt.date.today()
print(today_date.strftime("The Current Date is :\n\n%A %B %d, %Y"))

print ('^'*20)

name = input ("  نام ونام خانوادگي شما please enter your name : ")

birth_year = input ("متولد چه سالي هستي birth year: ")
age = 1401 - int (birth_year)
city = input (" متولد کدام شهريد Born in which city :")
print('-'*30)

print ( '!هستيد',city,'شما',age,'داريد وازشهر',name,'خوش آمديد')

print ( "Welcome ",name, "you are" ,age, "years old  and You were born in  " ,city , "!" )

print('-'*30)

# tarekh tavalod and rooz 
Month = [ 'Farvardin','Ordibehesht', 'Khordad','Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Day', 'Bahman', 'Esfand']

Y = birth_year
M = int(input('متولد چه ماهي هستي\nEnter Month :'))
D = int(input('متولد چه روزي هستي\nEnter Day :'))
S = city
end = ['st' ,  'nd' ,  'rd'] + 17*['th'] + [ 'st' , 'nd' , 'rd'] +7 * ['th'] + ['st']

m_index = M-1
d_index = D-1

print('-'*30)
print ('You were born ' ,D, end[d_index] ,   ' ' ,  Month [m_index] ,   ' ' ,  Y )
#print ( 'You were born in the city',S,)
#print ('you are', age ,'years old.')
print('-'*30)
