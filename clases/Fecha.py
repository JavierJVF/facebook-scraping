from datetime import datetime,date,timedelta
class Fecha:
    MonthDict = {
        1:'Enero',
        2:'Febrero',
        3:'Marzo',
        4:'Abril',
        5:'Mayo',
        6:'Junio',
        7:'Julio',
        8:'Agosto',
        9:'Septiembre',
        10:'Octubre',
        11:'Noviembre',
        12:'Diciembre',
    }

    def __init__(self, date_time_text):
        self.date_time_text = date_time_text
    
    def getDateNow(self):
        now = datetime.now()
        mes = self.MonthDict.get(now.month)
        day = now.day
        self.date_format = str(day)+' de '+mes
    
    def getDateYesterday(self):
        date_ = date.today() - timedelta(days=1)
        mes = self.MonthDict.get(date_.month)
        day = date_.day
        self.date_format = str(day)+' de '+mes

    def validate_yesterday_or_today(self):
        if 'hora' in self.date_time_text\
                or 'min' in self.date_time_text\
                    or 'seg' in self.date_time_text:
            self.getDateNow()

        elif 'yer' in self.date_time_text:
            self.getDateYesterday()

        else:
            self.date_format = self.date_time_text