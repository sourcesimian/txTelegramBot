test:
	trial tests/test_*.py


run:
	twistd -n telegrambot -c ./config.ini


coverage:
	coverage run tests/test_*.py
	coverage html
	open htmlcov/index.html


develop:
	./setup_env.sh


clean:
	rm -rf build
	rm -rf _trial*
	rm -rf htmlcov
	rm -f twistd.log*
	rm -rf *.egg-info

analyse:
	find TelegramBot -name '*.py' | xargs pep8 --ignore E501
	find TelegramBot -name '*.py' | xargs pyflakes
	find TelegramBot -name '*.py' | xargs pylint -d invalid-name -d locally-disabled -d missing-docstring -d too-few-public-methods -d protected-access


to_pypi_test:
	python3 setup.py register -r pypitest
	python3 setup.py sdist upload -r pypitest


to_pypi_live:
	python3 setup.py register -r pypi
	python3 setup.py sdist upload -r pypi


from_pypi_test:
	pip install --extra-index-url https://testpypi.python.org/pypi txTelegramBot
