# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary tools
RUN apt-get update -qqy \
  && apt-get -qqy install wget gnupg unzip \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install Chrome Binary
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install Chromedriver
RUN CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
  && wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P /tmp \
  && unzip /tmp/chromedriver_linux64.zip -d /opt \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/chromedriver /usr/local/bin/chromedriver \
  && chown root:root /usr/local/bin/chromedriver \
  && chmod 0755 /usr/local/bin/chromedriver

# Install Selenium
RUN pip install --no-cache-dir -r requirements.txt selenium

RUN python MarkdownToHTML.py
