SHELL := /bin/sh

doc:
	snowboard html -o docs/api.html docs/api.apib
	vanadia --input docs/api.apib --output docs/api.postman_collection.json

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;

test:
	pytest

format:
	black .

lint:
	flake8 .

sort:
	isort

dump_data:
	python manage.py load_data -f DEINFO_AB_FEIRASLIVRES_2014.csv