# [ENERGYCODE] (c) 2025
# .github/install_packages.R
# Script auxiliar para instalar paquetes CRAN listados en packages.txt
# Usado por GitHub Actions (publish.yml)

pkgs_file <- "packages.txt"

if (!file.exists(pkgs_file)) {
  stop("Archivo packages.txt no encontrado en la raíz del repositorio",
       call. = FALSE)
}

pkgs <- readLines(pkgs_file)
# filtra comentarios y líneas vacías
pkgs <- trimws(pkgs[!grepl("^#|^\\s*$", pkgs)])
pkgs <- pkgs[nzchar(pkgs)]

if (length(pkgs) > 0) {
  cat("Instalando", length(pkgs), "paquetes CRAN:\n")
  print(pkgs)

  install.packages(
    pkgs,
    repos = "https://packagemanager.posit.co/cran/__linux__/jammy/latest",
    Ncpus = parallel::detectCores(logical = TRUE),
    quiet = TRUE
  )
} else {
  message("No se encontraron paquetes válidos para instalar en packages.txt")
}
