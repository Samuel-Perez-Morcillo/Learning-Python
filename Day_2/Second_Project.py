# El jefe me ha pedido que cree un programa que les calcule a los empleados
# cual es el total de dinero recibido por sus comisiones teniendo en cuenta que todos
# los empleados reciben un 13 % de comisiones.


print("Calcula cuanto te Debemos en Comisiones")
name = input("Introduzca su Nombre: ")
surname = input("Introduzca su apellido: ")
total_income = int(input("Cuanto dinero ha ganado la empresa gracias a tus ventas este mes\n"))

print(f"Perfecto,"
      f"Acorde a lo dispuesto en el convenio\n "
      f"Usted {name} {surname}\n"
      f" gracias a ingresar {total_income}€ \n "
      f"recibirá un 13% del total, es decir {round(total_income * 13 / 100, 2)} €")
