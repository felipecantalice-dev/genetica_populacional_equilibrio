
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
        
    

populacao = FrequenciaGenotipica(AA=0.32, Aa=0.64, aa=0.04)
# populacao = FrequenciaGenotipica(AA=0.36, Aa=0.48, aa=0.16)
print(verificarEquilibrio(populacao=populacao,qtd_gen=3))
