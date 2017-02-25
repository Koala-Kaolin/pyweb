

# Unix vs windows

ifeq ($(OS),Windows_NT)
	echo=@echo
	python=f:/Python36-32/python.exe
	mkdirforce=@echo creer
	forcedel=@echo supprimer
	pep8=@echo pep8
	RED=
	ORANGE=
	GREEN=
	NC=
else
	echo=@echo
	python=python3
	mkdirforce=mkdir -p
	forcedel=rm -rf
	pep8=pep8
	RED=\033[0;31m
	GREEN=\033[0;32m
	ORANGE=\033[0;33m
	NC=\033[0m
endif


# Main goals

help:
	$(echo) "Commands list:"
	$(echo) "   $(ORANGE)help              $(NC)to display this message"
	$(echo) "   $(ORANGE)install           $(NC)to generate documentation en pyweb.pyz"
	$(echo) "   $(ORANGE)run [args="..."]    $(NC)to start the server"
	$(echo) "   $(ORANGE)test              $(NC)to start the server"
	$(echo) "   $(ORANGE)ssl               $(NC)to build certificates"

run:
	$(echo) "To get more options: $(ORANGE)make run args=\"-h\"$(NC)"
	$(python) pyweb.pyz $(args)

test:
	$(echo) "To get more options: $(ORANGE)make run args=\"-h\"$(NC)"
	$(python) pyweb.pyz -testing -nogui

install: document
	$(python) -m zipapp src -m "gui:main" -o pyweb.pyz  # -p $(python)
	$(mkdirforce) work
	$(echo) "pyweb.pyz $(GREEN) generated $(NC)"

ssl:
	openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout work/privateKey.key -out work/certificate.crt


# Sub goals

document:
	$(pep8) .
	$(pep8) src
	$(python) src/doc.py . src
	$(forcedel) src/__pycache__ ./__pycache__
	@$(echo) "pyweb $(GREEN) documented $(NC)"

commit:
	git commit -a -m '"'`date +%s`'"'

save:
	cp -r ./* /media/narf/F32/python

recup:
	cp -fr /media/narf/F32/python/* .

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

