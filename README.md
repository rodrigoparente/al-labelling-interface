# Active Learning Labelling Interface

This project is a generic web interface that researchers can use to label instances of a dataset. The labeling process is difficult and expensive. However, some machine-learning techniques can be used to facilitate this activity. The active learning technique is a simple and powerful example. Active learning can select the instances that, if labeled, will present the best performance gain for the model. Thus, this project generates a user-friendly web interface that facilitates the labeling process of instances of a dataset.

## Summary

- [Tecnologies](#tecnologies)
- [Installation and Execution](#installation-and-execution)
  - [Development environment local](#development-environment-local)
  - [Development environment in Docker](#development-environment-in-docker)
  - [Production environment](#production-environment)
- [License](#license)

## Tecnologies

Technologies used in the backend:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Motor](https://motor.readthedocs.io/en/stable/) (MongoDB)
- [Uvicorn](https://www.uvicorn.org/)

Technologies used in the frontend:

- [Typescript](https://www.typescriptlang.org/)
- [React](https://reactjs.org/)
- [Tailwind](https://tailwindcss.com/)
- [Vite](https://vitejs.dev/)

Technologies used in the infrastructure:

- [Docker](https://www.docker.com/)

## Installation and Execution

### Development environment local

To use this project, users must have python version 3.8 (or higher), mongodb version 6.0 (or higher), and node version 16.0 (or higher) installed on their computer.

The installation and running process is quite simple. The user must run the following commands in the terminal:

- `make environment`: install project dependencies
- `make run-backend`: run the backend development server
- `make npm-install`: install node packages
- `make run-frontend`: run the frontend development server
- `make build-frontend`: build the frontend production artifact

### Development environment in Docker

To use this project, users must have [Docker](https://docs.docker.com/engine/install/ubuntu/) version 20.10 (or higher) and [Docker Compose](https://docs.docker.com/compose/install/other/) version v2.12 (or higher) installed on their computer.

Before running the services in container, it is necessery to create the **.env** file and edit its values:

```bash
cp ./app/templates/.env.dev.example ./app/.env
nano ./app/.env
```

With the **.env** configured, the user can execute the commands:

- `make run-db`: initialize the database in container
- `make up-compose`: run all services in container (development mode)
- `make down-compose`: remove containers
- `make ps-compose`: list containers

### Production environment

For the production environment, we have prepared some example configuration files in the **templates** folder.

## License

This project is licensed under the terms of the MIT license.
