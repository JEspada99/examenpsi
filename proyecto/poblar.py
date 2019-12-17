import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')

import datetime

import django
django.setup()
from aplicacion.models import Camion, Objeto, Ruta

def poblar():
    camion_examples = [
        {'nombreC': 'camion_01'},
        {'nombreC': 'camion_02'},
        {'nombreC': 'camion_03'}]

    objetos_examples = [
        {'nombreO': 'objeto_01'},
        {'nombreO': 'objeto_02'},
        {'nombreO': 'objeto_03'},
        {'nombreO': 'objeto_04'}]


    for value in camion_examples:
        add_camion(value['nombreC'])


    for value in objetos_examples:
        add_objetos(value['nombreO'])

    add_ruta(Camion.objects.get(nombreC='camion_01'), Objeto.objects.get(nombreO='objeto_01'))
    add_ruta(Camion.objects.get(nombreC='camion_02'), Objeto.objects.get(nombreO='objeto_02'))
    add_ruta(Camion.objects.get(nombreC='camion_02'), Objeto.objects.get(nombreO='objeto_03'))
    add_ruta(Camion.objects.get(nombreC='camion_02'), Objeto.objects.get(nombreO='objeto_04'))


def add_camion(nombreC):
    c = Camion(nombreC=nombreC)
    c.save()
    return c


def add_objetos(nombreO):
    o = Objeto(nombreO=nombreO)
    o.save()
    return o


def add_ruta(camion, objeto):
    r = Ruta(camion=camion, objeto=objeto)
    r.save()
    return r


if __name__ == "__main__":
    poblar()

    

