environment:
	pip install -r app/backend/requirements/dev.txt
	npm install app/frontend

db-service:
	$ docker-compose -p ali -f app/backend/docker-compose.yml up -d mongodb
	$ docker-compose -f app/backend/docker-compose.yml ps

run-backend: db-service
	uvicorn main:app --app-dir app/backend --reload

run-frontend:
