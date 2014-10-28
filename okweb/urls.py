from django.conf import settings
from django.conf.urls import patterns, include, url
from flatty import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import okweb

admin.autodiscover()

handler404 = 'flatty.views.page_not_found'
handler500 = 'flatty.views.page_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okweb.views.home', name='home'),
    # url(r'^okweb/', include('okweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i/$', views.index),
    url(r'^i/index.html$', views.index),
    url(r'^i/form_styles.html$', views.form_styles),
    url(r'^i/form_components.html$', views.form_components),
    url(r'^i/validations.html$', views.validations),
    url(r'^i/widgets.html$', views.widgets),
    url(r'^i/ui_elements.html$', views.ui_elements),
    url(r'^i/buttons_and_icons.html$', views.buttons_and_icons),
    url(r'^i/charts.html$', views.charts),
    url(r'^i/address_book.html$', views.address_book),
    url(r'^i/chats.html$', views.chats),
    url(r'^i/inplace_editing.html$', views.inplace_editing),
    url(r'^i/filetrees.html$', views.filetrees),
    url(r'^i/fileupload.html$', views.fileupload),
    url(r'^i/todo.html$', views.todo),
    url(r'^i/wysiwyg.html$', views.wysiwyg),
    url(r'^i/tables.html$', views.tables),
    url(r'^i/grid.html$', views.grid),
    url(r'^i/type.html$', views.type),
    url(r'^i/calendar.html$', views.calendar),
    url(r'^i/invoice.html$', views.invoice),
    url(r'^i/gallery.html$', views.gallery),
    url(r'^i/timeline.html$', views.timeline),
    url(r'^i/pricing_tables.html$', views.pricing_tables),
    url(r'^i/user_profile.html$', views.user_profile),
    url(r'^i/sign_in.html$', views.sign_in),
    url(r'^i/faq.html$', views.faq),
    url(r'^i/orders.html$', views.orders),
    url(r'^i/search_results.html$', views.search_results),
    url(r'^i/blank.html$', views.blank),
    url(r'^i/closed_navigation.html$', views.closed_navigation),
    url(r'^i/fixed_header.html$', views.fixed_header),
    url(r'^i/fixed_navigation.html$', views.fixed_navigation),
    url(r'^i/fixed_navigation_and_header.html$', views.fixed_navigation_and_header),
    url(r'^i/email_templates.html$', views.email_templates),
    url(r'^i/wizard.html$', views.wizard),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
