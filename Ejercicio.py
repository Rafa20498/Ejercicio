class persona: 
    def __init__(self, Nombre = "", edad = 0, dni = 0, sexo ="M", peso = 0.0,altura = 0.0 ):
        self.Nombre = Nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura =altura
    def calcular_imc(self):
        imc = self.peso/(self.altura**2)
        if imc >= 20:
            print("Bajopeso ")
            return - 1
        elif imc >= 20 and imc <= 25:
            print("Peso Ideal ") 
            return 0 
        elif imc >= 25:
            print("Sobrepeso ")
            return 1
        else:
                print("error")
    def es_mayor_edad(self):
        if self.edad > 18:
            print("Es mayor de edad ")
            return True
        else:
            print("No es mayor de edad") 
            return False
    def comprobar_sexo(self):
        if sexo == self.sexo:
            return True 
        else:
            return False
    def toString(self):
        return "Nombre: " + self.Nombre + "\nedad: " + str(self.edad) + "\nDNI: " +str(self.dni)
        

Nombre = input("Ingrese el nombre ")
edad = int(input("Ingrese edad "))
dni = int(input("Ingrese su dni "))
sexo = input("Ingrese su sexo ") 
peso = float(input("Ingrese su peso "))
altura = float(input("Ingrese su altura "))
objetopersona = persona(Nombre, edad, dni, sexo, peso, altura)
while(True):
    print("Ingrese datos ")
    print("1- calcular IMC ")
    print("2- Comprobar si es mayor de edad ")
    print("3- Comprobar sexo ")
    print("4- Mostrar todos los datos ")
    opcion = input("Ingrese uno ")
    match opcion:
        case"1":
            print(objetopersona.calcular_imc())
        case"2":
            print(objetopersona.es_mayor_edad()) 
        case"3":
            print(objetopersona.comprobar_sexo())
        case"4":
            print(objetopersona.toString())
        case _:
            break





pass