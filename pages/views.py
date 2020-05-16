from django.shortcuts import render

# def home_view(request, *args, **kwargs):
#     return render(request, "home.html", {})
#
# def contact_view(request, *args, **kwargs):
#     return render(request, "contact.html", {})
#
# def about_view(request, *args, **kwargs):
#     my_context = {
#         "my_text": "This is about us",
#         "this_is_true": True,
#         "my_number": 1234567890,
#         "my_list" : [1,2,3,"Abc"]
#     }
#     return render(request, "about.html", my_context)
#
# def social_view(request, *args, **kwargs):
#     return render(request, "social.html", {})
from django.views.generic.base import View

class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/front-end-render.html", {})


