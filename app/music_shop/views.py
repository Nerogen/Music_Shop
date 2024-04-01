import json

from django.shortcuts import render


def main_page(request):
    return render(request=request, template_name="music_shop/index.html")


def catalog_page(request):
    color = request.GET.get('color')
    neck = request.GET.get('neck')
    body = request.GET.get('body')
    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')

    with open(f"music_shop/data/data.json") as file:
         context = json.load(file)

    result = {"data": {}}

    expr_trus = [color, neck, body, min_price, max_price]

    if expr_trus == ['' for _ in range(5)]:
        return render(request=request, template_name="music_shop/catalog.html", context=context)

    for key, item in context.items():
        for k, v in item.items():
            box = []

            if color and v.get("info").get("Colour") and color in v.get("info").get("Colour"):
                box.append(color)
            else:
                box.append('')

            if neck and v.get("info").get("Neck profile") and neck in v.get("info").get("Neck profile"):
                box.append(neck)
            else:
                box.append('')

            if body and v.get("info").get("Body") and body in v.get("info").get("Body"):
                box.append(body)
            else:
                box.append('')

            if min_price and max_price and int(min_price) <= int(v.get("cost").replace(",", "")) <= int(max_price):
                box.extend([min_price, max_price])
            else:
                box.extend(['', ''])

            print(expr_trus, box)

            if expr_trus == box:
                result[key][k] = v

    print("Done")

    return render(request=request, template_name="music_shop/catalog.html", context=result)
