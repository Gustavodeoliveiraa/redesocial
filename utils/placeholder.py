def add_class_field(field, attr_name, attr_new_val):
    exist = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{exist} {attr_new_val}'.strip()
