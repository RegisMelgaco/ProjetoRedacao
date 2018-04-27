from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	list_display = ('email',)
	list_filter = ('groups',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('primeiro_nome', 'segundo_nome','red_pontos', 'genero', 'nascimento', 'ingresso_ensino_medio', 'cep')}),
		('Permissions', {'fields': ('admin',)}),
		('Groups', {'fields': ('groups',)})
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()


admin.site.register(User, UserAdmin)