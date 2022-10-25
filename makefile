environment:
	pip install -r app/backend/requirements.txt
	npm install app/frontend

mongodb:
	docker-compose -p al-labelling-interface -f app/docker-compose.yml up -d

run-backend:
	uvicorn main:app --app-dir app/backend --reload

npm-install:
	npm install app/frontend

run-dev:
	npm run dev --prefix app/frontend
	
run-build:
	npm run build --prefix app/frontend