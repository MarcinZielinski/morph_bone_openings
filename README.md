Django based application with embedded web template to predict morphological openings from leg bone XRay photos.



To run:

1. Place pre-trained model with weights from Professor Bogdan Kwolek AGH site in folder `ml_model`
2. Execute below commands in project main folder:

```commandline
pip3 install
python3 manage.py migrate
python3 manage.py runserver
```

It will start the server and web application as well. Web app starts on 127.0.0.1:8000.