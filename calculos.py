# calculos.py
import math
import scipy.integrate as integrate
from parametros import a, b, e2, e22
from scipy.integrate import quad

def sexagesimal_a_decimal(grados, minutos, segundos):
    return grados + (minutos / 60.0) + (segundos / 3600.0)

def primera_vertical(latitud_rad):
    return a / math.sqrt(1 - e2 * math.sin(latitud_rad)**2)

def M(phi_rad):
    seno = math.sin(phi_rad)
    seno2 = seno ** 2
    cosn = math.cos(phi_rad)
    cosn2 = cosn ** 2
    V = math.sqrt(1 + e22 * cosn2)
    W = (b / a) * V
    W3 = W ** 3
    return (a * (1 - e2)) / W3

def longitud_arco_meridiano(lat1_deg, lat2_deg):
    lat1_rad = math.radians(lat1_deg)
    lat2_rad = math.radians(lat2_deg)
    longitud_arco, _ = integrate.quad(M, lat1_rad, lat2_rad)
    return longitud_arco

def longitud_arco_paralelo(latitud_deg, delta_longitud_deg):
    latitud_rad = math.radians(latitud_deg)
    delta_longitud_rad = math.radians(delta_longitud_deg)
    N_phi = primera_vertical(latitud_rad)
    longitud_arco = N_phi * math.cos(latitud_rad) * delta_longitud_rad
    return longitud_arco

def longitud_arco_paralelo_con_longitudes(latitud_deg, longitud1_deg, longitud2_deg):
    latitud_rad = math.radians(latitud_deg)
    longitud1_rad = math.radians(longitud1_deg)
    longitud2_rad = math.radians(longitud2_deg)
    delta_longitud_rad = abs(longitud1_rad - longitud2_rad)
    N_phi = primera_vertical(latitud_rad)
    longitud_arco = N_phi * math.cos(latitud_rad) * delta_longitud_rad
    return longitud_arco

def integrand(phi):
    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)
    return cos_phi / ((1 - e2 * sin_phi**2)**2)

def calcular_area_cuadrilátero(lat1, lon1, lat2, lon2):
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_lambda = math.radians(lon2 - lon1)
    
    integral, _ = quad(integrand, phi1, phi2)
    
    # Calcular el área del cuadrilátero
    area = b**2 * delta_lambda * integral
      
    return area
