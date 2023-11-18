import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_md")


def similarity_score(description1, description2):
    # Process the text using SpaCy
    doc1 = nlp(description1)
    doc2 = nlp(description2)

    # Calculate the similarity between the two processed texts
    return doc1.similarity(doc2)


def find_next_movie(description, movies_file):
    # Initialize variables to track the most similar movie and i similarity score
    most_similar_movie = None
    max_similarity = -1  # Initialize with a low value

    # Open the movies file and read descriptions
    with open(movies_file, 'r') as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                title, movie_description = parts[0], parts[1]

                # Calculate similarity between the given description and the movie description
                similarity = similarity_score(description, movie_description)

                # Update most similar movie if the current movie has higher similarity
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_movie = title

    return most_similar_movie


# Example usage
description_to_match = "Will he save their world or destroy it? When the Hulk becomes too dangerous for Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

movies_file_path = "movies.txt"
most_similar_movie = find_next_movie(description_to_match, movies_file_path)

if most_similar_movie:
    print(f"You should watch: {most_similar_movie}")
else:
    print("No similar movie found.")
