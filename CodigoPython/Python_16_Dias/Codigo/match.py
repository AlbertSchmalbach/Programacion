# EJEMPLO 1

# operacion = input("Eliga operacion: ").lower()
# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese otro: "))

# match operacion:
#     case "suma":
#         print(f"El resultado de la {operacion}: {n1 + n2}")

#     case "resta":
#         print(f"El resultado de la {operacion}: {n1 - n2}")

#     case "multiplicacion":
#         print(f"El resultado de la {operacion}: {n1 * n2}")

#     case "division":
#         print(f"El resultado de la {operacion}: {n1 / n2}")

# EJEMPLO 2

# error = input('Introduzca un código de error\n')
 
# if error == "200":
#     print('Todo ok.')
# elif error == "301":
#     print('Movimiento permanente de la página.')
# elif error ==  "302":
#     print('Movimiento temporal de la página.')
# elif error ==  "404":
#     print('Página no encontrada.')
# elif error ==  "500":
#     print('Error interno del servidor.')
# elif error == "503":
#     print('Servicio no disponible.')
# else:
#     print('Error no disponible.')

# EJEMPLO 3

# def provideAccess(user):
# 	return {
# 		"username": user,
# 		"password": "admin"
# 	}


# def runMatch():
# 	user = str(input("Write your username -: "))

# 	# match statement starts here .
# 	match user:
# 		case "luz saray":
# 			print("Luz Saray do not have access to the database \
# 			only for the api code.")
# 		case "mini":
# 			print(
# 				"Mini do not have access to the database , \
# 				only for the frontend code.")

# 		case "beto":
# 			print("beto have the access to the database")
# 			print(provideAccess("beto"))

# 		case _:
# 			print("You do not have any access to the code")


# if __name__ == "__main__":
# 	for _ in range(3):
# 		runMatch()

# EJEMPLO 4

from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int
	salary: int


@dataclass
class Programmer:
	name: str
	language: str
	framework: str


def runMatch(instance):
	match instance:
		case Programmer("Alberto", language="Python",
						framework="Django"):
			print("He is Alberto and he is a Python programmer and \
			uses Django Framework!")

		case Programmer("Luz Saray", "C++"):
			print("She is Luz Saray and is a C++ programmer !")

		case Person("Leo", age=5, salary=100):
			print("He is Leo and he is a kid !")

		case Programmer(name, language, framework):
			print(f"He is programmer , his name is {name} ,\
			he works in {language} and uses {framework} !")

		case Person():
			print("He is just a person !")

		case _:
			print("This person is nothiing !")


if __name__ == "__main__":
	programmer1 = Programmer("Alberto", "Python", "Django")
	programmer2 = Programmer("Luz Saray", "C++", None)
	programmer3 = Programmer("Sankalp", "Javascript", "React")
	person1 = Person("Leo", 5, 100)
	runMatch(programmer1)
	runMatch(programmer2)
	runMatch(person1)
	runMatch(programmer3)
