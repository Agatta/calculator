# Calculator

[![Pylint](https://github.com/Agatta/calculator/actions/workflows/pylint.yml/badge.svg)](https://github.com/Agatta/calculator/actions/workflows/pylint.yml)
[![Python application](https://github.com/Agatta/calculator/actions/workflows/python-app.yml/badge.svg)](https://github.com/Agatta/calculator/actions/workflows/python-app.yml)

Projekt zaliczeniowy: kalkulator w Pythonie z testami (pytest, coverage), analizą statyczną (pylint) i usługą webową (Flask).

## Uruchomienie

```
pip install -r requirements.txt
python calculator.py      # przykłady wywołania
python app.py             # http://127.0.0.1:5000/calculate?op=sum&arg1=2&arg2=5
pytest -v                 # testy
```

Autor: Agata
