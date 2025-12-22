from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy


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
    

class AuthRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login_user')

    def handle_no_permission(self):
        messages.error(self.request, self.not_auth_message)
        return super().handle_no_permission()


class OwnerAccessMixin(AuthRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().handle_no_permission()
        if request.user.id != kwargs.get('pk'):
            messages.error(request, self.another_user_message)
            return redirect(self.app_index_url)
        return super().dispatch(request, args, kwargs)

        


    


