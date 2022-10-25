environment:
	pip install -r app/backend/requirements/dev.txt
	npm install app/frontend

db-service:
	$ docker-compose -p ali -f app/docker-compose.yml up -d mongodb
	$ docker-compose -f app/docker-compose.yml ps

run-backend: db-service
	uvicorn main:app --app-dir app/backend --reload

npm-install:
	npm ci --prefix app/frontend

run-dev:
	npm run dev --prefix app/frontend
	
run-build:
	npm run build --prefix app/frontend
