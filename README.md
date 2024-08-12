# Remote RXD

CLI y servidor para el almacenamiento de ENVs

## Funcionaes basicas

- Almacenamiento de ENVIRONMENTS de forma remota
- Organizacion por Projects y ENVIRONMENTS
- Cifraddo para las envs usando ssh
- uso de vault para el almacenamiento remoto de las ENVs
- CLI simple similar en cirtos aspectos a git

## Funciones a futuro

- Uso de una DB de tipo blockchain para crear un historial de las ENVs
- Implementacion de otros cifrados de extremo a extremo


## Help
```bash

# Generic
rrxd remote set https://jalo.tech
rrxd email <EMAIL_OF_USER> # este email se enviara en cada request a la api
rrxd remote
rrxd key <PRIVATE_DIR_KEY>

# DevOps
# Registrar un nuevo usuario
rrxd register user -k <PUBLIC_KEY>

# Crear un nuevo proyecto
rrxd create project <NAME_OF_PROJECT> -e <ENVIRONMENT>

# Crear un nuevo environment
rrxd create env <ENVIRONMENT>

# Crear un secret 
rrxd create secret accounts -p <NAME_OF_PROJECT> -e <ENVIRONMENT>

# Development
# Get envs de un projecto y environment especifico
rrxd get -p <NAME_OF_PROJECT> -e <ENVIRONMENT>

# Get secret de forma interactiva
rrxd get 

# List projects
rrxd list -p

# List environments
rrxd list -p

```

