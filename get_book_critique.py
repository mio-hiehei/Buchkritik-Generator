

def get_book_critique:

    sentence = f"In {possessiv} {adjective} {objekt[0]} {verb[0]} {name} {verb[1]} {was} {wessen} {wowann} {verb[2]}."


    critique_content = {
        "book_title": book_title,
        "name": name,
        "sentence": sentence
    }


    return critique_content