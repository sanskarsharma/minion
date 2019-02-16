FROM python:3.7-alpine

#================================================================
# add dependencies
#================================================================

RUN apk add --update --no-cache g++ gcc libffi-dev

#================================================================
# pip and required modules install
#================================================================

### Upgrade pip to prevent errors
RUN pip install setuptools --upgrade
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#================================================================
# source code copy and setup
#================================================================
RUN mkdir -p /minion
WORKDIR /minion
ADD . /minion

#================================================================
# expose the correct port and run
#================================================================
EXPOSE 5665
# alpine images don't have bash installed by default
# sh shell can be used for our use-case
ENTRYPOINT /bin/sh run.sh