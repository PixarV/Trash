import random
from enum import Enum


class Ages(Enum):
    STUDENT = 1,
    MIDDLE_PERSON = 2,
    OLD_PERSON = 3,
    VERY_OLD_PERSON = 4


message = ""

GREETING_MAN = (
    'Hello, brother',
    'qwe'
)

GREETING_WOMAN = (
    'Hello,sister',
    '123'
)

MORE_CALLS = (
    'what bout up your phone calls?',
    'qwqwe'
)

MORE_SMSs = (
    'what bout up your phone sms?',
    'qwqwe'
)

MORE_INTERNET = (
    'what bout more INTERNET?',
    'qwqwe'
)

NEUTRAL_MESSAGE = (
    "HAVE a GOOD day"
)

def get_age(age, male):
    global message
    if (17>=age):
        raise IOError
    elif (18<=age<=27):
        if male == 'M':
            message += GREETING_MAN[random.randrange(len(GREETING_MAN))]
        else:
            message += GREETING_WOMAN[random.randrange(len(GREETING_WOMAN))]
        return Ages.STUDENT
    elif (27<age<=45):
        message += "You're welcome"
        return Ages.MIDDLE_PERSON
    elif (45<age<=60):
        message += "Dear "
        return Ages.OLD_PERSON
    else:
        return Ages.VERY_OLD_PERSON


def parse_attr(calls, SMS, Internet, tarif):
    global message
    check_out_tarif(calls, tarif[0], MORE_CALLS)
    check_out_tarif(SMS, tarif[1], MORE_SMSs)
    check_out_tarif(Internet, tarif[2], MORE_INTERNET)
    message += NEUTRAL_MESSAGE[random.randrange(len(NEUTRAL_MESSAGE))]



def check_out_tarif(values, tarif_val, mes):
    global message
    for value in values:
        if value > tarif_val:
            message += mes[random.randrange(len(mes))]
            return







#male = input('Enter your male')
#age = input("Enter your Age")
#calls = input("Calls")
#SMS = input("SMS")
#INT = input("INTERNET")
#tarif= input("TARIF")
#print(male,age,calls,SMS,INT,tarif)
male = 'M'
age = 60
calls = [1,1,1]
SMS = [1,1,1]
INT = [1,2,3]
tarif= [1,1,1]

try:
    age_format = get_age(int(age), male)
    parse_attr(calls, SMS, INT, tarif)
    print(message)
except IOError:
    print("ENTER ANOTHER AGE")
    exit(1)

