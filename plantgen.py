import random
import math


def get_random(seed, label, index: int = 0):
    rng = random.Random(seed + hash(label))
    if index > 0:
        return math.floor(rng.random() * index)
    return rng.random()


def genus_name(seed, plant_type):
    genus_types = {"Tree": "Arbor", "Shrub": "Fruticos", "Grass": "Gramin", "Frond": "Frond", "Vine": "Vitin", "Succulent": "Crass", "Fungoid": "Fung", "Floater": "Natan", "Flower": "Flor"}

    genus_endings = ["us", "a", "um", "is", "ex", "es", "ix", "ia", "ea", "eus", "ias"]
    return genus_types[plant_type] + genus_endings[get_random(seed, "genus_end", len(genus_endings))]


def pick_type(seed):
    possible_types = ["Tree", "Shrub", "Grass", "Frond", "Vine", "Succulent", "Fungoid", "Floater", "Flower"]
    return possible_types[get_random(seed, "plant_type", len(possible_types))]


def assign_climate(seed):
    possible_climates = ["Tropical", "Dry", "Cold", "Hot", "Dark", "Wet", "Mountainous"]
    return possible_climates[get_random(seed, "climate", len(possible_climates))]


def pick_color(seed, color_type):
    plant_colors = [
        "olive green",
        "mossy green",
        "fern-green",
        "sage green",
        "pine-green",
        "deep green",
        "pale green",
        "yellow-green",
        "blue-green",

        "brownish-green",
        "reddish-brown",
        "dark brown",
        "light brown",
        "golden-brown",

        "burgundy",
        "deep red",
        "wine-red",

        "plum-purple",
        "dark purple",
        "pale magenta",

        "pale yellow",
        "golden-yellow",
        "straw-colored",
        "muted yellow",

        "blue-green",
        "teal",
        "blue-gray",
        "muted blue",

        "cream-colored",
        "off-white",
        "ivory-white",
        "beige",
        "gray",
        "bright white",
    ]

    return plant_colors[math.floor(get_random(seed, color_type, len(plant_colors)))]


def species_name(seed, plant_traits):
    named_traits = ["preferred_climate"]
    trait_dictionary = {
        ### CLIMATES
        "Tropical": "tropic",
        "Dry": "adsicc",
        "Cold": "frigid",
        "Hot": "fervid",
        "Dark": "obscur",
        "Wet": "aquilent",
        "Mountainous": "montan"
    }

    selected_trait = named_traits[math.floor(get_random(seed, "species_trait", len(named_traits)))]

    selected_base = trait_dictionary[plant_traits[selected_trait]]

    species_endings = ["alia", "ius", "us", "anus", "a", "ensis", "imus", "issimus", "ia", "ium", "ada", "um", "ensus", "ae", "iae", "iferum", "ifus", "idae", "ida", "alis", "alus", "is"]
    selected_ending = species_endings[math.floor(get_random(seed, "species_ending", len(species_endings)))]
    return selected_base + selected_ending


def decide_fruit(seed, plant_type):
    fruitful_plants = ["Tree", "Shrub", "Vine"]
    if plant_type in fruitful_plants:
        if get_random(seed, "fruit", 6) < 1:
            return "edible"
        elif get_random(seed, "fruit", 6) < 2:
            return "poisonous"
    return "none"


def generate_plant():
    seed = random.randint(10000, 99999)

    new_plant = {
        "size_mult": "",
        "color_palette": "",
        "stem_color_pos": "",
        "leaf_color_pos": "",
        "fruit_color_pos": "",
        "plant_type": "",
        "genus_name": "",
        "species_name": "",
        "human_edible_bool": "",
        "poison_touch": "",
        "thorny_bool": "",
        "preferred_climate": "",
        "fruit_type": "",
        "other_material": "",
    }

    new_plant["size_mult"] = round(get_random(seed, "size_mult", 0) * 2, 2)
    new_plant["plant_type"] = pick_type(seed)
    new_plant["genus_name"] = genus_name(seed, new_plant["plant_type"])
    new_plant["preferred_climate"] = assign_climate(seed)
    new_plant["species_name"] = species_name(seed, new_plant)

    new_plant["stem_color_pos"] = pick_color(seed, "stem_color")
    leafy_plants = ["Tree", "Shrub", "Vine", "Frond", "Flower"]
    new_plant["leaf_color_pos"] = pick_color(seed, "leaf_color") if new_plant["plant_type"] in leafy_plants else "None"
    new_plant["fruit_color_pos"] = pick_color(seed, "fruit_color")

    new_plant["fruit_type"] = decide_fruit(seed, new_plant["plant_type"])

    colors_sentence = f"It has a {new_plant['stem_color_pos']} stem and {new_plant['leaf_color_pos']} leaves" if new_plant["leaf_color_pos"] != "None" else f"The whole plant is {new_plant['stem_color_pos']}"
    fruit_sentence = f"It also has {new_plant['fruit_type']}, {new_plant['fruit_color_pos']} fruits growing off of it." if new_plant["fruit_type"] != "none" else ""
    print(f"""
    Plant Name: {new_plant["genus_name"]} {new_plant["species_name"]}
    Plant Type: {new_plant["plant_type"]}
    Species Size: {new_plant["size_mult"]}x
    Description: {new_plant["genus_name"]} {new_plant["species_name"]} is a {new_plant["plant_type"].lower()}-like plant that is primarily found in {new_plant["preferred_climate"].lower()} climates. {colors_sentence}. {fruit_sentence}
    """)


generate_plant()
