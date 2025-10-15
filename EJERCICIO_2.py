import tkinter as tk
import math


# Clase base
class FiguraGeometrica:
    def __init__(self):
        self._superficie = 0.0
        self._volumen = 0.0

    def get_superficie(self):
        return self._superficie

    def get_volumen(self):
        return self._volumen


# Clase Cilindro
class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self._radio = radio
        self._altura = altura

    def calcular_volumen(self):
        return math.pi * (self._radio ** 2) * self._altura

    def calcular_superficie(self):
        return 2 * math.pi * self._radio * (self._altura + self._radio)


# Clase Esfera
class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self._radio = radio

    def calcular_volumen(self):
        return (4 / 3) * math.pi * (self._radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self._radio ** 2)


# Clase Pirámide
class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self._base = base
        self._altura = altura
        self._apotema = apotema

    def calcular_volumen(self):
        return (1 / 3) * (self._base ** 2) * self._altura

    def calcular_superficie(self):
        return (self._base ** 2) + (2 * self._base * self._apotema / 2)


# Ventana para el Cilindro
class VentanaCilindro:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cilindro")
        self.ventana.geometry("260x200")
        self.ventana.resizable(False, False)

        tk.Label(self.ventana, text="Radio (cms) = ").place(x=20, y=20)
        tk.Label(self.ventana, text="Altura (cms) = ").place(x=20, y=50)

        self.radio = tk.Entry(self.ventana)
        self.radio.place(x=100, y=20)
        self.altura = tk.Entry(self.ventana)
        self.altura.place(x=100, y=50)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).place(x=90, y=80)

        self.lbl_vol = tk.Label(self.ventana, text="Volumen (cm3) = ")
        self.lbl_vol.place(x=20, y=120)
        self.lbl_sup = tk.Label(self.ventana, text="Superficie (cm2) = ")
        self.lbl_sup.place(x=20, y=150)

    def calcular(self):
        radio = float(self.radio.get())
        altura = float(self.altura.get())
        c = Cilindro(radio, altura)
        self.lbl_vol.config(text=f"Volumen (cm3) = {c.calcular_volumen():.2f}")
        self.lbl_sup.config(text=f"Superficie (cm2) = {c.calcular_superficie():.2f}")


# Ventana para la Esfera
class VentanaEsfera:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Esfera")
        self.ventana.geometry("260x180")
        self.ventana.resizable(False, False)

        tk.Label(self.ventana, text="Radio (cms) = ").place(x=20, y=20)
        self.radio = tk.Entry(self.ventana)
        self.radio.place(x=100, y=20)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).place(x=90, y=60)

        self.lbl_vol = tk.Label(self.ventana, text="Volumen (cm3) = ")
        self.lbl_vol.place(x=20, y=100)
        self.lbl_sup = tk.Label(self.ventana, text="Superficie (cm2) = ")
        self.lbl_sup.place(x=20, y=130)

    def calcular(self):
        radio = float(self.radio.get())
        e = Esfera(radio)
        self.lbl_vol.config(text=f"Volumen (cm3) = {e.calcular_volumen():.2f}")
        self.lbl_sup.config(text=f"Superficie (cm2) = {e.calcular_superficie():.2f}")


# Ventana para la Pirámide
class VentanaPiramide:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Pirámide")
        self.ventana.geometry("260x220")
        self.ventana.resizable(False, False)

        tk.Label(self.ventana, text="Base (cms) = ").place(x=20, y=20)
        tk.Label(self.ventana, text="Altura (cms) = ").place(x=20, y=50)
        tk.Label(self.ventana, text="Apotema (cms) = ").place(x=20, y=80)

        self.base = tk.Entry(self.ventana)
        self.base.place(x=120, y=20)
        self.altura = tk.Entry(self.ventana)
        self.altura.place(x=120, y=50)
        self.apotema = tk.Entry(self.ventana)
        self.apotema.place(x=120, y=80)

        tk.Button(self.ventana, text="Calcular", command=self.calcular).place(x=90, y=110)

        self.lbl_vol = tk.Label(self.ventana, text="Volumen (cm3) = ")
        self.lbl_vol.place(x=20, y=150)
        self.lbl_sup = tk.Label(self.ventana, text="Superficie (cm2) = ")
        self.lbl_sup.place(x=20, y=180)

    def calcular(self):
        base = float(self.base.get())
        altura = float(self.altura.get())
        apotema = float(self.apotema.get())
        p = Piramide(base, altura, apotema)
        self.lbl_vol.config(text=f"Volumen (cm3) = {p.calcular_volumen():.2f}")
        self.lbl_sup.config(text=f"Superficie (cm2) = {p.calcular_superficie():.2f}")


# Ventana principal
class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Figuras")
        self.ventana.geometry("280x100")
        self.ventana.resizable(False, False)

        tk.Button(self.ventana, text="Cilindro", command=VentanaCilindro).place(x=20, y=30, width=70)
        tk.Button(self.ventana, text="Esfera", command=VentanaEsfera).place(x=110, y=30, width=60)
        tk.Button(self.ventana, text="Pirámide", command=VentanaPiramide).place(x=190, y=30, width=70)

        self.ventana.mainloop()


# Ejecucción del programa
if __name__ == "__main__":
    VentanaPrincipal()
