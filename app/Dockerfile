# Use an official Python runtime as an image
FROM python:3.6

WORKDIR /app
COPY ./ ./
# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist

# COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD python3 app.py
