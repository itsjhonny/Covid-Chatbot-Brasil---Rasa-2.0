# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN pip install --upgrade pip
RUN pip3 install recognizers-text-suite
RUN pip install --no-cache-dir requests

# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt


# By best practices, don't run the code with root user
USER 1001