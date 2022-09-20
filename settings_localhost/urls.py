from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    # path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.login.urls')),
    path('', include('apps.widget.urls')),
    path('', include('apps.contact_mgmt.urls')),
    path('', include('apps.sales.urls')),
    path('', include('apps.marketing.urls')),
    path('', include('apps.customer_service.urls')),
    path('', include('apps.project_mgmt_advance.urls')),
    path('', include('apps.project_mgmt_basic.urls')),
    path('', include('apps.global_settings.urls')),
    path('', include('apps.hrms.urls')),
    path('', include('apps.document.urls')),
    path('', include('apps.training.urls')),
    path('', include('apps.assets.urls')),
    path('', include('apps.feedback.urls')),
    path('', include('apps.vendor_management.urls')),
    path('', include('apps.inventory_management.urls')),
    path('', include('apps.market_research.urls')),
    path('', include('apps.compliance.urls')),
    path('', include('apps.accounting.urls')),
    path('', include('apps.organization.urls')),
    path('', include('apps.report_slick.urls')),
    path('', include('apps.analytics.urls')),
    path('', include('apps.settings.urls')),
    path('', include('apps.ticket.urls')),
    path('', include('apps.product.urls')),
    path('', include('apps.report.urls')),
    path('', include('apps.license_management.urls')),
    path('', include('apps.idea.urls')),
    path('', include('apps.notification.urls')),

    # community
    path('community/', include('community.apps.chat.urls')),
    path('community/', include('community.apps.company.urls')),
    path('community/', include('community.apps.company_settings.urls')),
    path('community/', include('community.apps.feedback.urls')),
    path('community/', include('community.apps.groups.urls')),
    path('community/', include('community.apps.invitation.urls')),
    path('community/', include('community.apps.job.urls')),
    path('community/', include('community.apps.my_profile.urls')),
    path('community/', include('community.apps.page.urls')),
    path('community/', include('community.apps.ticket.urls')),
    path('community/', include('community.apps.user_settings.urls')),

    # job portal
    path('job_portal/', include('job_portal.apps.applicant.urls')),
    path('job_portal/', include('job_portal.apps.job_description.urls')),
    path('job_portal/', include('job_portal.apps.feedback.urls')),
    path('job_portal/', include('job_portal.apps.ticket.urls')),
    # path('accounts/', include('allauth.urls')),
    path('job_portal/logout', LogoutView.as_view()),

    # license portal
    path('license_portal', include('license_portal.apps.license_management.urls',('license_portal.apps.license_management'))),

    # customer portal
    path('customer_portal/', include('customer_portal.apps.login.urls')),
    path('customer_portal/', include('customer_portal.apps.ticket.urls')),
    path('customer_portal/', include('customer_portal.apps.accounting.urls')),
    # path('customer_portal/', include('customer_portal.apps.bms_geo_location.urls')),

    # vendor portal
    # path('vendor_portal/', include('vendor_portal.apps.bms_geo_location.urls')),
    path('vendor_portal/', include('vendor_portal.apps.feedback.urls')),
    path('vendor_portal/', include('vendor_portal.apps.inventory_management.urls')),
    path('vendor_portal/', include('vendor_portal.apps.report_slick.urls')),
    # path('vendor_portal/', include('vendor_portal.apps.select_settings.urls')),
    path('vendor_portal/', include('vendor_portal.apps.settings.urls',('vendor_portal.apps.settings'))),
    path('vendor_portal/', include('vendor_portal.apps.ticket.urls')),
    path('vendor_portal/', include('vendor_portal.apps.vendor_login.urls')),
    path('vendor_portal/', include('vendor_portal.apps.widget.urls',('vendor_portal.apps.widget'))),

    # sperentes admin
    path('sperentes_admin/', include('sperentes_admin.apps.bms.urls')),
    path('sperentes_admin/', include('sperentes_admin.apps.product.urls')),
    path('sperentes_admin/', include('sperentes_admin.apps.login.urls')),
    # path('sperentes_admin/', include('sperentes_admin.apps.sperentes_admin_log.urls')),

    # vc
    path('video_conferenc/', include('video_conference.apps.video_call.urls')),

    # sperentes bms
    path('bms_sperentes/', include('bms_sperentes.apps1.login.urls',('bms_sperentes.apps1.login'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.widget.urls',('bms_sperentes.apps1.widget'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.contact_mgmt.urls',('bms_sperentes.apps1.contact_mgmt'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.sales.urls',('bms_sperentes.apps1.sales'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.marketing.urls',('bms_sperentes.apps1.marketing'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.customer_service.urls',('bms_sperentes.apps1.customer_service'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.project_mgmt_advance.urls',('bms_sperentes.apps1.project_mgmt_advance'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.project_mgmt_basic.urls',('bms_sperentes.apps1.project_mgmt_basic'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.global_settings.urls',('bms_sperentes.apps1.global_settings'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.hrms.urls',('bms_sperentes.apps1.hrms'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.document.urls',('bms_sperentes.apps1.document'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.training.urls',('bms_sperentes.apps1.training'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.assets.urls',('bms_sperentes.apps1.assets'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.feedback_internal.urls',('bms_sperentes.apps1.feedback_internal'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.vendor_management.urls',('bms_sperentes.apps1.vendor_management'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.inventory_management.urls',('bms_sperentes.apps1.inventory_management'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.market_research.urls',('bms_sperentes.apps1.market_research'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.compliance.urls',('bms_sperentes.apps1.compliance'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.accounting.urls',('bms_sperentes.apps1.accounting'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.organization.urls',('bms_sperentes.apps1.organization'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.report_slick.urls',('bms_sperentes.apps1.report_slick'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.analytics.urls',('bms_sperentes.apps1.analytics'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.settings.urls',('bms_sperentes.apps1.settings'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.ticket_incoming.urls',('bms_sperentes.apps1.ticket_incoming'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.product.urls',)),
    path('bms_sperentes/', include('bms_sperentes.apps1.ticket.urls')),
    path('bms_sperentes/', include('bms_sperentes.apps1.report.urls',('bms_sperentes.apps1.report'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.license_management.urls',('bms_sperentes.apps1.license_management'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.idea.urls',('bms_sperentes.apps1.idea'))),
    path('bms_sperentes/', include('bms_sperentes.apps1.bug_tracker.urls')),
    path('bms_sperentes/', include('bms_sperentes.apps1.feedback_incoming.urls'))
]
# +static(settings_prod.MEDIA_URL, document_root=settings_prod.MEDIA_ROOT)
