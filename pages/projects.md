---
title: Projets SIG
description: Portfolio de projets en géomatique, webmapping, analyse spatiale et développement SIG.
keywords:
  - Projets
  - SIG
  - Géomatique
  - Webmapping
  - Analyse spatiale
---

# Projets SIG

Sélection de projets réalisés dans le cadre de mon Master 2 Géomatique (G2M) à l'Université Paris 8 et de mon apprentissage au Port de Boulogne-sur-Mer—Calais.

---

## 🚢 Outil cartographique portuaire — Suivi des interventions sur le domaine portuaire

```{image} images/interventions.png
:alt: Outil cartographique portuaire
:width: 100%
```

**Contexte :** Projet développé dans le cadre de l'apprentissage au Service SIG (SSIG) du Port de Boulogne-sur-Mer—Calais, Région Hauts-de-France. Le domaine portuaire évolue en permanence (travaux, maintenances, modifications d'infrastructures) et les informations sur ces interventions provenaient de sources multiples sans centralisation, compliquant le suivi et la mise à jour des données SIG.

**Objectif :** Développer et déployer une application cartographique en ligne open source pour centraliser, géolocaliser et suivre l'ensemble des interventions réalisées sur le domaine portuaire.

**Fonctionnalités développées :**
- Carte interactive Leaflet avec affichage des interventions, symboles différenciés et fenêtres contextuelles
- Formulaires CRUD (création, édition, mise à jour, suppression) pour la saisie des interventions
- Recherche et filtrage multicritères (par date, zone, statut, service responsable)
- Tableau de bord de suivi avec graphiques et statistiques
- Authentification sécurisée et gestion des droits d'accès (consultation, édition, validation)
- Outils cartographiques d'analyse (mesures de distances, surfaces, zones tampons)

**Technologies :** Python, Django, PostgreSQL, PostGIS, Leaflet.js, HTML, CSS, JavaScript

**Durée :** 4 mois (février – mai 2026)

---

## 🐦 Portail Laridés — Suivi des colonies de mouettes et goélands

```{image} images/lariport.png
:alt: Portail Laridés
:width: 100%
```

**Contexte :** Projet développé au SSIG du Port de Boulogne-sur-Mer—Calais pour la cellule environnement, dans le cadre de la dérogation espèces protégées "Laridés". L'objectif était de créer un portail cartographique en ligne pour présenter et suivre les populations nicheuses de mouettes tridactyles et de goélands sur le domaine portuaire.

