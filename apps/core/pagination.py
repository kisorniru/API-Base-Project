def pagination_payload(items, *, page, per_page, total):
    return {
        'items': items,
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'has_next': page * per_page < total,
        },
    }
