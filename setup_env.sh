#! /bin/bash

if declare -f deactivate >/dev/null; then
    echo "- deactivating current virtual env"
    deactivate
fi

if [ -e virtualenv/ ]; then
    echo "- existing virtualenv found"
else
    python3 -m venv virtualenv
fi

if [ ! -e virtualenv/ ]; then
    echo "! virtualenv expected" 1>&2
    exit 1
fi

. ./virtualenv/bin/activate

if ! declare -f deactivate >/dev/null; then
    echo "! virtualenv did not activate" 1>&2
    exit 1
fi

python setup.py develop
