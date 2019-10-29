![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rauanisanfelice/R-Analise-Credito.svg)
![GitHub top language](https://img.shields.io/github/languages/top/rauanisanfelice/R-Analise-Credito.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/rauanisanfelice/R-Analise-Credito.svg)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/rauanisanfelice/R-Analise-Credito.svg)
![GitHub contributors](https://img.shields.io/github/contributors/rauanisanfelice/R-Analise-Credito.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/rauanisanfelice/R-Analise-Credito.svg)

![GitHub stars](https://img.shields.io/github/stars/rauanisanfelice/R-Analise-Credito.svg?style=social)
![GitHub followers](https://img.shields.io/github/followers/rauanisanfelice.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/rauanisanfelice/R-Analise-Credito.svg?style=social)

# Projeto Geolocalização em Python/Django

Projeto de geolocalização que utiliza Mapbox.

Neste projeto você consegue:
* Localizar um endereço e realizar uma demarcação de um raio;
* Salvar uma loja e realizar uma demarcação de um raio;
* Salvar um polígno;

![Exemplo área]()  
![Exemplo Polígino]()


Neste projeto possui duas formas de plotar os polígnos no mapa.
1. É realizado um cálculo para montar todo o polígno;
2. Utilizando a biblioteca Turf.js;

## Criando o ambiente;

1. Inicialização dos container

```
docker-compose up -d
```

2. Configurando o pgAdmin

Acesse o link:

[pgAdmin](http://localhost:80)

Realize o login:
>User: admin  
>Pass: admin

Clique em: Create >> Server

Conecte no Banco com os seguintes parametros:  

Name: #nome desejado#  
>Host: mapbox-postgre
>Port: 5432  
>DB  : postgres  
>User: postgres  
>Pass: docker123

3. Criando um Ambiente Virtual e ativando

```
python3 -m venv venv
source ./venv/bin/activate
```

4. Instalando as dependencias

```
pip3 install -r requirements.txt
```

5. Cria todas as tabelas no Banco de Dados:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Subo o site
```
python3 manage.py runserver
```

7. Cria um usário com privilégios

```
python3 manage.py createsuperuser
```

8. Trocando o token de acesso do Mapbox

Altere **'your-token'** pelo seu token de acesso.

>user: admin  
>pass: admin


## Links:

[Mapbox Account](https://account.mapbox.com/)  
[Mapbox Docs](https://docs.mapbox.com/)  
[Mapbox Examples](https://docs.mapbox.com/mapbox-gl-js/examples/)  
[Mapbox Example Json](https://docs.mapbox.com/mapbox-gl-js/example/geojson-polygon/)  
[Mapbox Example JS API](https://docs.mapbox.com/mapbox-gl-js/api/)  
[Geocoding](https://docs.mapbox.com/api/search/#geocoding)  
[Doc Search Maps](https://docs.mapbox.com/api/search/)  
[Doc API Maps](https://docs.mapbox.com/mapbox-gl-js/api/#point)  
[Realizar RAIO](https://stackoverflow.com/questions/37599561/drawing-a-circle-with-the-radius-in-miles-meters-with-mapbox-gl-js)  
[Docs Draw](https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/)  

[Turf Draw](http://turfjs.org/docs/#area)  
[Turf Exemplo](https://docs.mapbox.com/help/tutorials/analysis-with-turf/#add-turf)

[Debug Django VScode](https://code.visualstudio.com/docs/python/tutorial-django)  
[Point Inside a Polygon](https://automating-gis-processes.github.io/CSC18/lessons/L4/point-in-polygon.html)