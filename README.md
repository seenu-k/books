# REST API Development using Django
## ED17B015 | K Srinivasa Gopalan

***   


## Steps to run the project locally   


1. Clone repository:  
  
```console  
$ git clone https://github.com/seenu-k/books.git
```   
  
2. Go to `books`:    
  
```console   
$ cd books   
```
    
3. Install requirements:  
  
```console  
$ pip install -r requirements.txt  
```
  
3. Set up Database:   
   
```console  
$ python manage.py makemigrations   
$ python manage.py migrate   
```
   
4. Run the app:   
  
```console   
$ python manage.py runserver  
```

5. (Optional) Create superuser to access admin

```console
$ python manage.py createsuperuser
```
   

## Hosted Version in Heroku

[https://booksed17b015.herokuapp.com/api/v1/books/](https://booksed17b015.herokuapp.com/api/v1/books/)

[https://booksed17b015.herokuapp.com/api/external-books/](https://booksed17b015.herokuapp.com/api/external-books/)

Using Django Rest Framework, a browsable format of the API developed is hosted in the above URLs, with which the functionality can be seen within the browser window.

[https://booksed17b015.herokuapp.com/admin/](https://booksed17b015.herokuapp.com/admin/)

The above is the admin console for the app, with credentials attached in the submitted `.txt` file.

## Angular Frontend for Testing

The Angular frontend developed to test the above API (or any similar structured API) is as follows:

[https://booksed17b015.web.app/](https://booksed17b015.web.app/)

And the corresponding frontend SPA repository is as follows:

[https://github.com/seenu-k/books-spa](https://github.com/seenu-k/books-spa)

In particular, features like copying external API response to populate POST request and easy filtering mechanisms are incorporated.

The API base URL is also exposed to modification to be able to test similar API endpoints.

## Details

- The security key is configured both in the `.env` file as well as in `settings.py` for ease of development and testing, despite its safety risks. It needs to be rotated and secured before a production deployment.

- One of the assumptions made was about patch request with author object, since nested patching guidelines were not provided, assumed to be replaced.

- Patch and Delete methods are rewritten instead of being called directly from the base class, as the response object required data otherwise hidden in the standard implementation (Like the previous name of the book). It is possible to use the standard methods and derive this data separately, but that would account to 2 database calls. Hence to optimize the number of database queries, methods are remodelled.

- The local database choice is the default sqlite for the sake of simplicity in configuration in this minor use case. Since it does not support a list of strings to be stored, a custom `StringArrayField` Serializer was developed.

- Strings were assumed to have a maximum length of 200, for the sake of database configuration.

- Overridden CORS policy to allow all hosts to enable testing from any frontend.

- `DEBUG` is set to `TRUE` to debug issues while performance testing and evaluating through any frontend, which enables returning detailed server error reports and tracebacks as HTML string when requests are made.