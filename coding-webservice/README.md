## Installation

1. Create a virtual python environment and install the requirements from `requirements.txt`
2. Run the `index_m.py` and `index_t.py` files with the Python interpreter of the virtual environment created above for the creation of the indexes.
2. Launch the classification server with the command `<location of virtual environment binaries>/uvicorn main:app`

## Usage

This web service exposes endpoints for lookup in the CIE-O-M and CIE-O-T nomenclature at `/cie-o-m` and `/cie-o-t` respectively. To perform a search, a GET request must be sent to the respective endpoint with the search string in the `q` parameter.

The service will respond with a list of results, where each result is an object with the following properties:

* `code`: Code of the consulted nomenclature.
* `description`: Code description of the queried nomenclature.
* `score`: Value of the BM25F metric in the result (the higher it is, the closer this result is to the query string).

## Usage example

To search for the *tubular adenocarcinoma* text string in ICD-O-M, the following request must be made:

```bash
curl --location --request GET 'http(s)://<server url>/cie-o-m?q=adenocarcinoma%20tubular'
```

and the answer will be the following:

```javascript
[
     {
         "code": "8211/3",
         "description": "Tubular adenocarcinoma",
         "score": 14.65240778171962
     },
     {
         "code": "8211/6",
         "description": "Tubular adenocarcinoma, metastasis",
         "score": 7.883117241094898
     },
     {
         "code": "8210/3",
         "description": "Adenocarcinoma in adenomatous polyp",
         "score": 7.528550603683486
     },
     {
         "code": "8263/3",
         "description": "Adenocarcinoma in tubulovillous adenoma",
         "score": 7.19567170881193
     },
     {
         "code": "8210/2",
         "description": "Adenocarcinoma in situ in adenomatous polyp",
         "score": 6.563115285083312
     },
     {
         "code": "8503/3",
         "description": "Invasive intraductal papillary adenocarcinoma",
         "score": 6.25229547114941
     },
     {
         "code": "8571/3",
         "description": "Adenocarcinoma with bone and cartilage metaplasia",
         "score": 6.25229547114941
     },
     {
         "code": "8525/3",
         "description": "Low-grade polymorphic adenocarcinoma",
         "score": 6.0067746976636975
     },
     {
         "code": "8215/3",
         "description": "Anal gland adenocarcinoma",
         "score": 5.934968311877492
     },
     {
         "code": "8408/3",
         "description": "Eccrine papillary adenocarcinoma",
         "score": 5.934968311877492
     }
]
```