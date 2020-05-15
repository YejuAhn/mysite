# from pages.models import Menu
#
# from django import template
#
# register = template.Library()
#
# def build_menu(parser, token):
#     try:
#         tag_name, menu_name = token.split_contents()
#     except:
#         raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
#     return MenuObject(menu_name)
#
# class MenuObject(template.Node):
#     def __init__(self, menu_name):
#         self.menu_name = menu_name
#
#     def render(self, context):
#         current_path = template.resolve_variable('request.path', context)
#         user = template.resolve_variable('request.user', context)
#         context['menuitems'] = get_items(self.menu_name, current_path)
#
# def build_sub_menu(parser, token):
#
#
#
#
#
#
#
# def get_items(menu, current_path, user):
#     menuitems = []
#     for i in MenuItem.objects.filter(menu__slug=menu).order_by('order'):
#         current = (i.link_url != '/' and current_path.startswith(i.link_url == '/' and current_path == '/' ))
#
#
#
