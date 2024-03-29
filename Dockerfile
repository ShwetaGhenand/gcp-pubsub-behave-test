FROM python:3-slim

COPY src/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY src/. /src

WORKDIR /src

ENTRYPOINT [ "behave" ]

CMD [ "./features/example.feature" ]
