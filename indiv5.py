def integrar_lista(lista):
    try:
        resultado = 0
        for i in range(len(lista)):
            resultado += lista[i]
        return resultado
    except IndexError:
        print("Error: IndexError. El índice está fuera del rango de la lista.")
        print("Solución: Ver que los índices utilizados estén dentro del rango válido de la lista.")
    except TypeError:
        print("Error: TypeError. Se esperaba un tipo de dato numérico en la lista.")
        print("Solución: ver que todos los elementos de la lista sean números.")
    except KeyError:
        print("Error: KeyError. La clave no se encuentra en el diccionario.")
        print("Solución: Ver  que la clave utilizada exista en el diccionario.")
    finally:
        print(" 'finally' ejecutado.")

# Ejemplo de uso:
lista_numeros = [1, 2, 3, 4, 5]
diccionario = {'a': 1, 'b': 2, 'c': 3}

integrar_lista(lista_numeros)
integrar_lista(diccionario['d'])

#La utilidad de manejar los errores en la programación permite anticiparse y gestionar situaciones inesperadas que pueden surgir durante la ejecución de un programa. 
# Al manejar los errores, se puede ver información útil al usuario sobre lo que salió mal y cómo solucionarlo,
#  lo que mejora la experiencia del usuario y facilita la lectura del programa. 
# Además, el manejo adecuado de errores evita que el programa se detenga abruptamente y permite que continúe ejecutándose o realice acciones específicas en respuesta a cada tipo de error. 
