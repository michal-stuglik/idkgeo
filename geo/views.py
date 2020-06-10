# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string

from geo.models import Point


def fix_json(s: str) -> str:
    """Fix template JSON"""

    sp = s.strip().split("\n")

    sp_non_empty = []
    sp_non_empty_fixed = []

    for idx in range(len(sp)):

        line = sp[idx].strip()
        if len(line.strip()) == 0:
            continue

        sp_non_empty.append(line)

    for idx in range(len(sp_non_empty)):

        line = sp_non_empty[idx].strip()

        if line.strip() == "}," and len(sp_non_empty) > idx:
            next_line = sp_non_empty[idx + 1]

            if next_line.strip() in ["}", "]"]:
                sp_non_empty_fixed.append(line.strip().strip(","))
                continue

        sp_non_empty_fixed.append(sp_non_empty[idx])

    return "\n".join(sp_non_empty_fixed)


def point(request):
    if request.method == 'GET':
        points = Point.objects.all()

        template_as_string = render_to_string(request=request, template_name='point.json', context={'points': points})
        return HttpResponse(fix_json(template_as_string), content_type='application/json')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
