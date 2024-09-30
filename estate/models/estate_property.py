from odoo import models, fields

# this is creating a table
class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    # this is creating fields in the table
    name = fields.Char(default="House", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.add(value=fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=3)
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
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required=True, copy= False, default='new', string='Property Status',
        selection=[('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="Reflects the current status in the sales process"
        )
