# Django-Rest-Framework
Knox Authentication

 ## [django-rest-knox](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-knox)

[Django-rest-knox](https://github.com/James1345/django-rest-knox)  library provides models and views to handle token based authentication in a more secure and extensible way than the built-in TokenAuthentication scheme - with Single Page Applications and Mobile clients in mind. It provides per-client tokens, and views to generate them when provided some other authentication (usually basic authentication), to delete the token (providing a server enforced logout) and to delete all tokens (logs out all clients that a user is logged into).

Now, you are ready to create user auth using knox where a token is generated for a user to login and access data.  

You need to install the following:  

`pipenv install djangorestframework`  

`pipenv install django-rest-knox`

settings.py 

    REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
    
    'knox.auth.TokenAuthentication',
    
    )}

