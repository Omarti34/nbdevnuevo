# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_tarea.ipynb.

# %% auto 0
__all__ = ['Tarea']

# %% ../nbs/01_tarea.ipynb 4
class Tarea:
    def __init__(self, nombre:str, #aqui va el nombre
                    descripcion:str,  #aqui va la descripcion
                    fecha_entrega:str,# aqui la fecha
                    entregado:bool# aqui si se entrego o no la cosa 
                )-> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.entregado = False

    def __str__(self) ->str:
        return f"{self.nombre} {self.descripcion} {self.fecha_entrega} "
    __repr__=__str__
    

# %% ../nbs/01_tarea.ipynb 7
import nbdev; nbdev.nbdev_export()
