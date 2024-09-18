  Odex - RegEx for Char Fields

Odex - The Odoo RegEx Module
============================

#### Odex is a simple but powerful module for managing regular expressions in fields.

This Odoo module customizes the behavior of the `Char` field by introducing a new `regex` parameter. It allows you to define a regular expression pattern that the field value must match. If the value provided does not conform to the specified pattern, a `ValidationError` is raised.

### Usage

To use odex, simply add the parameter `regex` together with the string to be evaluated in the char field (`fields.Char`) of your model, for example:  
  
`name = fields.Char(string=_(“Name”), regex=r"^[A-Z0-9]+$")`  
  
When not matching the regular expression, the system will display a `ValidationError` indicating the value and the expected expression.

**Note:** The `regex` parameter is case-sensitive.

If you like my work please leave me a star on GitHub, I'd really appreciate it.
