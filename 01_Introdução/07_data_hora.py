import time
from datetime import datetime
from pytz import timezone

# utilizando a Lib TIME
# utilizando a Lib DATETIME
# utilizando a Lib PYTZ

print (time.localtime())

print(time.localtime().tm_year)

#utilizando a lib DATETIME 
print(datetime.today())
print(datetime.now().date())
print(datetime.now.time())

#utilizando a Lib PYTZ 

dthr= datetime.now()
fuso_br=timezone('America/Sao_Paulo') 
sp=dthr.astimezone(fuso_br) 
sp_formatado = sp.dtrfilme('%d | %m | %Y  %H:%M') 
print(sp) 
print(sp_formatado) 