#!/bin/bash
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    source venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 5)" == "MINGW" ]; then
    source venv/Scripts/activate
fi

uvicorn main:app --host 0.0.0.0 --port 80 --reload