## Dockerfile test for golf application
## Command to build the image (execute from MyGolfapp level):
## docker build -t golfapptest -f Dockerfile .

FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

## Expose port 5000
EXPOSE 5000

## Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
