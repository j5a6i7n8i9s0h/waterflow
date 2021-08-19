#!/bin/bash
VENV = vp/bin
PYTHON = $(VENV)/python3

CMDLIST_FILE ?= -
# Building virtual python (vp)

.PHONY: create_vp
create_vp: 
	python3 -m venv vp
	$(VENV)/pip3 install --upgrade pip

.PHONY: vp_install
vp_install:
	$(VENV)/pip3 install -r requirements.txt

# Main command to build vp
.PHONY: vp
vp: create_vp vp_install

.PHONY: destroy_vp
destroy_vp: 
	rm -rf vp/

.PHONY: run_py
run_py:
	$(PYTHON) src/main.py 1,1,0.3

.PHONY: test
test:
	cd src/ && ../$(VENV)/coverage run --branch -m pytest . -vv --ignore=./vp/ && \
	../$(VENV)/coverage report --omit="../vp*" && \
	../$(VENV)/coverage html --omit="../vp*" --title "Function Coverage" -d ../output/coverage

.PHONY: clean
clean:
	rm -rf output/
	rm -rf vp/