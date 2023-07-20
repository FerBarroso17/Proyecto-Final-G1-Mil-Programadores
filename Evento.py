class Evento():
    
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

        while self.id < 0 or type(self.id) != int:
            self.id = int(input("Ingrese un id valido: "))

        while self.nombre == "":
            self.nombre = input("Ingrese un nombre valido: ")

        while self.artista == "":
            self.artista = input("Ingrese un artista valido: ")

        while self.genero == "":
            self.genero = input("Ingrese un genero valido: ")
            
        while self.id_ubicacion < 0 or type(self.id_ubicacion) != int:
            self.id_ubicacion = int(input("Ingrese un id de ubicacion valido: "))
        