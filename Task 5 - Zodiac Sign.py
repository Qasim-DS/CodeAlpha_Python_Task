import datetime
import csv
import pandas

Dictionary1={}
def takeUserDay():
    try:
        day =int(input('Enter day: '))

        if day != str:
            if day <= 0 or day > 31:
                print('Enter a valid day!!! ')
                return takeUserDay()
            
            else:
                return day
    except:
        print('ERROR: Only Numbers are accepted!')
        return takeUserDay()




def takeUserMonth():
    month = input('Enter month: ')
    if month == 'January' or month == '1' or month == 'Jan' or month == 'january' or month == 'jan' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month=='February' or month == '2' or month == 'Feb' or month =='february' or month =='feb' or month =='02' :
        monthNumber = 2
        return monthNumber
    elif month=='March' or month =='3' or month =='Mar' or month =='march' or month =='mar' or month =='03':
        monthNumber = 3
        return monthNumber
    elif month=='April' or month =='4' or month =='Apr' or month =='april' or month =='apr' or month =='04':
        monthNumber = 4
        return monthNumber
    elif month=='May' or month =='5' or month =='may' or month =='05':
        monthNumber = 5
        return monthNumber
    elif month=='June' or month =='6' or month =='june' or month =='06':
        monthNumber = 6
        return monthNumber
    elif month=='July' or month =='7' or month =='july' or month =='07':
        monthNumber = 7
        return monthNumber
    elif month=='August' or month =='8' or month =='Aug' or month =='august' or month =='aug' or month =='08':
        monthNumber = 8
        return monthNumber
    elif month=='September' or month =='9' or month =='Sept' or month =='september' or month =='sept' or month =='09':
        monthNumber = 9
        return monthNumber
    elif month=='October' or month =='10' or month =='Oct' or month =='october' or month =='oct':
        monthNumber = 10
        return monthNumber
    elif month=='November' or month =='11' or month =='Nov' or month =='november' or month =='nov':
        monthNumber = 11
        return monthNumber
    elif month=='December' or month =='12' or month =='Dec' or month =='december' or month =='dec':
        monthNumber = 12
        return monthNumber
    else:
        print('ERROR: Enter a valid month ')
        return takeUserMonth()



def takeUserYear():

    try:

        year = int(input('Enter year: '))
        
        if year != str:
            if year <= 0:
                print('ERROR:  ')
                return takeUserYear()
            elif year%4 == 0:
                print('Leap year!')
                return year
            else:
                return year
    except:
        print('ERROR: Enter Numerical Value Only')
        return takeUserYear()
    



def calculateSign(day,month):
      
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
        
    return astro_sign

def takeDate(year,month,day):
    date1=datetime.date(year,month,day)
    print('DOB: ',date1)
    return date1




def repeatQuestion():
    Finder=input('Do you want to find any other Zodiac sign(yes/no): ')
    if Finder =='yes':
        return True
    else:
        return False


def UserInput(count):
    
    userName= input('Enter the name of the user: ')
    userYear = takeUserYear()
    userMonth = takeUserMonth()
    userDate = takeUserDay()
    fullDate = takeDate(userYear,userMonth,userDate)
    yourSign = calculateSign(userDate, userMonth)
    print(userName, "your Zodiac sign is :",yourSign)
    Dictionary1[count] = { 'FullName' : '', 'DateOfBirth' : '', 'ZodiacSign' : '' }
    Dictionary1[count]['FullName'] = userName
    Dictionary1[count]['DateOfBirth'] = str(fullDate)
    Dictionary1[count]['ZodiacSign'] = yourSign
    
    
    print(Dictionary1[count])
    
def SavetoPandas():
    pass

if __name__=='__main__':
    Repeat = True
    Count = 1
    while Repeat == True:
        UserInput(Count)
        Count +=1
        Repeat = repeatQuestion()
    df = pandas.DataFrame(data=Dictionary1)
    fileName = input('PLease enter file Name:   ')
    savedData = df.to_csv(fileName+'.csv', index = True)
    print(df)
