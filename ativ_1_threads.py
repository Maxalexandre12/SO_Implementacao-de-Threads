import threading
import time 

def ingredientesDaReceita(ingredientes: str, tempo_preparo: int = 3):
    print('Receita de Bolo\n')
    for n in ingredientes:
        print(f"Igrediente: {n}")
        time.sleep(tempo_preparo)

def modoDePreparo(preparo: str, tempo_preparo: int = 3):
    for i in preparo:
        print(f"Preparo: {i}")
        time.sleep(tempo_preparo)

def start_threads():

    inicio = time.time()

    ingredientes = ["3 ovos",
                    "4 colheres de margarina",
                    "2 xícaras de acucar",
                    "1 e 1/2 xicara de leite",
                    "3 xícaras de farinha de trigo", 
                    "1 forma de bolo",
                    "1 forno"]

    preparo = ["1 - Bata as claras em neve e reserve.",
               "2 - Misture as gemas, com a margarina.",
               "3 - Acresecente açúcar até obter uma massa homogênea.",
               "4 - Acrescente o leite.", 
               "5 - Depois coloque farinha de trigo aos poucos, sem parar de bater.",
               "6 - Despeje a massa em uma forma grande de furo central untada e enfarinhada.",
               "7 - Asse em forno médio 180 °C, preaquecido, por aproximadamente 40 minutos"]

    thread1 = threading.Thread(target=ingredientesDaReceita, args=(ingredientes, .6))
    thread2 = threading.Thread(target=modoDePreparo, args=(preparo, .7))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    fim = time.time()
    
    print(f"\n[Threads finalizadas] - Cozimento finalizado {fim-inicio}s depois\n")

def main():
    start_threads()

if __name__ == '__main__':
    main()