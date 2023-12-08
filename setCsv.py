import sys
import csv

def generar_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w', newline='') as f_out:
        csv_writer = csv.writer(f_out)
        csv_writer.writerow(['numero', 'string'])

        for numero, linea in enumerate(f_in, start=1):
            # Tomar la línea sin espacios en blanco al principio y al final
            valor = linea.strip()
            
            # Escribir en el archivo CSV
            csv_writer.writerow([numero, valor])

    print(f"La conversión se ha completado. El archivo CSV se encuentra en: {archivo_salida}")

if __name__ == "__main__":
    # Verificar si se proporciona el nombre del archivo de entrada
    if len(sys.argv) != 3:
        print("Uso: python script.py archivo_entrada.txt archivo_salida.csv")
        sys.exit(1)

    # Nombre del archivo de entrada
    archivo_entrada = sys.argv[1]

    # Nombre del archivo de salida CSV
    archivo_salida = sys.argv[2]

    # Llamar a la función para generar el CSV
    generar_csv(archivo_entrada, archivo_salida)
