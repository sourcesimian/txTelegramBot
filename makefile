test:
	trial tests/test_*.py


service:
	twistd -n telegrambot -c docker/example/config.ini


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


to_pypi_test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest


to_pypi:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi


from_pypi_test:
	pip install --extra-index-url https://testpypi.python.org/pypi txTelegramBot
