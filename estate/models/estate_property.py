from odoo import models, fields

# this is creating a table
class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    # this is creating fields in the table
    name = fields.Char(default="House", required=True)
    description = fields.Text()
	postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
	selling_price = fields.Float()
	bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('n', 'North'), ('ne', 'Northeast'), ('e', 'East'), ('se', 'Southeast'), ('s', 'South'), 
        ('sw', 'Southwest'), ('w', 'West'), ('nw', 'Northwest')],
        help="Denotes which direction the garden is facing"
        )