import math, random
import RSA
import El_gamal as GA

def leer():
    archivo=open('mensajerecibido.txt.','r')
    a=archivo.read()
    archivo.close()
    return a

def escribir(texto):
    final=texto
    archivo=open('mensajeentrada.txt','w')
    archivo.write(final)
    archivo.close()
    
#main rsa
def main():
    print('Comunicacion con RSA\n')
    p = 313
    q = 409
    n = RSA.generarN(p, q) #valor publico
    phi_n = RSA.generarN(p - 1, q - 1) 
    valor_e = RSA.e_value(phi_n) #valor publico

    try:
        res = RSA.find_mod_inv(valor_e, phi_n) #valor de la llave privada (d)
        print('proceso realizado exitoso')

    except:
        print('El valor del inverso no existe.\n')

    #valores publicos
    print('clave publica(n, e)\n')
    print(f' valor de n generado: {n}\n',
          f'valor de e generado: {valor_e}\n')
    
    mensaje = int(input('Ingresa el mensaje numerico que desea enviar--> '))

    M_cifrado = cifrar(mensaje, valor_e, n)
    escribir(M_cifrado)

    x = leer()
    M_descifrado = descifrar(x, res, n)

    print('Comunicacion con el gamal\n')
    g = random.randint(1, 1000)
    a = 369 #clave privada del emisor
    b = 693 #clave privada del receptor
    k = (g**a) % p
    clave_publica = (g, p, k)
    print(f'se genero la siguiente clave publica: {clave_publica}')
    m = int(input('ingresar el mensaje que desea enviar--> '))
    #cifrando
    y1 = (g**b) % p
    y2 = ((k**b) * m) % p
    #descifrando
    m2 = (y1**(p-1-a) * y2) % p
    print(f'El mensaje descifrado es el siguiente: {m2}\n')

main()
    

