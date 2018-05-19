import sys
import random
from PyQt5 import QtWidgets
from enum import Enum

class Ages(Enum):
    STUDENT = 1,
    MIDDLE_PERSON = 2,
    OLD_PERSON = 3,
    VERY_OLD_PERSON = 4


message = ""

GREETING_MAN = (
    'Hello, brother ',
    'Здравствуй! ',
    'Драсьте! ',
    'Привет! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Салют! ',
    'Здорово!',
    'Дарова! ',
    'Хэлло! ',
    'Хай! ',
    'Вечер в хату! ',
    'Глубокое (глубочайшее) почтение ',
    'Горячий привет! ',
    'С добрым утром! ',
    'Здра ',
    'Прив ',
    'Приветики ',
    'Превед ',
    'Здравки ',
    'Доброго здоровьечка ) ',
    'HI ',
    'Guten Tag ',
    'Guten Morgen ',
    'Guten Nacht ',
    'Bonjour ',
    'Hola ',
)

GREETING_WOMAN = (
    'Hello,sister',
    'Здравствуй! ',
    'Драсьте! ',
    'Привет! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Салют! ',
    'Здорово!',
    'Дарова! ',
    'Хэлло! ',
    'Хай! ',
    'Вечер в хату! ',
    'Глубокое (глубочайшее) почтение ',
    'Горячий привет! ',
    'С добрым утром! ',
    'Здра ',
    'Прив ',
    'Приветики ',
    'Превед ',
    'Здравки ',
    'Доброго здоровьечка ) ',
    'HI ',
    'Guten Tag ',
    'Guten Morgen ',
    'Guten Nacht ',
    'Bonjour ',
    'Hola ',
)

GREETIN_MIDDLE = (

    'Здравствуйте! ',
    'Здравствуй! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Приятного вечера! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Приветствую вас! ',
    'В кои-то веки! ',
    'Вот так встреча! ',
    'Всегда рады Вам ',
    'Добро пожаловать! ',
    'Дозвольте приветствовать (Вас) ',
    'Душевно рад (Вас видеть) ',
    'Душою рад Вас видеть ',
    'Желаю здравствовать! ',
    'Здравия желаю ',
    'Какая встреча! ',
    'Какие гости! ',
    'Позвольте Вас приветствовать ',
    'Приветствую Вас ',
    'Приятный вечер! ',
    'Приятный день! ',
    'Рад Вам ',
    'Рад Вас видеть ',
    'Рад Вас видеть в добром здравии ',
    'Рад Вас приветствовать ',
    'Рад Вас слышать ',
    'Разрешите Вас приветствовать ',
    'С возвращением! ',
    'С выздоровлением! ',
    'С добрым утром! ',
    'Сердечно приветствую Вас! ',
    'Сердечно рад Вам ',
    'Сердечный поклон Вам ',
    'Сколько лет, сколько зим! ',
    'Тысячу лет Вас не видел (не виделись)! '
)

GREETING_VERY_OLD = (
    'Сердечно приветствую Вас! ',
    'Сердечно рад Вам ',
    'Здравствуйте! ',
    'Доброе утро! ',
    'Добрый день! ',
    'Добрый вечер! ',
    'Приятного вечера! ',
    'Доброй ночи! ',
    'Доброго времени суток! ',
    'Приветствую вас! ',
    'В кои-то веки! ',
    'Вот так встреча! ',
    'Всегда рады Вам ',
    'Глубокое (глубочайшее) почтение ',
    'Доброго здоровья (здоровьица...)! ',
    'Добро пожаловать! ',
    'Дозвольте приветствовать (Вас) ',
    'Душевно рад (Вас видеть) ',
    'Душою рад Вас видеть ',
    'Желаю здравствовать! ',
    'Здравия желаю ',
    'Моё почтение! ',
    'Нижайшее почтение! ',
    'Позвольте Вас приветствовать ',
    'Почитаю приятным долгом засвидетельствовать Вам моё почтение ',
    'Приветствую Вас '
)

MORE_CALLS = (
    'what bout up your phone calls? ',
)

MORE_SMSs = (
    'what bout up your phone sms? ',
)

MORE_INTERNET = (
    'what bout more INTERNET? ',
)

NEUTRAL_MESSAGE = (
    "HAVE a GOOD day "
)

