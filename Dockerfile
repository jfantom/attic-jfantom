FROM python:2.7

COPY FlaskApp /
RUN pip install virtualenv
RUN pip install --no-cache-dir -r requirements.txt 

RUN chmod +x /start.sh
CMD ["/start.sh"]

