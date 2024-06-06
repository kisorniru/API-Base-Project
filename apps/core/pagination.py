def pagination_payload(items, *, page, per_page, total):
    return {
        'items': items,
        'meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': (total + per_page - 1) // per_page if per_page else 0,
            'total': total,
            'has_next': page * per_page < total,
        },
    }
