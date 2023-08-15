from django.test import TestCase
from tienda.models import Orden
from datetime import datetime
from django.utils import timezone
import zoneinfo
# Create your tests here.
class TiendaViewsTests(TestCase):

    def test_v_index(self):
        '''
            Debe entregar todos los registros 
            si no existen filtros
        '''
        respuesta = self.client.get("/") #es cuando el final aparece gitpod.io/
        ords = respuesta.context["ordenes"]
        self.assertEqual(0, len(ords))
        #preparando las condiciones
        newo = Orden()
        newo.client = "erika"
        newo.fecha = "2023-12-12"
        newo.fecha_envio = "2023-12-12"
        newo.direccion = "ciudad azulona"
        newo.save()

        respuesta = self.client.get("/") #es cuando el final aparece gitpod.io/
        ords = respuesta.context["ordenes"]
        self.assertEqual(1, len(ords))

    def test_v_index_filtros(self):
        '''
            Entrega los registros con filtros de fecha
        '''
        newo = Orden()
        newo.client = "surge"
        newo.fecha = "2022-12-12"
        newo.fecha_envio = datetime(2022, 12, 12).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "ciudad carmin"
        newo.save()

        newo = Orden()
        newo.client = "sabrina"
        newo.fecha = "2023-12-12"
        newo.fecha_envio = datetime(2023, 12, 12).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "ciudad azafran"
        newo.save()



        res = self.client.get("/?fecha_inicio=%s&fecha_fin=%s" % (
            '2023-11-01',
            '2023-12-25',
        ))

        ords = res.context["ordenes"]
        self.assertEqual(1, len(ords))
