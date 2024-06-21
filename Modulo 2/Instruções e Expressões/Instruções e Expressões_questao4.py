
DISTANCIA_KM = 42.195  
TEMPO_HORAS = 3  


distancia_metros = DISTANCIA_KM * 1000  
tempo_segundos = TEMPO_HORAS * 3600  


velocidade_media = distancia_metros / tempo_segundos  


print(f"Para completar a maratona em {TEMPO_HORAS} horas, a velocidade média necessária é de {velocidade_media:.2f} metros por segundo.")
