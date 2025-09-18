import spacy

def perform_ner(text):
    
    nlp = spacy.load("en_core_web_sm")
    
    doc = nlp(text)
    
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

def print_entities(entities):

    if not entities:
        print("No named entities found.")
    else:
        print("Named Entities:")
        for entity, label in entities:
            print(f"  - {entity} ({label})")

if __name__ == "__main__":
    text = "My name is Aman, and I am a Machine Learning Trainer at Google in New York."
    
    entities = perform_ner(text)
    
    print(f"Input Text: {text}")
    print_entities(entities)
    text2 = "Elon Musk founded Tesla and SpaceX in California."
    entities2 = perform_ner(text2)
    print(f"\nInput Text: {text2}")
    print_entities(entities2)