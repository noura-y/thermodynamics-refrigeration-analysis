# Thermodynamics Refrigeration Analysis

Modélisation et traçage des propriétés thermodynamiques d'un cycle fermé de réfrigération.

## Présentation du projet
Ce script Python a été développé pour analyser les transformations subies par le fluide frigorigène R404a. Le programme permet de calculer et d'afficher les coefficients de performance (COP) ainsi que les puissances associées aux quatre composants principaux du système :
* Évaporateur (Vaporisation isobare)
* Compresseur (Compression adiabatique non-isentropique)
* Condenseur (Refroidissement isobare)
* Détendeur (Détente isenthalpique)

## Technologies
* Python 3
* CoolProp (Accès aux tables thermodynamiques)
* NumPy (Gestion des tableaux de données)
* Matplotlib (Génération du diagramme quantitatif ln(p)-h)

## Propriétés calculées
Le programme génère le résumé des propriétés thermodynamiques aux points clés du cycle :
* Pressions absolues (bar) et températures (°C)
* Volumes spécifiques (dm3/kg)
* Enthalpies (kJ/kg) et entropies (kJ/kg/K)
* Titre de qualité de la vapeur (x)
* Puissances frigorifique, calorifique et de compression (kW)
* COP Frigo, PAC et Carnot
