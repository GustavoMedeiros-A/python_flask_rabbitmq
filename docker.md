# Base Docker Commands (BASH/CLI)

```sh
docker ps
docker ps -a

docker stop b148c8a0ad6f
docker rm -f b148c8a0ad6f

docker image list
docker rmi b148c8a0ad6f

docker prune -f --volumes --image

docker-compose up -d
docker-compose build
docker-compose exec <service> sh

docker network create default-svc-network
docker network ls
```
