from website.models import btn_content, btn_cta, btn_navbar, content_footer, content_mountain, content_offer, content_tool, desc_content, desc_mountain, desc_offer, desc_tool, logo_navbar, title_cta
from django.shortcuts import render

# Create your views here.


def base(request):
    logo_navbars = logo_navbar.objects.all()
    btn_navbars = btn_navbar.objects.all()
    desc_contents = desc_content.objects.all()
    btn_contents = btn_content.objects.all()
    desc_offers = desc_offer.objects.all()
    content_offers = content_offer.objects.all()
    desc_mountains = desc_mountain.objects.all()
    content_mountains = content_mountain.objects.all()
    desc_tools = desc_tool.objects.all()
    content_tools = content_tool.objects.all()
    title_ctas = title_cta.objects.all()
    btn_ctas = btn_cta.objects.all()
    content_footers = content_footer.objects.all()
    context = {'logo_navbars': logo_navbars,
               'btn_navbars': btn_navbars,
               'desc_contents': desc_contents,
               'btn_contents': btn_contents,
               'desc_offers': desc_offers,
               'content_offers': content_offers,
               'desc_mountains': desc_mountains,
               'content_mountains': content_mountains,
               'desc_tools': desc_tools,
               'content_tools': content_tools,
               'title_ctas': title_ctas,
               'btn_ctas': btn_ctas,
               'content_footers': content_footers,
               }
    return render(request, 'website/base.html', context)


def logo_navbars(request):
    logo_navbars = logo_navbar.objects.all()
    context = {'logo_navbars': logo_navbars}
    return render(request, 'website/navbar/logo_navbar.html', context)


def btn_navbars(request):
    btn_navbars = btn_navbar.objects.all()
    context = {'btn_navbars': btn_navbars}
    return render(request, 'website/navbar/btn_navbar.html', context)


def desc_contents(request):
    desc_contents = desc_content.objects.all()
    context = {'desc_contents': desc_contents}
    return render(request, 'website/content/desc_content.html', context)


def btn_contents(request):
    btn_contents = btn_content.objects.all()
    context = {'btn_contents': btn_contents}
    return render(request, 'website/content/btn_contents.html', context)


def desc_offers(request):
    desc_offers = desc_offer.objects.all()
    context = {'desc_offers': desc_offers}
    return render(request, 'website/offer/desc_offer.html', context)


def content_offers(request):
    content_offers = content_offer.objects.all()
    context = {'content_offers': content_offers}
    return render(request, 'website/offer/content_offer.html', context)


def desc_mountains(request):
    desc_mountains = desc_mountain.objects.all()
    context = {'desc_mountains': desc_mountains}
    return render(request, 'website/mountain/desc_mountain.html', context)


def content_mountains(request):
    content_mountains = content_mountain.objects.all()
    context = {'content_mountains': content_mountains}
    return render(request, 'website/mountain/content_mountain.html', context)


def desc_tools(request):
    desc_tools = desc_tool.objects.all()
    context = {'desc_tools': desc_tools}
    return render(request, 'website/tool/desc_tool.html', context)


def content_tools(request):
    content_tools = content_tool.objects.all()
    context = {'content_tools': content_tools}
    return render(request, 'website/tool/content_tool.html', context)


def title_ctas(request):
    title_ctas = title_cta.objects.all()
    context = {'title_ctas': title_ctas}
    return render(request, 'website/cta/title_cta.html', context)


def btn_ctas(request):
    btn_ctas = btn_cta.objects.all()
    context = {'btn_ctas': btn_ctas}
    return render(request, 'website/cta/btn_cta.html', context)


def content_footers(request):
    content_footers = content_footer.objects.all()
    context = {'content_footers': content_footers}
    return render(request, 'website/footer/content_footers.html', context)
