environment:
	pip install -r app/backend/requirements/dev.txt
	npm ci app/frontend

run-db:
	$ docker-compose -p alli -f app/docker-compose.yml up -d mongodb
	$ docker-compose -f app/docker-compose.yml ps

run-backend: db-service
	uvicorn main:app --app-dir app/backend --reload

npm-install:
	npm ci --prefix app/frontend

run-frontend:
	npm run dev --prefix app/frontend
	
build-frontend:
	npm run build --prefix app/frontend

up-compose:
	docker-compose -p alli -f app/docker-compose.yml up -d --build
	docker-compose -p alli -f app/docker-compose.yml ps

down-compose:
	docker-compose -p alli -f app/docker-compose.yml down
	docker-compose -p alli -f app/docker-compose.yml ps

ps-compose:
	docker-compose -p alli -f app/docker-compose.yml ps
