# Active Learning Labelling Interface

This project is a generic web interface that researchers can use to label instances of a dataset. The labeling process is difficult and expensive. However, some machine-learning techniques can be used to facilitate this activity. The active learning technique is a simple and powerful example. Active learning can select the instances that, if labeled, will present the best performance gain for the model. Thus, this project generates a user-friendly web interface that facilitates the labeling process of instances of a dataset.

## Installation and Execution

To use this project, users must have python version 3.8 or higher and node version 16.0 or higher installed on their computer.

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

The installation and running process is quite simple. The user must run the following commands in the terminal:

 - ``make environment``: install project dependencies
 - ``make mongodb``: initialize the database
 - ``make run-backend``: run the backend server
 - ``make run-frontend``: run the frontend server

## License

This project is licensed under the terms of the MIT license.