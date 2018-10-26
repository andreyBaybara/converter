from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
import conv


def converter(request):
    """Render main page."""
    return render(request, 'base.html')


@require_http_methods(["POST"])
def convert_value(request):
    """Convert and return json response."""
    res = conv.convert(request)
    return HttpResponse(json.dumps({
                                    "result": res
                                    }), content_type="application/json")
