FROM python:3

WORKDIR /src/Reuters

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "App.py" ]
