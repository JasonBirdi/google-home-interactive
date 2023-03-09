# Use an official Python runtime as a parent image
FROM python:3.10

ADD main.py .

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
#     # --trusted-host pypi.python.org: Tell pip to trust the specified host when downloading packages
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Expose port 80 for the Flask app
# EXPOSE 80

# # Set the environment variable for Flask to know which file to run
# ENV FLASK_APP=main.py

# Run the command to start the program using main.py
CMD ["python", "./main.py"]