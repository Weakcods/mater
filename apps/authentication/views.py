from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper


class CustomLoginView(LoginView):
    template_name = 'auth_login_basic.html'

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to auth/urls.py file for more pages.
"""


class AuthView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                'layout_path': TemplateHelper.set_layout("layouts/blank.html"),
            }
        )

        return context
