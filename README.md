# VocalForLocal

Neighborhood Hacks 2021


Vocal For Local - Supporting your neighborhood and the local communities around, along with my teammates, last week. It supports local shops and daily wage workers by getting listed with us. We built a full fledged system with the utmost simplicity.

- A simple phone number - OTP login. It checks if the number is registered before or not and redirects to respective business registration page or business portal, and if it is a customer, then to the common page.
- It provides a list of all the shops and services around the customer, altered according to the location of the user.
- The user can search the product, service, or a specific shop, and the list will be altered according to the location of user.
- The user has access to the shop's number, timings, ratings, delivery/take-away, and the distance.
- Now, a peculiar thing about this is that, we needed a simple User Experience from both ends, therefore we chose not implement any payment gateway system, everything is flexible according to the local needs. Moreover listing down each and every product (and the expiry, price, etc.) can be tiresome for the local community, also then it would simply become E-commerce.

Since, this is a local product which alters according to the user's needs, it can be used globally, to support local communities around the world as it also has all languages supported around the world.

### Setup

```bash
git clone https://github.com/tusharnankani/VocalForLocal.git
```

Before you start working

```bash
git pull
```

After you are done making the changes

```
git pull

git add .
git commit -m "message"
git push
```

### Django Commands

- initial setup

```python
django-admin startproject VocalForLocal
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
```

Go to /admin

- username: tusharnankani
- password: python

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Thank you
