FROM lambci/lambda:build-python3.8

WORKDIR /var/task

ADD . /var/task
# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

# Additional RUN commands here
RUN yum clean all && \
   yum -y install mysql-devel


RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install --dev
CMD ./start.sh

