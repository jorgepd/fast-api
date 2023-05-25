#!/bin/sh

# # change directories
# cd src

# run app
python -m uvicorn src:app --workers 1 --host 0.0.0.0 --port 5005
