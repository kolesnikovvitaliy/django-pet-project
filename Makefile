init: build push deploy

build: build_django_pet_project

build_django_pet_project:
	docker --log-level=debug build --pull --file=Dockerfile.prod --tag=${REGISTRY}/django_pet_project_web:${IMAGE_TAG} .

push: push_django_pet_project 

push_django_pet_project:
	docker push ${REGISTRY}/django_pet_project_web:${IMAGE_TAG}


deploy:
	ssh ${HOST} -p ${PORT} 'rm -rf site_${IMAGE_TAG}'
	ssh ${HOST} -p ${PORT} 'mkdir site_${IMAGE_TAG}'
	scp -P ${PORT} -r ./data ${HOST}:site_${IMAGE_TAG}/data
	scp -P ${PORT} docker-compose.prod.yml ${HOST}:site_${IMAGE_TAG}/docker-compose.prod.yml
	
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && echo "COMPOSE_PROJECT_NAME=django_pet_project_web" >> .env'
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && echo "REGISTRY=${REGISTRY}" >> .env'
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && echo "IMAGE_TAG=${IMAGE_TAG}" >> .env'
	
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml pull'
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml up --build --remove-orphans -d'
	ssh ${HOST} -p ${PORT} 'rm -f site'
	ssh ${HOST} -p ${PORT} 'ln -sr site_${IMAGE_TAG} site'

rollback:
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml pull'
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml up --build --remove-orphans -d'
	ssh ${HOST} -p ${PORT} 'rm -f site'
	ssh ${HOST} -p ${PORT} 'ln -sr site_${IMAGE_TAG} site'

stop:
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml down -v'

start:
	ssh ${HOST} -p ${PORT} 'cd site_${IMAGE_TAG} && docker-compose -f docker-compose.prod.yml up --remove-orphans -d'