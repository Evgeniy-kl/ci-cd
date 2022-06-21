FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /code/
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /code/
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
RUN ["flake8", "/code/", "--junitxml=reports/result.xml"]
RUN ["black", "/code/", "--junitxml=reports/result.xml"]