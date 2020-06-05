FROM joyzoursky/python-chromedriver:3.6

WORKDIR /suite
COPY . /suite

RUN apt-get update && apt-get install -y google-chrome-stable 

RUN python -m pip install --upgrade pip
RUN pip install -r /suite/requirements.txt

ENV SUITE=$SUITE
CMD python -m pytest -m $SUITE 
