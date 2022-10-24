environment:
	pip install -r app/backend/requirements.txt
	npm install app/frontend

mongodb:
	docker-compose -p al-classify-interface -f app/docker-compose.yml up -d

run-backend:
	uvicorn main:app --app-dir app/backend --reload

run-frontend:
	