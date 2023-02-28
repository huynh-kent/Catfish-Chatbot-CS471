import random
import json
import difflib

# open corpus json
CORPUS = {}
CORPUS_RESPONSES = []
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())
    CORPUS_RESPONSES = [response.lower() for response in CORPUS.keys()]


def process_message(user, sent_input):
    best_match = difflib.get_close_matches(sent_input, CORPUS_RESPONSES, n=1, cutoff=0.5) # change cutoff, higher more precise, lower more lenient
    if best_match:
        best_match_string = str(best_match).strip("[]'")
    #    print(best_match_string)
    #    print(CORPUS[best_match_string][user.ai.mood])
        response = random.choice(CORPUS[best_match_string][user.ai.mood])
    else:
        response = random.choice(CORPUS['default']['response'])

    """
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input][user.ai.mood])
    else:
        response = random.choice(CORPUS['default']['response'])
    """

    return (user, response)


