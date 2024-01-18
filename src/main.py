import psutil
import time
import os.path

# Função para iniciar monitoramento de memória
def monitorar_memoria(pid):
    processo = psutil.Process(pid)

    print(f"Monitorando a memória do processo {pid}...")

    try:
        while True:
            # Obter informações sobre a memória
            uso_memoria = processo.memory_info()

            # Exibir informações sobre o uso de memória
            print(f"Uso de memória (RSS): {uso_memoria.rss / (1024 * 1024):.2f} MB")
            print(f"Uso de memória (VMS): {uso_memoria.vms / (1024 * 1024):.2f} MB")
            
            # Aguardar o próximo intervalo
            time.sleep(intervalo)

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")

if __name__ == "__main__":
    # Insira o PID do processo que você deseja monitorar
    pid_alvo = int(input("Digite o PID do processo a ser monitorado: "))
    # Insira o tempo de intervalo de recebimento de dados
    intervalo = float(input("Digite o intervalo desejado (em segundos):"))

    # Verificar se o PID é válido
    if psutil.pid_exists(pid_alvo):
        monitorar_memoria(pid_alvo)
    else:
        print(f"O PID {pid_alvo} não corresponde a nenhum processo em execução.")
