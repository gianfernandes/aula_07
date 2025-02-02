from typing import List

def calcular_media(valores: List[float]) -> float:
  return sum(valores) / len(valores)

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
  resultado = []
  for valor in valores:
    if valor > limite:
      resultado.append(valor)
  return resultado

def contar_valores_unicos(lista: List[int]) -> int:
  return len(set(lista))

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
  return [(9/5) * temp + 32 for temp in temperaturas_celsius]