from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Asset
from .forms import AssetForm


def index(request):
    if request.method == 'GET':
        id = request.GET.get('id', '')
        if id:
            Asset.objects.get(pk=id).delete()
            return HttpResponse("ok")

    form = AssetForm(request.POST or None)

    if form.is_valid():
        asset = form.save(commit=False)
        asset.host_group = request.POST.get('host_group', '')
        asset.internal_ip = request.POST.get('internal_ip')
        asset.external_ip = request.POST.get('external_ip', '')
        asset.host_memory = request.POST.get('host_memory')
        asset.host_cpu = request.POST.get('host_cpu')
        asset.save()
    asset_list = Asset.objects.all()
    context = {'form': form, 'asset_list': asset_list, 'current_user': request.user}
    return render(request, 'asset/index.html', context)


def update(request):
    if request.method == 'POST':
        host_name = request.POST.get('host_name')
        asset = Asset.objects.get(host_name=host_name)
        asset.host_group = request.POST.get('host_group', '')
        asset.internal_ip = request.POST.get('internal_ip')
        if request.POST.get('external_ip', '') == str('None'):
            asset.external_ip = ''
        else:
            asset.external_ip = request.POST.get('external_ip')
        asset.host_memory = request.POST.get('host_memory')
        asset.host_cpu = request.POST.get('host_cpu')

        asset.save()
    return redirect('asset:index')
