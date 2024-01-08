# Recapify

Recapify is an open source project that summarizes videos on YouTube, now you can see if the video topics might be of interest to you

## Setup Virtual Environment (venv)

### Linux

These commands bellow are creating a folder .venv and activate the environment in the terminal.

```bash
python3 manage.py venv .venv
source .venv/bin/activate
```

### Windows

```bash
py manage.py venv .venv
.venv/Scripts/activate
```

## Installing Dependencies (requirements.txt)

```bash
pip install -r requirements.txt
```

## Make migrations

We already have all sql instructions for structure our database, we just need apply it in our database before runserver

```bash
python3 manage.py migrate
```

## Running server

```bash
python3 manage.py runserver
```
