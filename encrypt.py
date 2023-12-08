import hashlib

def encriptar_texto(texto):
  # Encriptar el texto usando SHA-256
  sha256 = hashlib.sha256()
  sha256.update(texto.encode('utf-8'))
  return sha256.hexdigest()

def procesar_archivo(entrada, salida):
  with open(entrada, 'r') as archivo_entrada, open(salida, 'w') as archivo_salida:
    for linea in archivo_entrada:
      # Dividir la línea en el número y el texto
      numero, texto = linea.strip().split(':', 1)
      
      # Encriptar el texto o agregar una línea vacía si el texto es vacío
      resultado = encriptar_texto(texto) if texto else ''

      # Escribir el resultado en el nuevo archivo
      archivo_salida.write(f"{numero}:{resultado}\n")

if __name__ == "__main__":
  archivo_entrada = "/outputs/plain.txt"
  archivo_salida = "new_passwords.txt"

  procesar_archivo(archivo_entrada, archivo_salida)
