from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.shortcuts import redirect, HttpResponseRedirect
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BaseAuthentication
from .models import User

# def logout_page(request):
#     print("loggedout")
#     logout(request)
#     return HttpResponseRedirect('/')

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        form.save()
    return render(request, "accounts/register.html", context)

#authenticate user
# def login_page(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data['username']
# #         password = form.cleaned_data['full_name']
#         user = authenticate(username = username, password = password)
#         login(request, user)
#         print('logged in')
#
#     context = {
#         "form" : form
#     }
#     return render(request, "accounts/login.html", context)


#takes user's username and password and creates a token with user information
#corresponding to the passed credentials as payload and returns it to the browser
# class Login(APIView):
#     def post(self, request, *args, **kwargs):
#         if not request.data:
#             return Response({'Error': "Please provide email/password"}, status="400")
#         email = request.data['email']
#         password = request.data['password']
#         try:
#             user = User.objects.get(email = email, password = password)
#         except User.DoesNotExist:
#             return Response({'Error': "Invalid email/password"}, status="400")
#         if user:
#             payload = jwt_payload_handler(user)
#             token = jwt.encode(payload, settings.SECRET_KEY)
#             user_details = {}
#             user_details['name'] = "%s" % (
#             user.full_name)
#             user_details['token'] = token
#             user_logged_in.send(sender=user.__class__,
#                                request=request, user=user)
#             return Response(user_details, status=status.HTTP_200_OK)
#         else:
#             return Response(
#              json.dumps({'Error': "Invalid credentials"}),
#              status=400,
#              content_type="application/json")
#
# #server will validate the token and allow the browser to access API protected with authentication class
# #based on validation results
# class TokenAuthentication(BaseAuthentication):
#     model = None
#
#     def get_model(self):
#         return User
#
#     def authenticate(self, request):
#         auth = get_authorization_header(request).split()
#         if not auth or auth[0].lower() != b'token':
#             return None
#         if len(auth) == 1:
#             msg = 'Invalid token header. No credentials provided.'
#             raise exceptions.AuthenticationFailed(msg)
#         elif len(auth) > 2:
#             msg = 'Invalid token header'
#             raise exceptions.AuthenticationFailed(msg)
#         try:
#             token = auth[1]
#             if token == "null":
#                 msg = "Null token not allowed"
#                 raise exceptions.AuthenticationFailed(msg)
#         except UnicodeError:
#             msg ='Invalid token header. Token string should not contain invalid characters.'
#             raise exceptions.AuthenticationFailed(msg)
#         return self.authenticate_credentials(token)
#
#     def authenticate_credentials(self, token):
#         model = self.get_model()
#         payload = jwt.decode(token, "SECRET_KEY")
#         email = payload['email']
#         userid = payload['id']
#         msg = {'Error': "Token mismatch", 'status': "401"}
#         try:
#             user = User.objects.get(
#                 email=email,
#                 id=userid,
#                 is_active=True
#             )
#             if not user.token['token'] == token:
#                 raise exceptions.AuthenticationFailed(msg)
#         except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
#             return HttpResponse({'Error': "Token is invalid"}, status="403")
#         except User.DoesNotExist:
#             return HttpResponse({'Error': "Internal server error"}, status="500")
#         return (user, token)
#
#     def authenticate_header(self, request):
#         return 'Token'

