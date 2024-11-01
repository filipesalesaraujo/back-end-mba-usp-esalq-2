# Django FastAPI MBA USP ESALQ

Este projeto é uma integração entre Django e FastAPI, desenvolvido como parte do curso de MBA da USP ESALQ.

## Estrutura do Projeto

- **Django**: Utilizado para a administração e backend principal.
- **FastAPI**: Utilizado para endpoints de alta performance.

## Requisitos

- Python 3.8+
- Django 3.2+
- FastAPI 0.65+
- Uvicorn

## Instalação

1. Clone o repositório:
	```bash
	git clone https://github.com/seu-usuario/django-fastapi-mba-usp-esalq.git
	```
2. Navegue até o diretório do projeto:
	```bash
	cd django-fastapi-mba-usp-esalq
	```
3. Crie um ambiente virtual:
	```bash
	python -m venv venv
	```
4. Ative o ambiente virtual:
	- No Windows:
		```bash
		venv\Scripts\activate
		```
	- No Unix ou MacOS:
		```bash
		source venv/bin/activate
		```
5. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```

## Uso

1. Execute as migrações do Django:
	```bash
	python manage.py migrate
	```
2. Inicie o servidor Django:
	```bash
	python manage.py runserver
	```
3. Inicie o servidor FastAPI:
	```bash
	uvicorn app.main:app --reload
	```