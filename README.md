# Safety Drone Application

Leftover tools and spills on a warehouse floor are a common cause of injuries and downtime, and manual inspections are slow and easy to skip. This project puts a DJI Tello drone on autonomous patrol, using a YOLO-based vision pipeline to spot hazards on the floor, pin their location on a live map, and log them for cleanup. Built as a Python desktop app with PySide6 for live control and monitoring.

Full report: [resources/report.pdf](resources/report.pdf)

# Project structure
- Application source code can be found in `src/` folder
- Jupyter notebooks containing training can be found in `/notebooks` folder

# Prerequisites

Make sure you have the following installed:

- Python >= 3.11
- Pip  
- UV (recommended package manager)

## Install UV

```
pip install uv
```

## Install dependencies
```
uv sync
```

## Install models
Install the models from huggingface and move them into the `models` folder
```
https://huggingface.co/ondralol/deep-learning-cnn/tree/main
```

## Run the main app
```
uv run src/main.py
```

## Run jupyter notebooks
Run 
```
uv sync
```
Install kernel
```
uv run python -m ipykernel install --user --name safety-drone-app --display-name "safety-drone-app"
```
Run the notebook
```
uv run jupyter notebook
```
and select the "safety-drone-app" kernel \
Note: If running inside sagemaker, you need to copy `pyproject.toml` first

# Streaming
```
sudo ufw allow 8890/udp
sudo ufw allow 11111/udp
```