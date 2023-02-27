FROM python:3.9 

# our working directory is /app
WORKDIR /app

# copy our requirements.txt into the image
COPY requirements.txt requirements.txt

# install all our dependencies
RUN pip3 install -r requirements.txt

# copy source files in
COPY . .

CMD [ "python3", "main.py" ] 