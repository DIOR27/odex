from odoo import fields, _
from odoo.exceptions import ValidationError
import re

# Guardar las implementaciones originales de los métodos __init__ y convert_to_cache
_original_char_init = fields.Char.__init__
_original_text_init = fields.Text.__init__


# Personalizar la inicialización del campo Char para aceptar un parámetro de regex
def custom_char_init(self, string=None, regex=None, **kwargs):
    if string is None:
        string = ""
    _original_char_init(self, string=string, **kwargs)
    self.regex = regex


# Personalizar la inicialización del campo Text para aceptar un parámetro de regex
def custom_text_init(self, string=None, regex=None, **kwargs):
    if string is None:
        string = ""
    _original_text_init(self, string=string, **kwargs)
    self.regex = regex


# Validar el valor del campo Char con el regex proporcionado
def custom_char_convert_to_cache(self, value, record, validate=True):
    if value and hasattr(self, "regex") and self.regex:
        if not re.match(self.regex.strip(), value):
            raise ValidationError(_("El valor '%s' no es válido" % value))
    return super(fields.Char, self).convert_to_cache(value, record, validate=validate)


# Validar el valor del campo Text con el regex proporcionado
def custom_text_convert_to_cache(self, value, record, validate=True):
    if value and hasattr(self, "regex") and self.regex:
        if not re.match(self.regex.strip(), value):
            raise ValidationError(_("El valor '%s' no es válido" % value))
    return super(fields.Text, self).convert_to_cache(value, record, validate=validate)


# Sobrescribir los métodos originales de Char y Text
fields.Char.__init__ = custom_char_init
fields.Char.convert_to_cache = custom_char_convert_to_cache

fields.Text.__init__ = custom_text_init
fields.Text.convert_to_cache = custom_text_convert_to_cache
