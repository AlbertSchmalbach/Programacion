class Producto(): 
  def __init__(self, nombre, valor, cantidad):
   self.__nombre = nombre 
   self.__valor = valor 
   self.__cantidad = cantidad

  def __repr__(self):
   return self.__nombre

  def get_nombre(self): 
    return self.__nombre

  def get_valor(self):
   return self.__valor

  def get_cantidad(self):
   return self.__cantidad

  def impresion(self): 
    return "nombre:%s valor:%s cantidad:%s" % (self.__nombre, self.__valor, self.__cantidad)
