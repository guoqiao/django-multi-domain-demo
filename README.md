# django-multi-domain-demo
Visit the same Django site from different domains, get different theme, content or behave according to the domain.

## How to run

### run django server:

    python manage.py migrate
    python manage.py loaddata fixtures/*.json
    python manage.py runserver

### add this to `/etc/hosts`:

    127.0.0.1 pact.co.nz
    127.0.0.1 twa.co.nz

### add nginx conf:

    server {
        listen 80;
        server_name pact.co.nz twa.co.nz;
        proxy_set_header X-Forwarded-Server $host;


        location / {
            proxy_pass http://127.0.0.1:8000;
        }
    }

### restart nginx:

    sudo service nginx restart

Now you can open two tabs in the same browser, and visit the site from both domain, you will see different content on the same page.
