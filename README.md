# O equilíbrio de Hardy-Weinberg
Princípio que afirma que a variação genética em uma população permanecerá constante de uma geração para a próxima na ausência de fatores perturbadores.

 https://www.portalsaofrancisco.com.br/biologia/equilibrio-de-hardy-weinberg


 Dado uma população com AA, Aa e aa frequencias, determinar se está em equilibrio


## Ferramentas
* Python
* Jupyter notebook

## Bibliotecas
* Pandas
* Matplotlib

## Classes

```python
@dataclass
class FrequenciaGenotipica:
    AA: float
    Aa: float
    aa: float
    

@dataclass
class FrequenciaAlelica:
    A: float
    a: float
```

## Funções

```python
# Calcula a frequencia alélica
def FrequenciaGenotipicaToAlelica(frequencia_gen: FrequenciaGenotipica) -> FrequenciaAlelica:
    half_heter_freq = (frequencia_gen.Aa/2)
    return FrequenciaAlelica(
        A=round(frequencia_gen.AA + half_heter_freq,4),
        a=round(frequencia_gen.aa + half_heter_freq,4),
    )
    
    
# Simula a próxima geração
def simularGeracao(frequencia_ale: FrequenciaAlelica):
    return FrequenciaGenotipica(
        AA=round(frequencia_ale.A ** 2,4),
        Aa= round(2 * frequencia_ale.A * frequencia_ale.a,4),
        aa= round(frequencia_ale.a ** 2,4),
    )

# Verifica se está em equilibrio em n gerações
def verificarEquilibrio(populacao: FrequenciaGenotipica, qtd_gen=3):
    geracao: List[FrequenciaGenotipica] = list()
    geracao.append(populacao)
    
    for i in range(qtd_gen):
        frequencia_alelica = FrequenciaGenotipicaToAlelica(populacao)
        populacao = simularGeracao(frequencia_ale=frequencia_alelica)
        geracao.append(populacao)
    return geracao
```

## Caso: Geração de ervilhas

```python
"""
    População de ervilhas, a frequência do alelo A (p) é 0,6 e a frequência do alelo a (q) é 0,4. 
    As frequências genotípicas esperadas
"""
A = 0.6
a = 0.4

frequencia_alelica = FrequenciaAlelica(A,a)
g_parental = simularGeracao(frequencia_alelica)

geracoes = verificarEquilibrio(populacao=g_parental,qtd_gen=3)

for i, geracao in enumerate(geracoes):
    
    if i == 0:
        print(f"Geração parental: AA: {geracao.AA}, Aa: {geracao.Aa}, aa: {geracao.aa}")
        continue
    print(f"Geração F{i}: AA: {geracao.AA}, Aa: {geracao.Aa}, aa: {geracao.aa}")
```