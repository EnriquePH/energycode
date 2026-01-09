<!-- badges: start -->

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Last commit](https://img.shields.io/github/last-commit/EnriquePH/energycode?color=blue)](https://github.com/EnriquePH/energycode/commits)
[![Repo Size](https://img.shields.io/github/repo-size/EnriquePH/energycode)](https://github.com/EnriquePH/energycode)
[![Built with Quarto](https://img.shields.io/badge/Built_with-Quarto-1f77b4?logo=quarto&logoColor=white)](https://quarto.org)
[![Netlify Status](https://api.netlify.com/api/v1/badges/d638f799-bbf7-4905-99e0-7696e734c879/deploy-status)](https://app.netlify.com/sites/energycodeorg/deploys)
[![Quarto Publish](https://github.com/EnriquePH/energycode/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/EnriquePH/energycode/actions/workflows/publish.yml)

</div>

<!-- badges: end -->

# ENERGYCODE Website

**My personal blog on Data Science, Mathematics, Engineering and Programming**

<p align="center">
  <a href="https://www.energycode.org">
    <img src="./img/logo/web_logo.png" alt="ENERGYCODE logo" width="300">
  </a>
</p>

<p align="center">
  <strong><a href="https://www.energycode.org">Visit the site →</a></strong>
</p>

This repository contains the full source code for
**[energycode.org](https://www.energycode.org)**, a personal technical blog with
articles, tutorials and resources on:

- Mathematics and Statistics
- Data Science and Machine Learning
- Engineering and Scientific Computing
- Programming (mainly R, Python and related tools)

## Contents

- ✏️ Blog posts and tutorials written in **Quarto** (`.qmd` files)
- 📊 Interactive visualizations and reproducible examples
- ⚙️ Custom website configuration, themes and styling
- 📚 Curated collection of projects and technical notes


## Quick start (local preview)

```bash
# Clone the repository
git clone https://github.com/EnriquePH/energycode.git
cd energycode

# Render the site locally
quarto render

# Or use live preview
quarto preview
```

## Required R packages

The site uses the following packages (automatically installed during render if
missing):

```R
install.packages(c("plot3D", "ggplot2", "hexSticker"))  # CRAN packages
remotes::install_github("EnriquePH/marketconf")         # Custom package
```

## Contributing
Contributions, suggestions and corrections are welcome! Feel free to:
* Open an issue
* Submit a pull request
* Share feedback on any post

## Deployment

The site is published automatically to:

- **GitHub Pages**  
  [https://enriqueph.github.io/energycode/](https://enriqueph.github.io/energycode/)    
  Triggered by pushes to `main` via `.github/workflows/publish.yml`

- **Netlify** (custom domain)  
  [www.energycode.org](https://www.energycode.org)    
  Auto-deployed via Netlify webhook  
  Build command: `quarto render`  
  Output directory: `_site`

## Author
Enrique Pérez Herrero

* GitHub: [@EnriquePH](https://github.com/EnriquePH)
* LinkedIn: [eph3000](https://www.linkedin.com/in/eph3000)

**Built with [Quarto](https://quarto.org)** • Licensed under the [MIT License](LICENSE)