**Objectif :** Mettre à disposition des partenaires internes et externes (Ville de Boulogne, Communauté d'Agglomération, exploitant portuaire) un outil de visualisation des zones de compensation, de quiétude et de nidification, avec les données de suivi annuel (effectifs, nids occupés, reproductivité).

**Fonctionnalités développées :**
- Cartographie interactive des zones de nidification et de compensation sur le domaine portuaire
- Consultation d'informations par zone : effectifs, photos, recommandations
- Gestion des données : ajout, modification et suppression des observations de nids
- Légende dynamique et fenêtres contextuelles
- Accès partagé entre utilisateurs internes (cellule environnement) et partenaires externes

**Technologies :** ArcGIS Pro, ArcGIS Online, ArcGIS Experience Builder, HTML, CSS, JavaScript

**Durée :** Janvier – Juillet 2025, puis maintenance continue

---

## 🦟 Tiques et paysages français — Analyse multivariée des signalements de piqûres

```{image} images/tiques_paysages.jpg
:alt: Carte des typologies paysagères des signalements de tiques
:width: 100%
```

**Contexte :** Projet tutoré de Master 2 G2M (Université Paris 8), réalisé en collaboration avec le programme de recherche participative [CiTIQUE](https://www.citique.fr/) (INRAE). L'objectif était de qualifier les signalements de piqûres de tiques sur les animaux domestiques en France, en caractérisant les paysages dans lesquels ces piqûres surviennent.

**Problématique :** Dans quelle mesure les caractéristiques paysagères permettent-elles d'identifier des profils spatiaux distincts associés aux environnements des piqûres de tiques ?

**Données :**
- ~4 500 signalements géolocalisés de piqûres (chiens et chats), issus du programme CiTIQUE (2017–2020)
- Données d'occupation du sol CLC+ Backbone 2018 (résolution 10 m, Copernicus)

**Méthodologie :**
1. Calcul d'un rayon d'analyse paysagère de 1 300 m basé sur les distances de déplacement des chiens
2. Extraction des proportions de couverture du sol (11 classes) dans chaque zone tampon
3. Analyse en Composantes Principales (ACP) pour identifier les gradients paysagers structurants
4. Classification k-means pour établir une typologie en 5 profils paysagers

**Résultats clés :**
- Identification de 5 typologies paysagères distinctes : forêts dominantes, territoires agricoles, milieux mixtes semi-naturels, espaces urbains/périurbains, paysages prairiaux
- Les piqûres ne se concentrent pas dans un seul type de milieu : ~75 % se répartissent entre forêts, agriculture et prairies, et ~20 % concernent des espaces urbains
- Mise en évidence de deux gradients majeurs : naturalité forestière vs agriculture, et anthropisation vs milieux ouverts naturels

**Technologies :** Python (pandas, geopandas, scikit-learn), R (FactoMineR, factoextra), ArcGIS Experience Builder, QGIS, Jupyter Notebook

**Livrables :** [Site web du projet](https://hoperror.github.io/Tiques-et-paysage---Projet-tutor-G2M/) | [Dépôt GitHub](https://github.com/hoperror/Tiques-et-paysage---Projet-tutor-G2M)

---

## 📹 Vidéoprotection et délinquance de rue — Analyse SIG sur Grand Paris Seine Ouest

```{image} images/videoprotection_gpso.png
:alt: Carte bivariée vidéoprotection et délinquance GPSO
:width: 100%
```

**Contexte :** Projet réalisé dans le cadre du cours d'Analyse de données et SIG en Master 2 G2M (Université Paris 8). L'étude évalue l'impact de la vidéoprotection sur la délinquance de rue à l'échelle des 8 communes de l'EPT Grand Paris Seine Ouest (Hauts-de-Seine), en croisant des données ouvertes de localisation de caméras avec les statistiques nationales de la délinquance (SSMSI 2025).

**Problématique :** Quel est l'impact réel de la vidéoprotection sur la délinquance de rue à l'échelle d'un territoire intercommunal ?

**Chaîne de traitement :**
1. **Traitement de données massives (Python/Pandas)** : filtrage de la base nationale SSMSI (plusieurs millions de lignes) pour extraire les 8 communes de GPSO, isolation des infractions "sensibles espace public" (vols, dégradations, stupéfiants), calcul de moyennes lissées sur deux périodes (2016-2018 vs 2022-2025) pour neutraliser l'effet COVID
2. **Normalisation et export** : calcul de la densité de caméras pour 10 000 habitants, taux d'évolution de la délinquance, part des infractions sur la voie publique — export CSV structuré vers QGIS
3. **Analyse spatiale et cartographie (QGIS/PyQGIS)** : géocodage par code INSEE via script PyQGIS, extraction de centroïdes, production de 3 cartes thématiques dont une carte bivariée croisant densité de caméras et taux de délinquance

**Résultats clés :**
- Corrélation négative globale : plus la densité de caméras est élevée, plus le taux d'infractions de voie publique tend à être faible
- Identification de deux logiques territoriales distinctes : logique de volume (Boulogne-Billancourt, 160 caméras) vs logique de densité (Ville-d'Avray, 31,5 caméras/10k hab.)
- Mise en évidence d'une anomalie statistique (Marnes-la-Coquette) démontrant les limites du facteur vidéoprotection seul

**Technologies :** Python (Pandas, Jupyter Notebook), QGIS 3.34, PyQGIS, Open Data (SSMSI, GPSO, IGN ADMIN-EXPRESS)

[Dépôt GitHub](https://github.com/hoperror/analyse-videoprotection-GPSO)

---

## 🌍 Simulation "Out of Africa" — Modélisation multi-agents de la dispersion humaine

```{image} images/out_of_africa.gif
:alt: Simulation Out of Africa
:width: 100%
```

**Contexte :** Projet réalisé dans le cadre du cours Agents et SIG en Master 2 G2M (Université Paris 8), en binôme. Basé sur les travaux fondateurs de Young & Bettinger (1995), l'objectif était de simuler la dispersion des humains modernes (*Homo sapiens*) depuis l'Afrique vers le reste du Vieux Monde à la fin du Pléistocène.

**Approche :** Modèle basé sur agents (ABM) développé en Julia, où chaque agent représente un groupe humain se déplaçant sur une grille contrainte par la géographie réelle. Le modèle intègre des règles de mortalité, de reproduction, de compétition pour les ressources et un gradient climatique nord-sud influençant la fertilité.

**Fonctionnalités du modèle :**
- Environnement géographique réel : conversion d'une carte du Vieux Monde en masque binaire (terre/océan) sur une grille 100×100
- Mortalité régulée par la densité locale (capacité de charge K et conflits pour les ressources)
- Gradient climatique : fertilité maximale à l'équateur, décroissante vers le nord
- Simulation sur 1 000 itérations avec génération de visualisations animées (GIF/vidéo)

**Résultats :**
- Reproduction du front de colonisation ("Wave of Advance") cohérent avec la théorie Out of Africa
- Mise en évidence de l'effet goulot d'étranglement au passage vers l'Eurasie (péninsule du Sinaï)
- Équilibre dynamique de la population grâce à l'autorégulation (densités plus fortes au sud qu'au nord)

**Technologies :** Julia, Agents.jl, CairoMakie, Images.jl/FileIO

[Dépôt GitHub](https://github.com/hoperror/simulation-out-of-africa)

---

## 🦟 Dengue à Girardot (Colombie) — Analyse spatio-temporelle des clusters épidémiques

<!-- ```{image} images/dengue_girardot.png
:alt: Clusters épidémiques de dengue à Girardot
:width: 100%
``` -->

**Contexte :** Projet réalisé dans le cadre du cours d'Analyse spatiale en Master 2 G2M (Université Paris 8), en binôme. L'étude porte sur la transmission de la dengue à Girardot (Colombie), ville de 150 000 habitants en climat tropical, à partir de 2 730 cas géocodés issus du système national de surveillance SIVIGILA (2010-2017).

**Problématique :** Où se concentrent les clusters épidémiques de dengue, sont-ils persistants dans le temps, et quelles implications pour les stratégies de prévention ?

**Méthodologie (double approche) :**
1. **Analyse par Getis-Ord Gi*** : identification des hotspots locaux avec deux modèles (Fixed Distance Band et Zone of Indifference), puis validation croisée par intersection pour ne retenir que les clusters robustes
2. **Scan statistique spatio-temporel (SaTScan)** : modèle de Poisson rétrospectif avec affinage progressif des paramètres (rayon ≤ 250 m calé sur la dispersion des Aedes aegypti, fenêtre temporelle 20 jours–6 mois, agrégation à 25 jours basée sur le cycle viral)

**Résultats clés :**
- Identification de clusters persistants sur 2013 et 2015 : secteur sud-ouest (stade + université) et rives du Rio Bogotá
- En 2013 : 6 clusters significatifs (p < 0.05), actifs de janvier à avril, avec des risques relatifs jusqu'à 28× la moyenne
- Apparition de nouveaux clusters au nord-est en 2015, révélant une évolution des dynamiques de transmission
- Validation croisée : les résultats SaTScan corroborent les hotspots identifiés par Getis-Ord Gi*

**Technologies :** SaTScan 10.1, ArcGIS Pro (Getis-Ord Gi*, Intersect), données SIVIGILA

---

## ✈️ Application métier ATE — Outil de checking des vols

```{image} images/ate_check.png
:alt: Application de checking des vols ATE
:width: 100%
```

**Contexte :** Projet réalisé dans le cadre d'un examen de PHP en Master 2 G2M (Université Paris 8). À partir d'une base de données existante d'une compagnie aérienne (avions, vols, pilotes, techniciens, essais techniques, aéroports géolocalisés), l'objectif était de concevoir une application web cartographique répondant à une problématique métier.

**Problématique :** Quels sont les vols prêts au départ, ceux en attente ou en anomalie, et où se situent-ils spatialement au moment du contrôle ?

**Fonctionnalités développées :**
- Modélisation et création de tables complémentaires (agents de trafic, checks de vols) avec contraintes d'intégrité
- Formulaire de saisie des contrôles d'avant-vol (statut OK / KO / EN_ATTENTE) avec requêtes PDO sécurisées
- Carte interactive Leaflet affichant les vols géolocalisés à l'aéroport de départ, avec code couleur par statut (vert, orange, rouge)
- Vue tabulaire complémentaire avec jointures complexes (vols, pilotes, avions, modèles, essais, techniciens)

**Technologies :** PHP, PostgreSQL, Leaflet.js, HTML, CSS, JavaScript, PDO

[Dépôt GitHub](https://github.com/hoperror/application-metier-ATE)

---

## 🪵 Blog cartographique Sticknation — Plateforme d'inventaire communautaire

<!-- ```{image} images/sticknation.png
:alt: Blog cartographique Sticknation
:width: 100%
``` -->

**Contexte :** Projet réalisé dans le cadre du cours ADYC en Master 2 G2M (Université Paris 8). L'objectif était de transformer un blog classique en une application cartographique interactive, en s'inspirant du phénomène viral "Official Stick Reviews" — un inventaire humoristique et géolocalisé de bâtons trouvés dans la nature.

**Fonctionnalités développées :**
- Dashboard cartographique immersif avec Leaflet (multi-fonds de carte : plan, satellite, mode sombre)
- Slider temporel dynamique pour filtrer les publications par année via une API JSON interne (AJAX)
- Chargement dynamique de fichiers GeoJSON pour l'exploration par zones géographiques
- Système de likes asynchrone et commentaires hybrides (utilisateurs connectés et invités)
- Gestion des profils utilisateurs et interface d'administration

**Technologies :** Python, Django, SQLite, Leaflet.js, AJAX, GeoJSON, HTML, CSS, JavaScript

[Dépôt GitHub](https://github.com/hoperror/webmap_sticknation)
