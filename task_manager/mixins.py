from django.contrib import messages
from django.shortcuts import redirect


class FormValidMixin:

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class FormContextMixin:
    h1 = None
    submit_button = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = self.h1
        context['submit_button'] = self.submit_button
        if getattr(self, 'get_delete_warning', None):
            context['delete_warning'] = self.get_delete_warning()
        return context


class PermissionMixin:
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.not_auth_message)
            return redirect('login_user')
        updating_user = self.model.objects.get(id=kwargs.get('pk'))
        if request.user.id != updating_user.id:
            messages.error(request, self.another_user_message)
            return redirect('index_users')
        return super().get(request, args, kwargs)
