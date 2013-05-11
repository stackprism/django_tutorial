#NOTE there are not sudo prefixes here, you can run this however you want, we just omit all command prefixes
1. Created "django_tutorial" repository on Github
2. Launched "django" EC2 machine on AWS
3. Setup DynDNS
4. Verify python version is compatable with the desired django app.
    dpkg -l python | grep 2.7
5. If using pip for django installation make sure you have python-setuptools installed
    apt-get install python-setuptools
6. Install the database of choice, if not using the internal one, additionally install the appropriate python module (I like to install the debug when first learning)
    apt-get install python-mysqldb python-mysqldb-dbg mysql-server -y 
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
    mkdir -p /opt/django_apps
13. Create the intro project
    cd /opt/django_apps && django-admin.py startproject intro
14. Copy file from nginx/intro_site.conf into /etc/nginx/sites-available/ and link file into site-enabled Make sure to change the site name
    cp nginx/intro_site.conf /etc/nginx/sites_available/introsite.conf
    ln -s /etc/nginx/sites-available/intro_site.conf /etc/nginx/sites-enabled/intro_site.conf
15. Start python via CGI (This needs a wrapper obvs)
    python ./manage.py runfcgi host=127.0.0.1 port=8080
16. Hit your page!
17. Log in to mysql and run `create database 'django_intro';`
18. Edit settings.py, add .mysql to the database type, fill in the database, user, password, and host fields
19. Update timezone in settings.py
20. Python manage.py syncdb
21. Python startapp tweetgramsandwich
22. Edit models.py to have a Search model with fields for ip_address, query, query_time, twitter_url, instagram_url and a unicode return function for shell inspection
23. Edit settings.py to include tweetgramsandwich to the list of installed apps
24. python manage.py sql tweetgramsandwich
25. python manage.py syncdb
