# 1 mayus, 8 caracteres, 1 numero, 1 caracter especial

import os, time, re
from dotenv import load_dotenv, set_key

caracteres_especiales= "!@#$%&/?¡*+-=_"
tiene_mayus= False
tiene_char_especial= False
tiene_numero= False

load_dotenv()

password= os.getenv('password')
username= os.getenv('username')
mail= os.getenv('mail')
nombre= os.getenv('name')
edad= os.getenv('age')



def validar_correo(correo):
        partes= correo.split("@")

        if len(partes)!=2:
            return False
        
        dominio= partes[1].split(".")

        if len(dominio)< 2:
            return False
        
        for parte in partes + dominio:
            if not parte:
                return False
        return True


print("Cargando login, un momento...")
time.sleep(0.5)
          
print("""
    ---------------- MENÚ DE INICIO DE SESIÓN ----------------
        1. Nuevo registro
        2. Inicio de sesión
        3. Salir   

    """)
while True:

    try:
        opcion= int(input("Por favor ingrese una opción del menú (1 , 2, 3): "))

        match opcion:

            case 1:
                print("""
                ---------------- REGISTRO NUEVA CUENTA ----------------""")
                
                
                while True:
                    try:
                        usuario= input("Ingrese el usuario para su nueva cuenta, por favor (mínimo 5 caracteres): ")

                        if len(usuario)<5 or " " in usuario:
                            print("El usuario debe tener mayor longitud y no debe tener espacios")
                            

                        else:
                            print("Usuario registrado correctamente")
                            set_key(".env", "username", usuario)

                        correo= input("Ingrese su correo electrónico: ")

                        correo_correcto= validar_correo(correo)

                        if correo_correcto:
                            print("Correo verificado")
                            set_key(".env", "mail", correo)
                        else:
                            print("Correo incorrecto. Vuelva a intentarlo")

                        
                        
                        contrasena= input("Ingrese la contraseña que quiere usar para acceder en un futuro al sistema: ")

                        if " " in contrasena or len(contrasena)<8:
                            print("La contraseña no puede tener espacios y debe tener más de 8 caracteres. Vuelve a ingresarla")
                        
                        for char in contrasena:
                            
                            if char in caracteres_especiales:
                                tiene_char_especial = True

                            elif char.isupper():
                                tiene_mayus= True

                            elif char.isdigit():
                                tiene_numero = True

                        if tiene_char_especial and tiene_mayus and tiene_numero:
                            
                            print("Registro de contraseña exitoso.")    
                            set_key(".env", "password", contrasena)
                            break

                        else:
                            print("La contraseña debe tener 1 mayus, 8 caracteres, 1 numero, 1 caracter especial")

                            

                    except Exception as e:
                        print("Error")
                    
                                       

                        


            case 2:
                print("""
                ----------------  INICIAR SESIÓN ----------------""")

                usuario_correo= input("Ingrese su usuario o su correo eléctronico, por favor: ")
                
                contrasena= input("Ingrese la contraseña para acceder al sistema: ")

                if (username==usuario_correo or mail==usuario_correo) and password == contrasena:
                     print("Login exitoso. Gracias por usar nuestro sistema.")

                     print(f"""
                        Nombre: {nombre}
                        Edad: {edad}

                    """)
                     
                     break

                else:
                     print("No coinciden las credenciales")
            case 3:
                print("Saliendo del sistema...")
                time.sleep(0.5)
                break
            
            case _:
                print("Error")

    except ValueError:
                print("Error de tipo")
    
    

