FROM python
RUN mkdir /workspace
WORKDIR /workspace
RUN pip install --upgrade pip --no-cache-dir
RUN pip install flask
RUN pip install requests
RUN pip install pandas
