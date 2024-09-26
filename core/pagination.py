from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumber(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        return Response(
            {
                "total_items": count,
                "total_pages": self.page.paginator.num_pages,
                "prev": bool(self.get_previous_link()),
                "next": bool(self.get_next_link()),
                "results": data,
            })
