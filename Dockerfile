FROM python:3.11
# Start from the official Python base image.

WORKDIR /code
# Set the current working directory to /code.

COPY ./requirements.txt /code/requirements.txt
# Pass the requirements.txt to the folder we the app we using. 

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# no-cache-dir -> tells pip to not save the downloaded packages locally. Only related to pip!
# upgrade -> updgrade packages if they already installed

COPY . /code
# Copy the .app inside the /code and is important to put this near the end of the Dockerfile, to optimize the container image build times.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# Execute the code will run in the CMD.
