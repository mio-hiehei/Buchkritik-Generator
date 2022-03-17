import random
import names


def get_book_critique(book_title_list,
                      adjective_list,
                      objekt_list,
                      verb_list,
                      was_list,
                      wessen_list,
                      wowann_list):

    global possessiv
    book_title = random.sample(book_title_list, k=1)[0]

    adjective = random.sample(adjective_list, k=1)[0]

    objekt = random.sample(objekt_list, k=1)

    verb = random.sample(verb_list, k=1)

    was = random.sample(was_list, k=1)[0]

    wessen = random.sample(wessen_list, k=1)[0]

    wowann = random.sample(wowann_list, k=1)[0]

    gender_author = random.choice(["female", "male"])
    name = names.get_full_name(gender=gender_author)

    if objekt[0][1] == "f" and gender_author == "female":
        possessiv = "ihrer"
    elif objekt[0][1] == "m" and gender_author == "female":
        possessiv = "ihrem"
    elif objekt[0][1] == "f" and gender_author == "male":
        possessiv = "seiner"
    elif objekt[0][1] == "m" and gender_author == "female":
        possessiv = "seinem"


    sentence = f"In {possessiv} {adjective} {objekt[0][0]} {verb[0][0]} {name} {verb[0][1]} {was} {wessen} {wowann}."


    critique_content = {
        "book_title": book_title,
        "name": name,
        "sentence": sentence
    }


    return critique_content