#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    host_name = forms.CharField(
        label='主机名',
        widget=forms.TextInput(
            attrs={
                'placeholder': '主机名',
                'class': 'form-control'
            }
        )
    )
    # host_group = forms.ChoiceField(
    #     label='主机组',
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
    host_group = forms.CharField(
        label='主机组',
        widget=forms.TextInput(
            attrs={
                'placeholder': '主机组',
                'class': 'form-control'
            }
        )
    )
    internal_ip = forms.GenericIPAddressField(
        label='内网IP',
        widget=forms.TextInput(
            attrs={
                'placeholder': '内网IP',
                'class': 'form-control'
            }
        )
    )
    external_ip = forms.GenericIPAddressField(
        label='外网IP',
        widget=forms.TextInput(
            attrs={
                'placeholder': '外网IP',
                'class': 'form-control'
            }
        )
    )
    host_cpu = forms.IntegerField(
        label='CPU',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'CPU',
                'class': 'form-control'
            }
        )
    )
    host_memory = forms.IntegerField(
        label='内存',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '内存',
                'class': 'form-control',
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super(AssetForm, self).__init__(*args, **kwargs)
    #     print(Asset.objects.values_list('host_group'))
    #     self.fields['host_group'].choices = Asset.objects.values_list('id', 'host_group')

    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.fields['host_group'].required = False
        self.fields['external_ip'].required = False

    class Meta:
        model = Asset
        fields = "__all__"
        error_messages = {
            'host_name': {
                'required': '此处不能为空'
            },
            'internal_ip': {
                'required': '此处不能为空',
                'invalid': '请输入一个有效的IP地址'
            },
            'host_memory': {
                'required': '此处不能为空',
                'invalid': '请输入一个有效的数字'
            },
            'host_cpu': {
                'required': '此处不能为空',
                'invalid': '请输入一个有效的数字'
            },
            'external_ip': {
                'invalid': '请输入一个有效的IP地址'
            },
        }
