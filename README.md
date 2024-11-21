# **Thermal Project**

Ce projet modélise un cycle Rankine organique (ORC) avec des fichiers Python pour définir les états, exécuter le programme, et des outils pour la simulation.

## **Structure du Projet**

### **1. Fichiers principaux**
- **`ORC_group_21.py`** : Définit les états du cycle ORC (pression, température, etc.).
- **`ORC_test.py`** : Permet de lancer le programme et d’évaluer les performances.

### **2. Folder `Tools`**
- Contient les fichiers liés aux outils nécessaires au projet :
  - **`heat_exchanger.py`** : Définit les calculs et modèles liés aux échangeurs de chaleur.
  - **`pump.py`** : Définit les calculs et paramètres liés aux pompes.

### **3. Folder `Param`**
- Contient le fichier **Excel** avec tous les paramètres d'entrée nécessaires au modèle :
  - **`Projet_contraintes.xlsx`** : Fournit les contraintes et valeurs initiales.

## **Comment utiliser le projet**
1. **Configurer les paramètres** :
   - Modifie les valeurs dans le fichier Excel `Projet_contraintes.xlsx` selon les besoins du modèle.
2. **Exécuter le programme** :
   - Lance le fichier `ORC_test.py` pour simuler le cycle et obtenir les résultats.

