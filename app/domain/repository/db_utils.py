from sqlalchemy import inspect

class DBUtils():
    @staticmethod
    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}        

    @staticmethod
    def get_paginator_dict():
        return {
            "limit": None,
            "next": None,
            "offset": 0,
            "previous": None,
            "total_count": None
        }

    @staticmethod
    def get_pagination(limit, paginator, page):
        current_page = paginator.page(page)
        count = current_page.paginator.count
        total_pages = current_page.paginator.total_pages
        previous = None
        next_value = None
        if current_page.has_next():
            next_value = current_page.next_page_number
        if current_page.has_previous():
            previous = current_page.previous_page_number
        meta_dict = DBUtils.get_paginator_dict()
        meta_dict['limit'] = limit
        meta_dict['next'] = next_value
        meta_dict['previous'] = previous
        meta_dict['total_count'] = count
        meta_dict['total_pages'] = total_pages

        return meta_dict
