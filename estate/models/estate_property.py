from odoo import models, fields

# this is creating a table
class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    # this is creating fields in the table
    name = fields.Char(default="House", required=True)
    price = fields.Float()
