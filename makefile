
ifeq ($(OS),Windows_NT)
    echo=@echo
    python=python
else
    echo=echo
    python=python3
endif

help:
	$(echo) "Liste des actions:\
    help\
    pack\
    run\
    commit\
    recup\
    save\
    docu\
    ssl"

run:
	$(python) gui.py

pack: _docu_
	$(python) -m zipapp src -m "gui:App" -o pyweb.pyz  # -p $(python)

commit:
	git commit -a -m '"'`date +%s`'"'

save:
	cp -r ./* /media/narf/F32/python

recup:
	cp -fr /media/narf/F32/python/* .

_docu_:
	pep8 .
	$(python) src/doc.py

ssl:
	openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout run/privateKey.key -out run/certificate.crt
