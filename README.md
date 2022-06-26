# Welcome to White-prince :crown:

 [![White-prince](https://github.com/White-prince/White-prince/blob/main/assets/White-prince_0.jpg?raw=true)](https://white-prince.github.io/Homepage/)

You can follow me on my social networks:

[![Twitter](https://img.shields.io/badge/-Twitter-131313?style=for-the-badge&logo=Twitter)](https://twitter.com/White_prince_0)

[![Instagram](https://img.shields.io/badge/-Instagram-131313?style=for-the-badge&logo=Instagram)](https://www.instagram.com/0xe_white_prince_ex0/)

[![Telegram](https://img.shields.io/badge/-Telegram-131313?style=for-the-badge&logo=Telegram)](https://t.me/Dark_Hub_info)

[![VK](https://img.shields.io/badge/-VK-131313?style=for-the-badge&logo=VK)](https://vk.com/id333667069)

[![Facebook](https://img.shields.io/badge/-Facebook-131313?style=for-the-badge&logo=Facebook)](https://www.facebook.com/profile.php?id=100023988285502)

# Vedmenko.production Webpage :globe_with_meridians:

Website for best project of films.

## Preview :desktop_computer:

![Vedmenko](https://github.com/White-prince/Vedmenko.production/blob/main/taskmanager/static/images/pr.jpg?raw=true)

## Installation :gear:

If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    git clone https://github.com/White-prince/Vedmenko.production.git

You will need to install:

    pip install Django

If the library doesn't install, try updating pip.

## Usege :information_source:

I use mailgun to send emails, in order to run this feature, register on mailgun or sandgrid. Replace these fields with your login, password:

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    RECIPIENTS_EMAIL = ['e-mail'] - recipient

    DEFAULT_FROM_EMAIL = 'e-mail' - sender

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_HOST_USER = 'login'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_PORT = ### - your port
    EMAIL_USE_TLS = True

To start the server:
    
    python manage.py runserver

Hope this code helps you :crown:
