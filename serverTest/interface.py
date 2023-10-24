testeDado = 10

def sendData():
    dataRcv = input("insira uma das opções abaixo:\n1 - printa 1\n2 - printa 2\n3 - printa 3\nsair - sair do programa\n\n")


    #while dataRcv!="4":
        
    if dataRcv == "1":
        #print("numero 1")
        return dataRcv
    elif dataRcv == "2":
        #print("numero 2")
        return dataRcv

    elif dataRcv == "3":
        #print("numero 3")
        return dataRcv
    elif dataRcv == "sair":
        print("saindo!")
        return dataRcv
    else:
        
        print("Não entendi o que você digitou... Digite uma das opções do menu")
        return dataRcv
    #dataSend = None
    # dataRcv = input("insira um numero de 1 a 3, e 4 para sair do programa\n")
