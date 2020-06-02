from django.test import TestCase
import json

result = {'success': {'lifang': '{"cmd": "df -h", "stdout": "Filesystem      Size  Used Avail Use% Mounted on\\ndevtmpfs        870M     0  870M   0% /dev\\ntmpfs           880M  136K  879M   1% /dev/shm\\ntmpfs           880M  508K  879M   1% /run\\ntmpfs           880M     0  880M   0% /sys/fs/cgroup\\n/dev/vda1        40G  4.7G   33G  13% /\\ntmpfs           176M     0  176M   0% /run/user/0", "stderr": "", "rc": 0, "start": "2020-06-01 18:10:45.422914", "end": "2020-06-01 18:10:45.425996", "delta": "0:00:00.003082", "changed": true, "invocation": {"module_args": {"_raw_params": "df -h", "_uses_shell": true, "warn": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}, "_ansible_parsed": true, "stdout_lines": ["Filesystem      Size  Used Avail Use% Mounted on", "devtmpfs        870M     0  870M   0% /dev", "tmpfs           880M  136K  879M   1% /dev/shm", "tmpfs           880M  508K  879M   1% /run", "tmpfs           880M     0  880M   0% /sys/fs/cgroup", "/dev/vda1        40G  4.7G   33G  13% /", "tmpfs           176M     0  176M   0% /run/user/0"], "stderr_lines": [], "_ansible_no_log": false}'}, 'failed': {}, 'unreachable': {}}


for k, v in result.items():
    if v:
        for host, info in v.items():
            print(info)
