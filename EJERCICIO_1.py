import tkinter as tk
import math

# Clase para manejar las notas y sus cálculos
class Notas:
    def __init__(self):
        self._lista_notas = []

    def agregar(self, valor: float):
        self._lista_notas.append(valor)

    def calcularPromedio(self) -> float:
        if len(self._lista_notas) == 0:
            return 0
        return sum(self._lista_notas) / len(self._lista_notas)

    def calcularDesviacion(self) -> float:
        if len(self._lista_notas) == 0:
            return 0
        promedio = self.calcularPromedio()
        suma_cuadrados = sum((n - promedio) ** 2 for n in self._lista_notas)
        return math.sqrt(suma_cuadrados / len(self._lista_notas))

    def calcularMenorValor(self) -> float:
        if len(self._lista_notas) == 0:
            return 0
        return min(self._lista_notas)

    def calcularMayorValor(self) -> float:
        if len(self._lista_notas) == 0:
            return 0
        return max(self._lista_notas)


# Clase principal de la interfaz gráfica
class VentanaPrincipal:
    def __init__(self):
        self._ventana = tk.Tk()
        self._ventana.title("Notas")
        self._ventana.geometry("300x320")
        self._ventana.resizable(False, False)

        self._notas = Notas()
        self._entradas = []

        for i in range(5):
            tk.Label(self._ventana, text=f"Nota {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
            entrada = tk.Entry(self._ventana, width=10)
            entrada.grid(row=i, column=1)
            self._entradas.append(entrada)

        self._lbl_promedio = tk.Label(self._ventana, text="Promedio = ")
        self._lbl_promedio.grid(row=6, column=0, columnspan=2, sticky="w", padx=10)

        self._lbl_desv = tk.Label(self._ventana, text="Desviación estándar = ")
        self._lbl_desv.grid(row=7, column=0, columnspan=2, sticky="w", padx=10)

        self._lbl_mayor = tk.Label(self._ventana, text="Valor mayor = ")
        self._lbl_mayor.grid(row=8, column=0, columnspan=2, sticky="w", padx=10)

        self._lbl_menor = tk.Label(self._ventana, text="Valor menor = ")
        self._lbl_menor.grid(row=9, column=0, columnspan=2, sticky="w", padx=10)

        tk.Button(self._ventana, text="Calcular", command=self.calcular).grid(row=5, column=0, pady=10)
        tk.Button(self._ventana, text="Limpiar", command=self.limpiar).grid(row=5, column=1, pady=10)

    def calcular(self):
        self._notas = Notas()
        for e in self._entradas:
            valor = e.get()
            if valor:
                self._notas.agregar(float(valor))

        promedio = self._notas.calcularPromedio()
        desviacion = self._notas.calcularDesviacion()
        menor = self._notas.calcularMenorValor()
        mayor = self._notas.calcularMayorValor()

        self._lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
        self._lbl_desv.config(text=f"Desviación estándar = {desviacion:.2f}")
        self._lbl_mayor.config(text=f"Valor mayor = {mayor}")
        self._lbl_menor.config(text=f"Valor menor = {menor}")

    def limpiar(self):
        for e in self._entradas:
            e.delete(0, tk.END)
        self._lbl_promedio.config(text="Promedio = ")
        self._lbl_desv.config(text="Desviación estándar = ")
        self._lbl_mayor.config(text="Valor mayor = ")
        self._lbl_menor.config(text="Valor menor = ")

    def mainloop(self):
        self._ventana.mainloop()


# Clase que ejecuta el programa
class Principal:
    @staticmethod
    def main():
        app = VentanaPrincipal()
        app.mainloop()


# Ejecutar el programa
if __name__ == "__main__":
    Principal.main()
