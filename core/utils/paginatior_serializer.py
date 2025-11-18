from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = "limit"
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get("id_only"):
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(
            {
                "total_items": self.page.paginator.count,
                "page_size": self.page.paginator.per_page,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link(),
                "items": data,
            }
        )
