
from paquete1 import modulos 

print(modulos.saludar("Edson"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t..:Agenda telefonica: {tel}..\n\tNombre: {nom}")
modulos.espereTecla()
