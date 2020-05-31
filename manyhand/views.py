from django.shortcuts import render
from asset.models import Asset


def index(request):
    asset_list = Asset.objects.all()
    context = {'asset_list': asset_list}
    if request.method == 'POST':
        host_name = request.POST.get('host_name', '')
        host_group = request.POST.get('host_group', '')
        command = request.POST.get('command', '')
        playbook = request.POST.get('playbook', '')
        print(host_name, host_group, command, playbook)
    return render(request, 'manyhand/index.html', context)

