# from odoo import fields, models

# class ModuleReport(models.Model):

#     _name = 'invoice.summary'
#     _description = "Invoice Summary"
#     _rec_name = 'account_id'
#     _auto = False

#     account_id = fields.Many2one('account.account')
#     partner_id = fields.Many2one('res.partner')
#     acct_type = fields.Char(string = "Account Type")
#     partner_city = fields.Char(string = "City")
#     partner_country_code = fields.Char()

#     @property
#     def _table_query(self):
#         query = 'SELECT %s FROM %s' % (self._select(), self._from())
#         print(query)
#         return query

#     def _select(self):
#         _select = """
#             MIN(line.id) as id,
#             line.account_id,
#             line.partner_id,
#             acc.account_type as acct_type,
#             rsprtnr.city as partner_city,
#             rscntry.code as partner_country_code
#         """

#         return _select

#     def _from(self):
#         _from = """
#             account_move_line line
#             LEFT JOIN account_account acc ON line.account_id = acc.id
#             LEFT JOIN res_partner rsprtnr ON line.partner_id = rsprtnr.id
#             LEFT JOIN res_country rscntry ON rsprtnr.country_id = rscntry.id
#         """

#         return _from