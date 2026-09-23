# [ENERGYCODE] (c) 2026
# Makefile: local setup, render and publish helpers for the Quarto site.
# Run `make` or `make help` to list targets.

VENV       := .venv
PYTHON     := $(VENV)/bin/python
CRAN       := https://cloud.r-project.org

# Installs only packages that are missing (runs as one line of R)
R_SETUP := \
  pkgs <- trimws(readLines("packages.txt")); \
  pkgs <- pkgs[nzchar(pkgs) & !grepl("^\#", pkgs)]; \
  new <- setdiff(pkgs, rownames(installed.packages())); \
  if (length(new)) install.packages(new, repos = "$(CRAN)"); \
  if (!requireNamespace("marketconf", quietly = TRUE)) \
    remotes::install_github("EnriquePH/marketconf@master", upgrade = "never")

# Make Quarto use the project virtualenv for Python cells
export QUARTO_PYTHON := $(abspath $(PYTHON))

.DEFAULT_GOAL := help
.PHONY: help setup setup-r setup-py check render preview publish clean

help: ## List available targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

setup: setup-r setup-py ## Install all R and Python dependencies

setup-r: ## Install missing R packages from packages.txt + marketconf
	Rscript -e '$(R_SETUP)'

setup-py: $(PYTHON) ## Create .venv and install requirements.txt
	$(PYTHON) -m pip install --quiet --upgrade pip
	$(PYTHON) -m pip install --quiet -r requirements.txt

$(PYTHON):
	python3 -m venv $(VENV)

check: ## Run quarto check
	quarto check

render: ## Render the full site into _site/
	quarto render

preview: ## Live preview at http://localhost:4444
	quarto preview

publish: render ## Render and stage _site/ (served by Netlify from git)
	git add _site
	@echo "_site/ staged. Review with 'git status', then commit and push."

clean: ## Remove Quarto temp files (keeps _site/ and _freeze/)
	rm -rf .quarto
	find posts projects -name '*.quarto_ipynb' -delete
