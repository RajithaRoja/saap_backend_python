FROM python:3.11
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY ./docker_entrypoint.sh .
RUN chmod +x ./docker_entrypoint.sh
ENTRYPOINT ["/bin/bash", "docker_entrypoint.sh"]
RUN apt update && apt upgrade -y && apt install nano -y
COPY . .
EXPOSE 8000
EXPOSE 50051
