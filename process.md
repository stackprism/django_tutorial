1. Created "django_tutorial" repository on Github
2. Launched "django" EC2 machine on AWS
3. Setup DynDNS
4. Verify python version is compatable with the desired django app.
    dpkg -l python | grep 2.7
5. If using pip for django installation make sure you have python-setuptools installed
    apt-get install python-setuptools
6. Install the database of choice, if not using the internal one
    apt-get install mysql-server -y 
7. Download pip for installation
    curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
8. Install pip
    python get-pip.py
9. Install django
    pip install django
10. Verify correct django installation
    print(django.get_version())
11. Install webserver and fastcgi (Apache with mod_wsgi works as well as uwsgi)
    aptitude install nginx python-flup
12. Create directory to run django from, here we choose /opt due to http://www.pathname.com/fhs/pub/fhs-2.3.pdf
    mkdir -p django_apps
