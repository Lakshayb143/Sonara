import spacy

# Loading spacy model.
processor_lang = spacy.load("en_core_web_sm")


# Simple command processing
def process_command(command):
    doc = processor_lang(command)
    
    if "time" in command:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    return "Sorry, Please try again"
