## Quickstart
For installing, just run this command in your shell
```python
pip install -r requirements.txt
```
### Settings
Add the following lines to settings.py
```python
INSTALLED_APPS = (
    # ...
    'django.contrib.staticfiles', # Required for GraphiQL
    'graphene_django',
)

GRAPHENE = {
    'SCHEMA': 'app.schema.schema' # Where your Graphene schema lives
}
```
### Urls
We need to set up a `GraphQL` endpoint in our Django app, so we can serve the queries.
```python
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
```
### Development server 
To run the server, just run this command in your shell
```python
python manage.py runserver
```






