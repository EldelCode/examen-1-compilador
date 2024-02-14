import tkinter as tk
import ply.lex as lex

# Definición de tokens
tokens = ['RESERVADO', 'IDENTIFICADOR', 'DELIMITADOR', 'OPERADOR', 'SIMBOLO']

# Patrones para tokens
t_RESERVADO = r'(programa|suma|read|printf|int|end)'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DELIMITADOR = r'[(){};]'
t_OPERADOR = r'[=+]'
t_SIMBOLO = r'[.,"]'

# Ignorar espacios y tabs
t_ignore = ' \t'

# Crear lexer
lexer = lex.lex()

# Función para analizar texto
def analizar(texto):
    lexer.input(texto)
    return [token for token in iter(lexer.token, None)]

# Función para obtener tipo de identificador
def tipo_identificador(token):
    tipo = {
        'RESERVADO': 'RESERVADO',
        'IDENTIFICADOR': 'IDENTIFICADOR',
        'DELIMITADOR': 'DELIMITADOR',
        'OPERADOR': 'OPERADOR',
        'SIMBOLO': 'SIMBOLO'
    }
    return f"{tipo.get(token.type, 'NO VALIDO')}:    {token.value}"

# Procesar y mostrar resultados
def procesar_resultados():
    codigo_fuente = entrada_texto.get("1.0", tk.END)
    resultados = []
    contador = {'RESERVADO': 0, 'IDENTIFICADOR': 0, 'DELIMITADOR': 0, 'OPERADOR': 0, 'SIMBOLO': 0}

    for num_linea, linea in enumerate(codigo_fuente.split("\n"), 1):
        for token in analizar(linea):
            resultados.append((num_linea, tipo_identificador(token)))
            if token.type in contador:
                contador[token.type] += 1

    resultado_texto.delete("1.0", tk.END)
    for linea, identificador in resultados:
        resultado_texto.insert(tk.END, f"Línea {linea}\n{identificador}\n")

    for tipo, cuenta in contador.items():
        resultado_texto.insert(tk.END, f"\n{tipo.capitalize()} detectado: {cuenta}\n")

# Configuración de la interfaz gráfica
def configurar_interfaz():
    ventana = tk.Tk()
    ventana.geometry("750x580")
    ventana.title("Analizador lexico")
    ventana.config(bg="#12657f")

    global entrada_texto, resultado_texto
    entrada_texto = tk.Text(ventana, font=("Arial", 10), bg="white", fg="blue")
    entrada_texto.grid(row=0, column=0, sticky="nsew")
    entrada_texto.configure(insertbackground="blue")

    resultado_texto = tk.Text(ventana, font=("Arial", 10), bg="white", fg="red")
    resultado_texto.grid(row=0, column=1, sticky="nsew")

    boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 10), bg="#121b29", fg="white", command=procesar_resultados)
    boton_analizar.grid(row=1, column=0, sticky="ew")

    boton_borrar = tk.Button(ventana, text="Borrar", font=("Arial", 10), bg="#121b29", fg="white", command=lambda: entrada_texto.delete(1.0, tk.END))
    boton_borrar.grid(row=1, column=1, sticky="ew")

    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    ventana.mainloop()

if __name__ == "__main__":
    configurar_interfaz()

