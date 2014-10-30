# Create your views here.


from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {})


def form_styles(request):
    return render_to_response('form_styles.html', {})


def form_components(request):
    return render_to_response('form_components.html', {})


def validations(request):
    return render_to_response('validations.html', {})


def widgets(request):
    return render_to_response('widgets.html', {})


def ui_elements(request):
    return render_to_response('ui_elements.html', {})


def buttons_and_icons(request):
    return render_to_response('buttons_and_icons.html', {})


def charts(request):
    return render_to_response('charts.html', {})


def address_book(request):
    return render_to_response('address_book.html', {})


def chats(request):
    return render_to_response('chats.html', {})


def inplace_editing(request):
    return render_to_response('inplace_editing.html', {})


def filetrees(request):
    return render_to_response('filetrees.html', {})


def fileupload(request):
    return render_to_response('fileupload.html', {})


def todo(request):
    return render_to_response('todo.html', {})


def wysiwyg(request):
    return render_to_response('wysiwyg.html', {})


def tables(request):
    return render_to_response('tables.html', {})


def grid(request):
    return render_to_response('grid.html', {})


def type(request):
    return render_to_response('type.html', {})


def calendar(request):
    return render_to_response('calendar.html', {})


def invoice(request):
    return render_to_response('invoice.html', {})


def gallery(request):
    return render_to_response('gallery.html', {})


def timeline(request):
    return render_to_response('timeline.html', {})


def wizard(request):
    return render_to_response('wizard.html', {})


def pricing_tables(request):
    return render_to_response('pricing_tables.html', {})


def user_profile(request):
    return render_to_response('user_profile.html', {})


def sign_in(request):
    return render_to_response('sign_in.html', {})


def faq(request):
    return render_to_response('faq.html', {})


def orders(request):
    return render_to_response('orders.html', {})


def search_results(request):
    return render_to_response('search_results.html', {})


def blank(request):
    return render_to_response('blank.html', {})


def closed_navigation(request):
    return render_to_response('closed_navigation.html', {})


def fixed_header(request):
    return render_to_response('fixed_header.html', {})


def fixed_navigation(request):
    return render_to_response('fixed_navigation.html', {})


def fixed_navigation_and_header(request):
    return render_to_response('fixed_navigation_and_header.html', {})


def email_templates(request):
    return render_to_response('email_templates.html', {})


def wizard(request):
    return render_to_response('wizard.html', {})


def base(request):
    return render_to_response('base.html', {})


def dashboard(request):
    return render_to_response('dashboard.html', {})


def page_not_found(request):
    return render_to_response('err404.html', {})


def page_error(request):
    return render_to_response('err500.html', {})
