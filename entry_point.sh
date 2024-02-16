#!/bin/bash
python -m venv venv

if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    source venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 5)" == "MINGW" ]; then
    source venv/Scripts/activate
fi

pip install .