from odoo import models, fields

# this is creating a table
class RealEstate(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    # this is creating fields in the table
    price = fields.Float(copy=False, required=True)
    status = fields.Selection(
        default="received", required=True,
        selection=[('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('refused', 'Refused')],
        )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)

