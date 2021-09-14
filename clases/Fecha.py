from datetime import datetime,date,timedelta

#Clase para abstraer la fecha y gestionarla segun el contexto
class Fecha:

    #atributo tipo dict para identificar los meses basados en su numero
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

    #el init recibe un string que obtiene la fecha en texto y cierto formato para ser procesada
    def __init__(self, date_time_text):
        self.date_time_text = date_time_text
    
    # le da formato a la fecha basada en la fecha actual
    def getDateNow(self):
        now = datetime.now()
        mes = self.MonthDict.get(now.month)
        day = now.day
        self.date_format = str(day)+' de '+mes
    
    # le da fpormato a la fecha basada en la fecha de ayyer
    def getDateYesterday(self):
        date_ = date.today() - timedelta(days=1)
        mes = self.MonthDict.get(date_.month)
        day = date_.day
        self.date_format = str(day)+' de '+mes

    # Metodo que identifica si el periodo de tiempo que marca la fecha
    # Se refiere a el dia de ayer o de hoy para darle el formato correspondiente.
    # En caso que no sea ni de hoy ni de ayer se deja la fecha coMo esta
    def validate_yesterday_or_today(self):
        if 'hora' in self.date_time_text\
                or 'min' in self.date_time_text\
                    or 'seg' in self.date_time_text: # si esto se cumple significa que se publico hoy
            self.getDateNow()

        elif 'yer' in self.date_time_text: #si tiene la palabra yer de 'AYER' significa que es un post publicado ayer
            self.getDateYesterday()

        else: #sino no se necesita modificar el formato
            self.date_format = self.date_time_text