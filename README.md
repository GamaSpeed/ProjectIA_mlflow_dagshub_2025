# 1. Construire le modèle de machine Learning
- Le code pour construire, entraîner et sauvegarder le modèle se trouve dans le fichier `projet.ipynb`.

# 2. Créer une API pour le modèle (Fast API)

- Implémenter l'application dans `app.py`
- Utiliser test/test_request.py pour tester l'appel à l'API en local

# 3. Configurer Google Cloud 
- Créer un nouveau projet
- Activer l'API Cloud Run et l'API Cloud Build

## Installer et initialiser Google Cloud SDK
- [Installer Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Initialiser avec gcloud init

# 4 Créer le fichier requirements.txt
requirements.txt

# 5. Conteneurisation:  Dockerfile, requirements.txt, .dockerignore
Créer les fichier Dockerfile, et .dockerignore

# 6. Construction et déploiement dans le Cloud

### Soumettre le build de l'image Docker à Google Container Registry
gcloud builds submit --tag gcr.io/russian-housing-price/deployment

### Déployer l'image sur Google Cloud Run
gcloud run deploy --image gcr.io/russian-housing-price/deployment --platform managed

# 7 Test
- Tester le code avec `app.py` en utilisant le lien disponible après le déploiement
