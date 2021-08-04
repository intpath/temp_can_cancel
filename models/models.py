# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class ResUser(models.Model):
    _inherit = 'res.users'

    can_cancel = fields.Boolean(string='Can Cancel Tickets?')



class CarRepairSupport(models.Model):
    _inherit = 'car.repair.support'

    can_cancel = fields.Boolean()