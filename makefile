
ifeq ($(OS),Windows_NT)
    echo=@echo
    python=python
else
    echo=echo
    python=python3
endif

help:
	$(echo) "Liste des actions:\
    help   aide\
    pack   génération de l'archive et de la doc\
    start  démarrage du serveur\
    commit \
    recup  \
    save   \
    docu   génération de la documentation\
    ssl    génaration des certificats"

start:
	$(python) pyweb.pyz

pack: _docu_
	mkdir -p run
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

# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# ------
# cat ~/.ssh/id_rsa.pub
# ssh -T git@github.com
# git clone git@github.com:Koala-Kaolin/pyweb.git
# ------
# git remote -v
# git remote set-url origin https://github.com/Koala-Kaolin/pyweb.git
# ------
# git config -l

