debug:
	uvicorn app:app --reload

docker-up:
	docker build -t visado-back .
	docker run --rm --name visado-back --publish 8080:8080 --env-file ./app/assets/.env.local visado-back

docker-run:
	docker run --rm --name visado-back --publish 8080:8080 --env-file ./app/assets/.env.local visado-back
