# Thermodynamics Refrigeration Analysis

Modélisation et traçage des propriétés thermodynamiques d'un cycle fermé de réfrigération.

## Présentation du projet
[cite_start]Ce script Python a été développé pour analyser les transformations subies par le fluide frigorigène R404a[cite: 27]. [cite_start]Le programme permet de calculer et d'afficher les coefficients de performance (COP) ainsi que les puissances associées aux quatre composants principaux du système[cite: 40, 114, 128]:
* [cite_start]Évaporateur (Vaporisation isobare) [cite: 45, 81]
* [cite_start]Compresseur (Compression adiabatique non-isentropique) [cite: 41, 76]
* [cite_start]Condenseur (Refroidissement isobare) [cite: 42, 79]
* [cite_start]Détendeur (Détente isenthalpique) [cite: 44, 80]

## Technologies
* Python 3
* [cite_start]CoolProp (Accès aux tables thermodynamiques) [cite: 113, 811]
* [cite_start]NumPy (Gestion des tableaux de données) [cite: 442]
* [cite_start]Matplotlib (Génération du diagramme quantitatif ln(p)-h) [cite: 82, 443]

## Propriétés calculées
[cite_start]Le programme génère le résumé des propriétés thermodynamiques aux points clés du cycle[cite: 85]:
* [cite_start]Pressions absolues (bar) et températures (°C) [cite: 83]
* [cite_start]Volumes spécifiques (dm3/kg) [cite: 83]
* [cite_start]Enthalpies (kJ/kg) et entropies (kJ/kg/K) [cite: 83]
* [cite_start]Titre de qualité de la vapeur (x) [cite: 83]
* [cite_start]Puissances frigorifique, calorifique et de compression (kW) [cite: 131]
* [cite_start]COP Frigo, PAC et Carnot [cite: 117, 119, 125]
