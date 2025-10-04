import json
import os

# === 1. Charger la liste des films ===
def load_movie_list(filepath):
    """Charge le fichier JSON contenant la liste complète des films."""
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# === 2. Filtrer uniquement les films britanniques ===
def classify(movies):
    """Retourne uniquement les films dont l'origine est 'British'."""
    british_movies = []
    for movie in movies:
        origin = movie.get("Origin", {})
        ethnicity = origin.get("Ethnicity", "")
        if ethnicity.lower() == "british":
            british_movies.append(movie)
    return british_movies


# === 3. Sauvegarder le résultat dans un nouveau fichier JSON ===
def save_movie_list(movies, output_path):
    """Sauvegarde les films filtrés dans un nouveau fichier JSON."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # crée le dossier 'output' s'il n'existe pas
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=4, ensure_ascii=False)
    print(f"{len(movies)} films britanniques ont été sauvegardés dans {output_path}")


# === 4. Fonction principale ===
def main():
    input_path = "input/wiki_movie_plots.json"
    output_path = "output/movie_plots.json"

    # Étape 1 : Charger le fichier d'entrée
    movies = load_movie_list(input_path)

    # Étape 2 : Filtrer les films britanniques
    british_movies = classify(movies)

    # Étape 3 : Sauvegarder le résultat
    save_movie_list(british_movies, output_path)


if __name__ == "__main__":
    main()
