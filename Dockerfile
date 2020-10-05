FROM python:3
WORKDIR /usr/src/app
EXPOSE 8082

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]
