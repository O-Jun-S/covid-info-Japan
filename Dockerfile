FROM python
RUN mkdir /workspace
WORKDIR /workspace
RUN pip install --upgrade pip --no-cache-dir
RUN pip install flask
RUN pip install requests
RUN pip install pandas
RUN pip install Flask-APScheduler
ENV FLASK_APP=main.py
