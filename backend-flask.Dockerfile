FROM python:3.8.10-slim
LABEL author="Maksim Kovtun"
LABEL description="This is a backend image for FairyTales"

COPY ./requirements.txt .
COPY ./requirements-back-flask.txt .
RUN pip install -r requirements-back-flask.txt

COPY ./backend_flask /backend_flask
COPY ./backend /backend_flask/backend

EXPOSE 8000

# CMD ["~/bash/sh"]
# ENTRYPOINT ["python"]

# CMD ["python", "./backend_flask/run_webserver.py"]
# CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "backend_flask.main:app"]
# CMD ["uvicorn ./backend_flask/main:app --port 8080"]
# docker build -t fairytales_back_flask:latest -f backend-flask.Dockerfile .
# docker run -d -p 8000:8000 fairytales_back_flask:latest
# docker exec -ti 28085ce5b034 /bin/sh
# docker run --rm -it --entrypoint bash fairytales_back_flask:latest
# docker tag fairytales_back_flask vdumchiviy/fairytales_back_flask 
# docker push vdumchiviy/fairytales_back_flask:latest