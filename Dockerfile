FROM python:2.7

ENV HOME=/home

COPY jfantom $HOME/jfantom
RUN pip install -e $HOME/jfantom/

ENTRYPOINT [ \
    "gunicorn", \
    "--bind", "0.0.0.0:8000", \
    "--workers", "4", \
    "main:app" ]
