from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # class Meta:
    #     model = User

    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

