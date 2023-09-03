def create_and_update_form(request, form_class, session_key):

    form = form_class()
    form_data = request.session.get(session_key)

    if form_data:
        form = form_class(form_data)

    return form
