# PPP Engenharia Elétrica - UFPB 
Página do PPP de criação do curso de Engenharia Elétrica da UFPB.

## Para clonar esse repositório:
```
git clone git@github.com:rsmarinho/ppp.git
```

## Para fazer funcionar

dentro do diretório plots/grade digite:
```
bokeh serve grade.py
```

dentro do diretório raiz, digite:
```
python3 -m http.server 8000 (se python 3)
```
ou
```
python -m SimpleHTTPServer 8000 (se python 2)
```

Caso tudo tenha corrido bem, vá ao navegador e digite
```
http://localhost:8000/build/html
```
