# Run backend component

## Without Docker (development mode)

#### Create and activate python environment

1. Inside backend folder:

```
# Create the virtual environment
python -m venv env 
```

or

```
# Create the virtual environment
virtualenv -p python3 env
```

2. Activate python environment

```
# Activate the virtual environment (Linux/Mac)
source env/bin/activate
```

```
# Before activate allow execution (Windows)
Set-ExecutionPolicy RemoteSign
```

```
# Activate the virtual environment (Windows)
env\Scripts\activate
```

#### Install dependencies

With python env activated

```
pip install -r requirements.txt
```

### Run service

With python env activated

```
python src/service.py
```

## Using Dockerfile

#### Create Dockerfile 

Create a empty file with name `Dockerfile`
Set image base:

```
FROM python:3.12.3
```


## Unisg Docker Compose