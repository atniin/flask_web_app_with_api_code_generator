# Code generator for Flask APP (Web app, API included) 

## Why? How?
This is a simple tool to make life easier. Run the code (python3 create_structure.py) and it'll create the project structure for you.

This repository is not actively maintained but maybe I'll add some extra features in the future.

The structure:
```bash
app/
├── __init__.py
├── routes.py
├── services/
│   └── __init__.py
├── views/
│   ├── __init__.py
│   ├── get/
│   │   ├── __init__.py
│   │   └── index.py
│   └── post/
│       ├── __init__.py
└── api/
    ├── __init__.py
    ├── get/
    │   ├── __init__.py
    │   └── index.py
    └── post/
        ├── __init__.py
templates/
└── index.html
static/
├── css/
├── js/
└── images/
config/
└── __init__.py
README.md
requirements.txt
.gitignore
app.py
.env
```
