from odoo import models, fields

# this is creating a table
class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Test model"

    # this is creating fields in the table
    name = fields.Char(default="House", required=True)
    price = fields.Float()
