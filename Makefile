SHELL := /bin/bash
TZ    := America/Chicago
STAMP := $(shell date +"%Y-%m-%dT%H-%M-%S%z")

.PHONY: help validate new-agent new-handshake rollup apply-decision

help:
	@echo "Targets:"
	@echo "  make validate"
	@echo "  make new-agent N=A1"
	@echo "  make new-handshake [N=01]"
	@echo "  A=A1 make rollup"
	@echo "  H=handshakes/HH-<stamp>-<seq> make apply-decision"

validate:
	@bash scripts/validate.sh

new-agent:
	@python3 scripts/aidt.py new-agent --id $${N:?Missing N= e.g. A1}

new-handshake:
	@python3 scripts/aidt.py new-handshake --seq $${N:-01}

rollup:
	@python3 scripts/aidt.py rollup --agent $${A:?Missing A= A1|A2|A3|...}

apply-decision:
	@python3 scripts/aidt.py apply-decision --handshake $${H:?Missing H= path to HH folder}
