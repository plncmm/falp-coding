## Installation

1. Create a virtual python environment and install the requirements from `requirements.txt`
2. Place the models trained for entity detection in the root of the repository.
3. Launch the annotation server with the command `<location of virtual environment binaries>/python app.py`

## Usage

This web service exposes endpoints to lookup different entities and exposes them in `/<entity name>`. In order to annotate, a POST request must be sent to the respective endpoint with a JSON object containing the `text` property.

The service will respond with a JSON object containing the annotations with the following properties:

* `entities`: List of annotated entities, where each annotation is a list containing the index of the annotation, the name of the entity, and a list containing the start and end character of the annotation.
* `labels`: List of labels associated to each of the tokens of the queried text.
* `normalized_text`: Preprocessed text.
* `probabilities`: Probabilities associated to each of the tokens with respect to each of the labels.
* `raw_text`: Query text.
* `tagged_string`: Text queried with the annotations added.
* `tokens`: List of tokens found in the queried text.

## Usage example

To write down the text string *patient with squamous cell carcinoma of the border of the tongue*, the following request must be made:

```bash
curl --location --request POST 'http(s)://<server url>/neoplasm_morphologies' \
--header 'Content-Type: application/json' \
--data-raw '{
     "text":"patient with squamous cell carcinoma of the edge of the tongue"
}'
```

and the answer will be the following:

```javascript
{
     "entities": [
         [
             "T1",
             "MORPHOLOGY_NEOPLASM",
             [
                 [
                     13,
                     36
                 ]
             ]
         ]
     ],
     "labels": [
         "EITHER",
         "EITHER",
         "B-MORPHOLOGY_NEOPLASM",
         "I-MORPHOLOGY_NEOPLASM",
         "EITHER",
         "EITHER",
         "EITHER",
         "EITHER"
     ],
     "normalized_text": "patient with squamous cell carcinoma of tongue border",
     "probabilities": [
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.9997)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.0)",
                 "<START> (0.0)",
                 "<STOP> (0.0002)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.9727)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.0)",
                 "<START> (0.0)",
                 "<STOP> (0.0272)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.0)",
                 "B-MORPHOLOGY_NEOPLASM (0.9878)",
                 "I-MORPHOLOGY_NEOPLASM (0.0)",
                 "<START> (0.0)",
                 "<STOP> (0.0122)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.0005)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.999)",
                 "<START> (0.0)",
                 "<STOP> (0.0004)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0001)",
                 "OR(0.7672)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.232)",
                 "<START> (0.0)",
                 "<STOP> (0.0007)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.5432)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.408)",
                 "<START> (0.0)",
                 "<STOP> (0.0487)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.9662)",
                 "B-MORPHOLOGY_NEOPLASM (0.0)",
                 "I-MORPHOLOGY_NEOPLASM (0.0256)",
                 "<START> (0.0)",
                 "<STOP> (0.0081)"
             ]
         },
         {
             "ner": [
                 "<bk> (0.0)",
                 "OR(0.8688)",
                 "B-MORPHOLOGY_NEOPLASM (0.0002)",
                 "I-MORPHOLOGY_NEOPLASM (0.0327)",
                 "<START> (0.0)",
                 "<STOP> (0.0982)"
             ]
         }
     ],
     "raw_text": "patient with squamous cell carcinoma of tongue border",
     "tagged_string": "patient with <B-MORFOLOGIA_NEOPLASIA> squamous cell carcinoma <I-MORFOLOGIA_NEOPLASIA> of the tongue edge",
     "tokens": [
         "patient",
         "with",
         "carcinoma",
         "spinocellular",
         "of",
         "edge",
         "of",
         "language"
     ]
}
```