from django.db import models
from enum import Enum
from django.contrib.auth.models import User


# Create your models here.
class CategoriaVuelo(Enum):
    NATIONAL_FLIGHT = 'National Flight'
    INTERNATIONAL_FLIGHT = 'International Flight'
    REGIONAL_FLIGHT = 'Regional Flight'


class Airline(models.Model):
    codigo_IATA_aerolinea = models.CharField(primary_key=True, unique=True, max_length=45)
    nombre_aerolinea = models.CharField(max_length=127, null=False)


class Country(models.Model):
    id_pais = models.CharField(primary_key=True, unique=True, max_length=45)
    nombre_pais = models.CharField(max_length=45, null=False)


class City(models.Model):
    id_ciudad = models.CharField(primary_key=True, unique=True, max_length=45)
    id_pais_ciudad = models.ForeignKey(Country, on_delete=models.CASCADE)
    nombre_ciudad = models.CharField(max_length=127, null=False)


class Airport(models.Model):
    codigo_IATA_aeropuerto = models.CharField(primary_key=True, unique=True, max_length=45)
    id_ciudad_aeropuerto = models.ForeignKey(City, on_delete=models.CASCADE)
    id_pais_aeropuerto = models.ForeignKey(Country, on_delete=models.CASCADE)
    nombre_aeropuerto = models.CharField(max_length=127, null=False)


class Flight(models.Model):
    id_vuelo = models.CharField(primary_key=True, unique=True, max_length=45)
    codigo_IATA_aerolinea_vuelo = models.ForeignKey(Airline, on_delete=models.CASCADE)
    codigo_IATA_aeropuerto_salida = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='codigo_IATA_aeropuerto_salida')
    id_ciudad_aeropuerto_salida = models.ForeignKey(City, on_delete=models.CASCADE, related_name='id_ciudad_aeropuerto_salida')
    id_pais_aeropuerto_salida = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='id_pais_aeropuerto_salida')
    codigo_IATA_aeropuerto_llegada = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='codigo_IATA_aeropuerto_llegada')
    id_ciudad_aeropuerto_llegada = models.ForeignKey(City, on_delete=models.CASCADE, related_name='id_ciudad_aeropuerto_llegada')
    id_pais_aeropuerto_llegada = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='id_pais_aeropuerto_llegada')
    fecha_salida = models.DateTimeField(null=False)
    fecha_llegada = models.DateTimeField(null=False)
    categoria_vuelo = models.CharField(max_length=45, choices=[(tag.name, tag.value) for tag in CategoriaVuelo], null=False)


class Ticket(models.Model):
    id_ticket = models.CharField(primary_key=True, unique=True, max_length=45)
    grupo = models.CharField(max_length=45, null=False)
    asiento = models.CharField(max_length=45, null=False)
    categoria_pasajero = models.CharField(max_length=45, null=False)
    equipaje_mano = models.FloatField(null=False)
    equipaje_bodega = models.FloatField(null=False)