TARIF = (
    ('Включайся! Слушай', 450, 10),
    ('Включайся! Общайся', 600, 15),
    ('Включайся! Говори', 700, 5),
    ('Включайся! Смотри', 800, 20),
    ('Включайся! Смотри+', 1000, 25),
    ('Включайся! Пиши', 200,5,10),
    ('Включайся! Премиум', 3000, 30, 0)
)
TARIF_SNG = (
    ('Тёплый приём М', 500, 13, 300),
    ('Тёпылый приём S', 300, 3, 100)
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
        message += GREETIN_MIDDLE[random.randrange(len(GREETIN_MIDDLE))]
        return Ages.MIDDLE_PERSON
    elif (45<age<=60):
        message += GREETING_VERY_OLD[random.randrange(len(GREETING_VERY_OLD))]
        return Ages.OLD_PERSON
    else:
        return Ages.VERY_OLD_PERSON


def parse_attr(calls, SMS, Internet, tarif):
    global message
    SS = check_out_tarif(calls, tarif[0], 1) + check_out_tarif(SMS, tarif[1], 3) + check_out_tarif(Internet, tarif[2], 5)
    if SS == 1:
        message += MORE_CALLS[random.randrange(len(MORE_CALLS))]
    elif SS == 3:
        message += MORE_SMSs[random.randrange(len(MORE_SMSs))]
    elif SS == 4:
        message += " calls and messages"
    elif SS == 5:
        message += MORE_INTERNET[random.randrange(len(MORE_INTERNET))]
    elif SS == 8:
        message += " messages and internet"
    elif SS == 6:
        message += " "
    elif SS == 9:
        message += "смените тариф."
    else:
        message += NEUTRAL_MESSAGE[random.randrange(len(NEUTRAL_MESSAGE))]



def check_out_tarif(values, tarif_val, inc):
    global message
    for value in values:
        if value > tarif_val:
            return inc
    return 0


class Example(QtWidgets.QWidget):
    def __init__(self, lines, text, calls, sms, inet, tarif):
        super().__init__()
        self.lines = lines
        self.text = text
        self.calls = calls
        self.sms = sms
        self.inet = inet
        self.tarif = tarif
        self.window()

    def window(self):
       self.setGeometry(100,50,500,100)
       form = QtWidgets.QFormLayout()
       self.text.setReadOnly(True)
       
       arr = ['Gender', 'Age', 'Calls', 'SMS', 'Internet', 'Tarif']
       for i in range(len(arr)):
           line = QtWidgets.QLineEdit()
           self.lines[arr[i]] = line
           form.addRow(arr[i], line) 

    
       form.addRow("result", self.text)
    
       okButton = QtWidgets.QPushButton("OK")
       okButton.clicked.connect(self.listener)
    
       vbox = QtWidgets.QVBoxLayout()
       #vbox.addStretch(1)
       vbox.addLayout(form)
       vbox.addWidget(okButton)
       self.setLayout(vbox)
       self.show()
    
    def listener(self):
        sender = QtWidgets.QPushButton(self.sender())
        age = self.lines['Age'].text()
        gender = self.lines['Gender'].text()
        calls = self.lines['Calls'].text().split(',')
        sms = self.lines['SMS'].text().split(',')
        inet = self.lines['Internet'].text().split(',')
        tarif = self.lines['Tarif'].text().split(',')
        age_format = get_age(int(age), gender)
        parse_attr(calls, sms, inet, tarif)
        self.text.setText(message)
    
	
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example(dict(),QtWidgets.QTextEdit(),[], [], [], [])
    sys.exit(app.exec_())
   




#male = input('Enter your male')
#age = input("Enter your Age")
#calls = input("Calls")
#SMS = input("SMS")
#INT = input("INTERNET")
#tarif= input("TARIF")
#print(male,age,calls,SMS,INT,tarif)
#male = 'M'
#age = 60
#calls = [1,1,1]
#SMS = [1,1,1]
#INT = [1,2,3]
#tarif= [1,1,1]
#
#try:
#    age_format = get_age(int(age), male)
#    parse_attr(calls, SMS, INT, tarif)
#    print(message)
#except IOError:
#    print("ENTER ANOTHER AGE")
#    exit(1)


