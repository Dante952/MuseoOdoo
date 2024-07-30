from odoo import http
from odoo.http import request
import json
import base64

class ArtPieceController(http.Controller):

    @http.route('/api/art_pieces', auth='public', methods=['GET'], type='http', csrf=False)
    def get_art_pieces(self, **kwargs):
        art_pieces = request.env['art.piece'].sudo().search([])
        art_pieces_list = []
        for piece in art_pieces:
            art_pieces_list.append({
                'id': piece.id,
                'title': piece.title,
                'description': piece.description,
                'author': piece.author,
                'image': base64.b64encode(piece.image or b'').decode('utf-8'),
                'audio_url': piece.audio_url,
                'price': piece.price,
            })
        return request.make_response(
            json.dumps(art_pieces_list),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/art_pieces', auth='public', methods=['POST'], type='json', csrf=False)
    def create_art_piece(self, **kwargs):
        data = request.jsonrequest
        if 'image' in data:
            data['image'] = base64.b64decode(data['image'])
        new_piece = request.env['art.piece'].sudo().create(data)
        return json.dumps({'id': new_piece.id})

    @http.route('/api/art_pieces/<int:piece_id>', auth='public', methods=['PUT'], type='json', csrf=False)
    def update_art_piece(self, piece_id, **kwargs):
        data = request.jsonrequest
        if 'image' in data:
            data['image'] = base64.b64decode(data['image'])
        art_piece = request.env['art.piece'].sudo().browse(piece_id)
        if art_piece.exists():
            art_piece.sudo().write(data)
            return json.dumps({'status': 'success'})
        else:
            return json.dumps({'status': 'error', 'message': 'Art piece not found'})

    @http.route('/api/art_pieces/<int:piece_id>', auth='public', methods=['DELETE'], type='http', csrf=False)
    def delete_art_piece(self, piece_id, **kwargs):
        art_piece = request.env['art.piece'].sudo().browse(piece_id)
        if art_piece.exists():
            art_piece.sudo().unlink()
            return json.dumps({'status': 'success'})
        else:
            return json.dumps({'status': 'error', 'message': 'Art piece not found'})
