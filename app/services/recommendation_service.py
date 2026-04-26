def recomendar_curso(perfil):
    matematica = perfil.matematica
    pratico = perfil.pratico
    tempo = perfil.tempo

    if matematica < 4 and pratico > 6:
        return "Análise e Desenvolvimento de Sistemas (ADS)"
    
    if matematica > 7:
        return "Ciência da Computação"
    
    if tempo == "curto":
        return "ADS"
    
    return "Sistemas de Informação"