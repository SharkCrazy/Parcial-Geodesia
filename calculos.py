# calculos.py
import math
import scipy.integrate as integrate
from parametros import a, b, e2, e22, e
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

# calculos.py
import math
from parametros import a, e2

def sexagesimal_a_decimal(grados, minutos, segundos):
    return grados + (minutos / 60.0) + (segundos / 3600.0)

# calculos.py
import math
from parametros import a, e2

def sexagesimal_a_decimal(grados, minutos, segundos):
    return grados + (minutos / 60.0) + (segundos / 3600.0)

def calcular_area_cuadrilátero(lat1, lon1, lat2, lon2):
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lon_rad = math.radians(lon2 - lon1)
    
    area = abs(a**2 * (1 - e2) * delta_lon_rad * 
               (math.sin(lat2_rad) - math.sin(lat1_rad) + 
                (2/3) * e2 * (math.sin(lat2_rad)**3 - math.sin(lat1_rad)**3) + 
                (3/5) * (e2**2) * (math.sin(lat2_rad)**5 - math.sin(lat1_rad)**5) + 
                (4/7) * (e2**3) * (math.sin(lat2_rad)**7 - math.sin(lat1_rad)**7) + 
                (5/9) * (e2**4) * (math.sin(lat2_rad)**9 - math.sin(lat1_rad)**9) +
                (6/11) * (e2**5) * (math.sin(lat2_rad)**11 - math.sin(lat1_rad)**11) +
                (7/13) * (e2**6) * (math.sin(lat2_rad)**13 - math.sin(lat1_rad)**13) +
                (8/15) * (e2**7) * (math.sin(lat2_rad)**15 - math.sin(lat1_rad)**15)))

    return area

