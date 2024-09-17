from odoo import fields, _
from odoo.exceptions import ValidationError
import re

_original_char_init = fields.Char.__init__


def custom_char_init(self, string=None, regex=None, **kwargs):
    if string is None:
        string = ""
    _original_char_init(self, string=string, **kwargs)
    self.regex = regex


def custom_char_convert_to_cache(self, value, record, validate=True):
    if value and hasattr(self, "regex") and self.regex:
        if not re.match(self.regex, value):
            raise ValidationError(_(""The value '%s' does not match the required pattern: %s"" % value))
    return super(fields.Char, self).convert_to_cache(value, record, validate=validate)


fields.Char.__init__ = custom_char_init
fields.Char.convert_to_cache = custom_char_convert_to_cache
