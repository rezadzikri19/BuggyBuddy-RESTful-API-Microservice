#!/bin/bash
source venv/Scripts/activate

uvicorn main:app --host 0.0.0.0 --port 80 --reload