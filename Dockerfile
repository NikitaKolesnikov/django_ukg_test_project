# Create ukg_restaurant directory in base image
FROM python:3.8-alpine
RUN apk update && apk add --no-cache postgresql-dev musl-dev gcc libffi-dev make git && mkdir /python
RUN mkdir /code
WORKDIR /code

# Add dependency files
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

# Install dependencies
RUN pip install --upgrade pip==21.3.1 && pip install pipenv
RUN pipenv install --dev

# Copy necessary files
COPY ./conf/.pylintrc /python
COPY ./conf/mypy.ini /python
COPY ./conf/.coveragerc /python

# Copy over all the code
COPY . /code/