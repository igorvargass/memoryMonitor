import psutil
import time
from datetime import datetime, timedelta

# Salvando em arquivo .log
def savefile(ftxt, fname, fprocess):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestampParaNomeArquivo = datetime.now().strftime("%Y-%m-%d")
    
    with open(fname + '_PID' + fprocess + '_' + timestampParaNomeArquivo + '.log', "a") as f:
        f.write(f"{timestamp} | {ftxt}\n")

# Função para iniciar monitoramento de memória
def monitorar_memoria(pid, intervalo):
    processo = psutil.Process(pid)

    print(f"Monitorando a memoria do processo {pid}...")

    # Inicializa a última marcação de hora
    ultima_marca = datetime.now()

    try:
        while True:
            # Obter informações sobre a memória
            uso_memoria = processo.memory_info()
            nome_pid = processo.name()

            # Exibir informações sobre o uso de memória
            dado1 = f"Uso de memoria (RSS): {uso_memoria.rss / (1024 * 1024):.2f} MB"
            dado2 = f"Uso de memoria (VMS): {uso_memoria.vms / (1024 * 1024):.2f} MB"

            print(dado1)
            print(dado2)

            # Salvar informações no arquivo
            savefile(dado1, nome_pid, str(pid))
            savefile(dado2, nome_pid, str(pid))

            # Verificar se passou 1 hora desde a última marcação
            if datetime.now() - ultima_marca > timedelta(hours=1):
                marca = f"Marcacao de hora: {datetime.now().strftime('%H:%M:%S')}"
                print(marca)
                savefile(marca, nome_pid, str(pid))
                ultima_marca = datetime.now()

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
        monitorar_memoria(pid_alvo, intervalo)
    else:
        print(f"O PID {pid_alvo} nao corresponde a nenhum processo em execucao.")
