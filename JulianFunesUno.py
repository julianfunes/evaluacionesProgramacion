print("este programa calcula el promedio de notas de un estudiante")
print("el estudiante solo aprobara si tine un promedio mayor a 7")
# crea una lista vacia para guardar las materias y notas ingresadas
notas = []
materias = []

print("Ingrese las materias y sus notas (escriba 'salir' para terminar)")
#crea un bucle que pide ingresar materias y notas
while True:
# Pedir al usuario el nombre de la materia
    materia = input("Nombre de la materia📋: ")
#transcribe el texto a minuscula para evitar errores de escritura
    if materia.lower() == "salir":
        break

# Pedir la nota para esa materia
    nota = input("Nota📊 (entre 0 y 10): ")

    try:
        # Intentar convertir la nota a número decimal
        nota = float(nota)
# verifica si la nota esta entre 0 y 10
        if 0 <= nota <= 10:
            materias.append(materia)
            notas.append(nota)
        else:
#si no esta dentro de 0 y 10 muestra un mensaje de error
            print("❌ La nota debe estar entre 0 y 10.")
    except:
 # Si la conversión falla (por ejemplo, si el usuario escribe letras), mostrar error
        print("❌ Entrada no válida. Ingrese un número.")

# Mostrar los resultados
if notas:
    print("\n📋 Materias y notas:")
    for i in range(len(materias)):
        print(f"{materias[i]}: {notas[i]}")

 # Calcular el promedio de notas
    promedio = sum(notas) / len(notas)
    print(f"📊 Promedio de notas: {promedio:.1f}")
    print ("✅ el estudiante aprobo")
    print("❌el estudiante desaprobo")