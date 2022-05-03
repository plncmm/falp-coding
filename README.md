Official repository for the experiments performed in the paper: Automatic support system for tumor coding in pathology reports in Spanish.

The ner folder contains the code associated with the first step of our system, where the NER models are trained using the Flair framework. The coding folder corresponds to the source code used to perform the second step, where pre-trained NER models are used to annotate documents, and then, through our coding method, the codes are assigned. Finally, the app folder contains a web app to test the annotations made by the NER model.

In addition, the following resources are available:

1. Annotation guidelines: https://doi.org/10.5281/zenodo.5541839
2. FALP corpus: https://doi.org/10.5281/zenodo.5555431
