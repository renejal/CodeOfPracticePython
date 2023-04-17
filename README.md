# code de practiva unittest con python
# prueba nvim

# 1. install pre-commit
# 2. crear el archivo .pre-commit-config.yaml
    "instalar hooks"
    pre-commit install
    "correr hooks con "
    pre-commit run
    "update hooks"
    pre-commit update
# 3 black
    "comando correige todo con normas pep8"
    black phat_file
    "se puede agrear mas comandos con como, este comando agregar
    --diff : muestra en consola , --checke : Valida no gurada cambios,
    --color: pintar las lineas que se eliminar y las que se agregan "
    black ./file --diff --color --check
