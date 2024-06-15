FROM python

WORKDIR /app

COPY . .

RUN pip3 install -r requirement.txt

EXPOSE 5000

CMD ["python3", "app.py"]