import numpy as np
from matplotlib import pyplot as plt
from CoolProp.CoolProp import PropsSI

# Fluide de travail
fluid = "R404a"

# Caractéristiques critiques et limites
p_crit = PropsSI("Pcrit", fluid) # Conversion en bar effectuée plus bas dans le tracé
T_crit = PropsSI("Tcrit", fluid)
h_crit = PropsSI("H", "P", p_crit, "T", T_crit, fluid)

p_min = 1.0e5 # de pression en bar
pressures = np.linspace(p_min, p_crit, 100)
In_pressures = np.log(pressures)

# Courbes de saturation
enthalpie_liquide = PropsSI("H", "P", pressures, "Q", 0, fluid)
enthalpie_vapeur = PropsSI("H", "P", pressures, "Q", 1, fluid)

# État initial 1 : Vapeur saturée à -20°C
T1 = -20 + 273.15
p1 = PropsSI("P", "T", T1, "Q", 1, fluid)
h1 = PropsSI("H", "T", T1, "Q", 1, fluid)
s1 = PropsSI("S", "T", T1, "Q", 1, fluid)

# État 2s et 2 : Compression avec rendement isentropique de 0.75
# L'état 2 est à la pression de saturation correspondant à 30°C
T2_sat = 30 + 273.15
p2 = PropsSI("P", "T", T2_sat, "Q", 1, fluid)
p2s = p2

h2s = PropsSI("H", "P", p2s, "S", s1, fluid)
h2 = h1 + (h2s - h1) / 0.75
T2 = PropsSI("T", "P", p2, "H", h2, fluid)

# État 3 : Refroidissement isobare jusqu'en liquide saturé (x=0)
p3 = p2
h3 = PropsSI("H", "P", p3, "Q", 0, fluid)
T3 = PropsSI("T", "P", p3, "H", h3, fluid)

# État 4 : Détente isenthalpique jusqu'à -20°C
p4 = p1
h4 = h3
T4 = T1

# Stockage des états pour le cycle fermé
h_states = [h1, h2, h3, h4, h1]
In_p_states = [np.log(p1), np.log(p2), np.log(p3), np.log(p4), np.log(p1)]

# Calcul des volumes spécifiques et autres propriétés pour affichage
v1 = 1 / PropsSI("D", "P", p1, "Q", 1, fluid)
T2s = PropsSI("T", "P", p2s, "S", s1, fluid)
v2s = 1 / PropsSI("D", "P", p2s, "T", T2s, fluid)
s2s = s1
v2 = 1 / PropsSI("D", "P", p2, "H", h2, fluid)
s2 = PropsSI("S", "P", p2, "H", h2, fluid)
v3 = 1 / PropsSI("D", "P", p3, "Q", 0, fluid)
s3 = PropsSI("S", "P", p3, "Q", 0, fluid)
v4 = 1 / PropsSI("D", "P", p4, "H", h4, fluid)
s4 = PropsSI("S", "P", p4, "H", h4, fluid)
x4 = PropsSI("Q", "P", p4, "H", h4, fluid)

# Débit massique et calculs énergétiques
m_dot = 3.5 / 1000 # 3.5 g/s en kg/s
P_evap = m_dot * (h1 - h4)
P_cond = m_dot * (h2 - h3)
P_comp = m_dot * (h2 - h1)

COP_fr = (h1 - h4) / (h2 - h1)
COP_pac = COP_fr + 1
COP_carnot = T1 / (T2_sat - T1)

# Affichage des résultats dans la console
print("Point, p (bar), T (°C), v (dm3/kg), h (kJ/kg), s (kJ/kg/K), x (-)")
print(f"1, {round(p1/1e5,1)}, {round(T1-273.15,1)}, {round(v1*1000,1)}, {round(h1/1000,1)}, {round(s1/1000,2)}, 1")
print(f"2s, {round(p2s/1e5,1)}, {round(T2s-273.15,1)}, {round(v2s*1000,1)}, {round(h2s/1000,1)}, {round(s2s/1000,2)}, -")
print(f"2, {round(p2/1e5,1)}, {round(T2-273.15,1)}, {round(v2*1000,1)}, {round(h2/1000,1)}, {round(s2/1000,2)}, -")
print(f"3, {round(p3/1e5,1)}, {round(T3-273.15,1)}, {round(v3*1000,1)}, {round(h3/1000,1)}, {round(s3/1000,2)}, 0")
print(f"4, {round(p4/1e5,1)}, {round(T4-273.15,1)}, {round(v4*1000,1)}, {round(h4/1000,1)}, {round(s4/1000,2)}, {round(x4,3)}")
print()
print(f"Puissance frigorifique (kW) : {round(P_evap/1000,2)}")
print(f"Puissance calorifique (kW) : {round(P_cond/1000,2)}")
print(f"Puissance de compression (kW) : {round(P_comp/1000,2)}")
print(f"COP frigo (-) : {round(COP_fr,1)}")
print(f"COP PAC (-) : {round(COP_pac,1)}")
print(f"COP Carnot (-) : {round(COP_carnot,1)}")

# Tracé du diagramme ln(p)-h
plt.figure(figsize=(8, 6))
plt.plot(enthalpie_liquide / 1000, In_pressures - np.log(1e5), label="Saturation (liquide)", color="#89CFF8")
plt.plot(enthalpie_vapeur / 1000, In_pressures - np.log(1e5), label="Saturation (vapeur)", color="#b9f0ca")
plt.plot(np.array(h_states) / 1000, np.array(In_p_states) - np.log(1e5), 'o-', label="Cycle frigorifique", color="#f7921e")
plt.plot(h_crit / 1000, np.log(p_crit) - np.log(1e5), marker="x", markersize=10, markeredgecolor="black", label="Point critique")

plt.xlabel("Enthalpie (kJ/kg)")
plt.ylabel("ln(P) [ln(bar)]")
plt.title("Prépa diagramme ln(p)-h pour le fluide frigorigène R404a")
plt.legend()
plt.grid()
plt.show()