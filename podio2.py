def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        primeiro_colocado = tempo_chegada1
        if (tempo_chegada2 < tempo_chegada3):
            segundo_colocado = tempo_chegada2
            terceiro_colocado = tempo_chegada3
        else:
            segundo_colocado = tempo_chegada3
            terceiro_colocado = tempo_chegada2
    elif tempo_chegada2 < tempo_chegada3:
        terceiro_colocado = tempo_chegada2
        if tempo_chegada1 < tempo_chegada3:
            segundo_colocado = tempo_chegada1
            primeiro_colocado = tempo_chegada3
        else:
            segundo_colocado = tempo_chegada3
            primeiro_colocado = tempo_chegada1
    else:
        terceiro_colocado = tempo_chegada3
        if tempo_chegada1 < tempo_chegada2:
            segundo_colocado = tempo_chegada1
            primeiro_colocado = tempo_chegada2
        else:
            segundo_colocado = tempo_chegada2
            primeiro_colocado = tempo_chegada1

    podio = f"1 - {menor} minutos\n2 - {meio} minutos\n3 - {maior} minutos\n"
        
    return (podio)

print(podio_olimpico(1, 3, 2))


        
        