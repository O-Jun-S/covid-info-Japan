FROM python
RUN mkdir /workspace
WORKDIR /workspace
RUN pip install --upgrade pip --no-cache-dir
RUN pip install flask
RUN pip install requests
RUN pip install pandas
RUN pip install Flask-APScheduler
RUN pip install gunicorn
COPY app/ /workspace/
ENV FLASK_APP=/workspace/app.py

EXPOSE 80
