FROM centos:centos6
MAINTAINER Nozomu Kaneko <nozom.kaneko@gmail.com>

RUN yum update -y
# RUN rpm -Uvh http://download.jubat.us/yum/rhel/6/stable-0.5.4/x86_64/jubatus-release-6-1.el6.x86_64.rpm
# RUN rpm -Uvh http://download.jubat.us/yum/rhel/6/stable-0.6.0/x86_64/jubatus-release-6-1.el6.x86_64.rpm
RUN rpm -Uvh http://download.jubat.us/yum/rhel/6/stable-0.6.5/x86_64/jubatus-release-6-1.el6.x86_64.rpm
RUN yum install -y jubatus

RUN mkdir -p /jubatus/data
ADD recommender.json /jubatus/recommender.json

CMD ["jubarecommender", "--configpath", "/jubatus/recommender.json", "--datadir", "/jubatus/data"]
EXPOSE 9199
