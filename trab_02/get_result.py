import numpy as np
import sys


def calculate_result(path):
    print(f"Calculando resultados de {path}...")
    results_file = open(f"{sys.path[0]}/{path}", "r")
    results = results_file.readlines()
    results = np.array(results, dtype=np.float32)
    results_file.close()

    print(f"\nMédia: {np.average(results)}")
    print(f"Desvio padrão: {np.std(results)}\n")
