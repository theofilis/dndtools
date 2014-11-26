# dndtools
==========

An open source Django-based wiki-like web application for DnD.

## Status
------
This github repository is currently a clone of a private repository. It contains ONLY source codes of the application, not its data. 

Also, this readme file is just an early preview to be updated as soon as someone have the time. 

If you find anything wrong, just start an issue.

## Installation Guide
-----------------

### Ubuntu
Install all dependencies.
```
    virtualenv env
    source env/bin/activate
    pip install -r requirement.txt
```
Run django website.
```
    cd dndtools/
    chmod +x manager.py
    ./manager.py migrate
    ./manager.py syncdb
    
    ./manager.py runserver 0.0.0.0:8000
```

### Windows
Download [Django Stack](https://bitnami.com/stack/django).

### Mac
