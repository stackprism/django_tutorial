#####This shows the course taken to arrive at the destination. It contains mistakes, missteps, and retracking - to arrive at the finished product look at step_by_step.md
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
22. We chose to use https://github.com/sixohsix/twitter so clone that and setup install
    cd ~/ git clone --recursive https://github.com/sixohsix/twitter 
    cd twitter 
    python setup.py install
23. Edit models.py to have a Search model with fields for ip_address, query, query_time, twitter_url, instagram_url and a unicode return function for shell inspection
24. Edit settings.py to include tweetgramsandwich to the list of installed apps
25. python manage.py sql tweetgramsandwich
26. python manage.py syncdb
27. Sign up with twitter and get a twitter application @StackerJoe and app name tweetgrahamsandwich
28. Get the oauth keys and credentials
29. FastCGI - so last year. uWSGI is the hotness. http://www.peterbe.com/plog/fcgi-vs-gunicorn-vs-uwsgi 
    sudo apt-get install gcc build-essential
    pip install was failing 
        with error code 1 in /tmp/pip-build-root/uwsgi
      solution:
    pip install versiontools
    pip install uwsgi
    mkdir /etc/uwsgi/vassals 
    vim /etc/uwsgi/vassals/intro.ini
30. Reconfigure the nginx, much of this was followed/inspired by http://bartek.im/blog/2012/07/08/simplicity-nginx-uwsgi-deployment.html
31. The more you know... Now we circle back and begin again
32. Install virtualenvwrapper - Virtualenv is like rbenv or rvm in that it allows a seperation of system installed libraries and user/project/directory installed libraries; thus providing the ability to install/run/switch-between multiple versions of <insert thing you need>. Hopefully virtualenv differs from the ruby tools by not being a pain while performing mundane tasks. The wrapper adds additional functionality in the current shell process: particulary keeping installation/management/tracking of the envs to the home folder, switching shell variables automatically when switching virtual envs, and tabcompletetion - because why memorize when you can <insert something that refers to automation and rhymes with ize> .
    pip install virtualenvwrapper
  add 
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/code
    source /usr/local/bin/virtualenvwrapper.sh
  to ~/.bashrc. The wrapper needs to be loaded after the path is set, because it manages the path.
33. Make a virtualenv
    mkvirtualenv django_intro
34. Reinstall django because now we only have access to things which are installed in our virtualenv.
    pip install django
35. For some reason, the virtualenv now needs libmysqlclint-dev, probably some ramification of trying to isolate the python env
    apt-get install libmysqlclient-dev
36. Now install mysql-python again
    pip install mysql-python
37. One of the reasons I wanted virtualenv was to mimic developer flow, so deploying is the next step. Fabric seems super similar to capistrano: fan-freaking-tastic.
    pip install fabric
38. 

