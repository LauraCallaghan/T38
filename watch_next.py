""" 
This reads a list of films with their descriptions from a text file, and allows the user to input a film description. 
It returns a suggestion of a film to watch next based on the similarity of the description the user entered to the 
descriptions in the text file.
"""

# Imports the spaCy package
import spacy

# Accesses the language model
nlp = spacy.load('en_core_web_md')

def find_similar(movie_desc):
    """ 
    Takes input of a film description, compares the input to descriptions in a dictionary, selects and returns the film with the best matching description
    Parameters: string input of a film's description
    Returns: Recommended film title
    """
    # Runs the input description through the language model
    movie_desc = nlp(movie_desc)

    # Creates an empty dictionary to store the similarity scores of each film
    sim_dict = {}

    # Iterates through the dictionary, checking comparing each description to the input description and adding each film title and similarity score to the sim_dict
    for k,v in moviedict.items():
        similarity = nlp(v).similarity(movie_desc)
        sim_dict[k] = similarity
        
    # Sets variable to use below in determining the film with the highest similarity score 
    max_sim = 0
    #  Variable to hold title of most similar film
    movie_rec = ""

    # Iterates through sim_dict, finding the item with the highest similarity score
    for k,v in sim_dict.items():
        if v > max_sim:
            max_sim = v
            movie_rec = k
    
    # Returns a message recommending the film with the highest similarity score
    return f"The film you should watch next is: {movie_rec}"

# Opens the movies file, reads contents into a variable, then closes file
f = open('movies.txt','r')
movies = f.readlines()
f.close()

# Creates a dictionary to hold the name and descriptions of the films
moviedict = {}

# Iterates through each item in the contents of the file, splitting it at the colon and populating the dictionary with the title as key and 
# description as value
for movie in movies:
    split_data = movie.split(" :")
    moviedict[split_data[0]] = split_data[1] 

# A variable to store the description of the film we want to compare with. Alternatively the full text could go straight into the find_similar function
# as a parameter, but this seems tidier to me.
movie_comp = """Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into 
space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."}
"""

# Calls the function, supplying the description in the form of a variable
print(find_similar(movie_comp))
