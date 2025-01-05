from dataclasses import dataclass
from typing import List

@dataclass
class FrequenciaGenotipica:
    AA: float
    Aa: float
    aa: float
    

@dataclass
class FrequenciaAlelica:
    A: float
    a: float


# Dado uma frequencia genotipica, encontramos a frequencia alelica
def FrequenciaGenotipicaToAlelica(frequencia_gen: FrequenciaGenotipica) -> FrequenciaAlelica:
    half_heter_freq = (frequencia_gen.Aa/2)
    return FrequenciaAlelica(
        A=round(frequencia_gen.AA + half_heter_freq,4),
        a=round(frequencia_gen.aa + half_heter_freq,4),
    )
    
    

def simularGeracao(frequencia_ale: FrequenciaAlelica):
    return FrequenciaGenotipica(
        AA=round(frequencia_ale.A ** 2,4),
        Aa= round(2 * frequencia_ale.A * frequencia_ale.a,4),
        aa= round(frequencia_ale.a ** 2,4),
    )
    
def verificarEquilibrio(populacao: FrequenciaGenotipica, qtd_gen=3):
    geracao: List[FrequenciaGenotipica] = list()
    geracao.append(populacao)
    
    for i in range(qtd_gen):
        frequencia_alelica = FrequenciaGenotipicaToAlelica(populacao)
        populacao = simularGeracao(frequencia_ale=frequencia_alelica)
        geracao.append(populacao)
    return geracao


"""
    População de ervilhas, a frequência do alelo 'A' é 0,6(60%) e a frequência do alelo 'a' é 0,4(40%). 
    As frequências genotípicas esperadas
"""
A = 0.6 # lisa
a = 0.4 # rugosa

frequencia_alelica = FrequenciaAlelica(A,a)
g_parental = simularGeracao(frequencia_alelica)

geracoes = verificarEquilibrio(populacao=g_parental,qtd_gen=3)

for i, geracao in enumerate(geracoes):
    
    if i == 0:
        print(f"Geração parental: AA: {geracao.AA}, Aa: {geracao.Aa}, aa: {geracao.aa}")
        continue
    print(f"Geração F{i}: AA: {geracao.AA}, Aa: {geracao.Aa}, aa: {geracao.aa}")