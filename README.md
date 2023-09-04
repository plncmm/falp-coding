Official repository for the paper: Automatic support system for tumor coding in pathology reports in Spanish.

The `ner-training` folder contains the code associated with the training of the NER model for the first step of our system; the NER models are trained using the Flair framework. The `ner-webservice` folder corresponds to the source code used to perform the first step, where pre-trained NER models annotate documents. Then, the `coding-webservice` folder contains the code to assign an ICD code to a mention. 

Each folder contains the documentation for each part describer above.

In addition, the following resources are also available:

1. Annotation guidelines: https://doi.org/10.5281/zenodo.5541839
2. FALP corpus: https://doi.org/10.5281/zenodo.5555431