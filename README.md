# Build docker cluster with celery and RabbitMQ
Simply run Celery and RabbitMQ with Docker, and generate worker clusters with just ONE command.

## Usage

Running as docker containers

```bash
docker-compose build
docker-compose up --scale worker=5
docker-compose ps

# Run task 
docker exec -it celery_worker_1 bash
python -m test_celery/run_tasks

```
