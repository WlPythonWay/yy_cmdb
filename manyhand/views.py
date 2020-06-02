import os
import json
from django.shortcuts import render
from asset.models import Asset
from .ansible_api import AnsibleApi
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    asset_list = Asset.objects.all()
    context = {'asset_list': asset_list}
    if request.method == 'POST':
        asb = AnsibleApi()
        host_name = request.POST.get('host_name', '')
        host_group = request.POST.get('host_group', '')
        command = request.POST.get('command', '')
        playbook = request.POST.get('playbook', '')
        if not host_name and not host_group:
            context['error_messages'] = '主机或主机组必填一个'
            return render(request, 'manyhand/index.html', context)
        if not command and not playbook:
            context['error_messages'] = '命令或剧本必填一个'
            return render(request, 'manyhand/index.html', context)
        if host_name:
            host_list = [host_name]
        else:
            host_list = [host_group]

        if command:
            tasks_list = [
                dict(action=dict(module='shell', args=command)),
            ]
            response = asb.runansible(host_list, tasks_list)
        else:
            playbook_path = os.path.join('/etc/ansible/', playbook+'.yml')
            response = asb.playbookrun(playbook_path=[playbook_path])
        result = []
        if response['failed']:
            for host, info in response['failed'].items():
                data_obj = {}
                data_obj['host'] = host
                data_obj['stdout'] = info
                result.append(data_obj)
        elif response['unreachable']:
            for host, info in response['unreachable'].items():
                data_obj = {}
                data_obj['host'] = host
                data_obj['stdout'] = info
                result.append(data_obj)
        elif response['success']:
            for host, info in response['success'].items():
                data_obj = {}
                info = json.loads(info)
                data_obj['host'] = host
                data_obj['stdout'] = info['stdout']
                data_obj['cmd'] = info['cmd']
                data_obj['delta'] = info['delta']
                result.append(data_obj)

        context['result'] = result
        
    return render(request, 'manyhand/index.html', context)

