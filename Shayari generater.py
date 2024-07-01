import random

# Dictionary storing templates categorized by type
shayari_templates = {
    'sad': [
        "Aansu {verb} hai {pronoun} ke {noun1} hum, Sab kehte hai kaisi lag gayi hai yeh {noun2} tumhe.",
        "Har kisi ko {adjective} {noun1} nahi milta, Kisi ko {noun2} toh kisi ko {noun3} nahi milta."
    ],
    'romantic': [
        "Tumhe dekhta hu toh lagta hai, Har {noun1} mein bas tumhara hi {verb} kiya.",
        "Tere bina zindagi mein koi {noun1} nahi, Tere bina raaton ko {noun2} bhi nahi."
    ],
    'motivational': [
        "Mehnat se jo milta hai, uski {noun1} alag hoti hai, Kaamyaabi ka {noun2} bhi kuch {adjective} hota hai.",
        "Haar na maano, {noun1} mil hi jayegi, Koshish karte raho, {noun2} zarur aayegi."
    ]
}

# Words to fill in the templates
words = {
    'verb': ['bahate', 'rote', 'dekhta', 'sochta'],
    'pronoun': ['sab', 'sabke', 'tumhare', 'mere'],
    'noun1': ['gham', 'pyaar', 'zindagi', 'khushi', 'raaste'],
    'noun2': ['aadat', 'raahat', 'neend', 'mohabbat'],
    'noun3': ['aasmaan', 'zameen', 'sapne', 'jazbaat'],
    'adjective': ['mukammal', 'rangin', 'khushnuma', 'sundar']
}


# Function to fill a template with random words
def fill_template(template):
    filled_shayari = template
    for key, word_list in words.items():
        filled_shayari = filled_shayari.replace(f'{{{key}}}', random.choice(word_list))
    return filled_shayari


# Function to return a random shayari from the chosen category
def get_random_shayari(category):
    if category in shayari_templates:
        template = random.choice(shayari_templates[category])
        return fill_template(template)
    else:
        return "Category not found. Please choose a valid category."


# Main program
if __name__ == "__main__":
    print("Welcome to Hinglish Shayari Generator!")
    print("Available categories: sad, romantic, motivational")

    category = input("Enter the category of shayari you want: ").strip().lower()

    shayari = get_random_shayari(category)
    print("\nHere is a {} shayari for you:\n".format(category))
    print(shayari)
