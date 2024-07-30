from odoo import models, fields

class ArtPiece(models.Model):
    _name = 'art.piece'
    _description = 'Art Piece'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    author = fields.Char(string='Author')
    image = fields.Binary(string='Image')  # Campo binario para almacenar la imagen
    audio_url = fields.Char(string='Audio URL')
    price = fields.Float(string='Price')
