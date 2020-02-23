"""Detects unsafe features in the file."""
from google.cloud import vision
import io
import json

def detect_safe_search(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    '''Json Start'''
    adult = getRank(likelihood_name[safe.adult])
    medical = getRank(likelihood_name[safe.medical])
    spoofed = getRank(likelihood_name[safe.spoof])
    violence = getRank(likelihood_name[safe.violence])
    racy = getRank(likelihood_name[safe.racy])
    jsonObject = {
        "adult": adult,
        "medical": medical,
        "spoofed": spoofed,
        "violence": violence,
        "racy": racy
    }
    jsonString = json.dumps(jsonObject, indent=4)
    '''Json End'''

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return jsonString


def getRank(likelihood):
    if "UNKNOWN" == likelihood:
        return 0
    elif "VERY_UNLIKELY" == likelihood:
        return 1
    elif "UNLIKELY" == likelihood:
        return 2
    elif "POSSIBLE" == likelihood:
        return 3
    elif "LIKELY" == likelihood:
        return 4
    else:
        return 5