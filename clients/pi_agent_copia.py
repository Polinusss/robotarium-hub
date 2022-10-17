
# leer el archivo de texto 
with open('archivo1.txt') as archivo1:
    lines = [line for line in archivo1]
AGENT_ID =lines[1] 
AGENT_NAME = lines[2] 
AGENT_IP = lines[3] 
AGENT_PORT = lines[4] 
SERVER_IP = lines[5] 
print(AGENT_ID)
print(AGENT_NAME)
print(AGENT_IP)
print(AGENT_PORT)
print(SERVER_IP)
archivo1.close()


