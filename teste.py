import datetime
import time

# Hora atual
hora_inicial = time.time()
print(f"Hora inicial: {datetime.datetime.now()}")
# Enquanto não se passarem 60 segundos
while True:
    # Hora atual
    hora_atual = time.time()
    
    # Verifica se já se passaram 60 segundos
    if hora_atual - hora_inicial >= 60:
        print("O tempo acabou!")
        break  # Sai do laço após 60 segundos
    else:
        time.sleep(1)  # Espera 1 segundo para não sobrecarregar o processador
        print(f"Passaram {int(hora_atual) - int(hora_inicial)} segundos")

print(datetime.datetime.now())
