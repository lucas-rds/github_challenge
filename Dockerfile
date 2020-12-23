FROM python:3.9.1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/wait

CMD [ "bash", "start.sh" ]