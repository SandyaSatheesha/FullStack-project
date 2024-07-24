from django.contrib import admin
from .models import Task

admin.site.register(Task)

# Debugging admin login
import logging
logger = logging.getLogger(__name__)

class CustomAdminSite(admin.AdminSite):
    def login(self, request, extra_context=None):
        logger.debug('Admin login attempt')
        response = super().login(request, extra_context)
        if request.user.is_authenticated:
            logger.debug('Admin login successful')
        else:
            logger.debug('Admin login failed')
        return response

admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Task)
