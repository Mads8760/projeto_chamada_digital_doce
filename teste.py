import os
print("--- O QUE TEM NA PASTA APP? ---")
try:
    arquivos = os.listdir("app")
    print(arquivos)
except Exception as e:
    print(f"Erro ao ler pasta: {e}")