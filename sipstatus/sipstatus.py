from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
from django.template import loader, Context
from django.db.models import Count
from server.models import *

class SIPStatus(IPlugin):
    def show_widget(self, page, machines=None, theid=None):

        if page == 'front':
            t = loader.get_template('chasetb/sipstatus/templates/front.html')

        if page == 'bu_dashboard':
            t = loader.get_template('chasetb/sipstatus/templates/id.html')

        if page == 'group_dashboard':
            t = loader.get_template('chasetb/sipstatus/templates/id.html')


        disabled = machines.filter(facts__fact_name='mac_sip_status', facts__fact_data='disabled').count()

        if disabled:
            size = 4
        else:
            size = 0

        c = Context({
            'title': 'SIP Status',
            'disabled_count': disabled,
            'page': page,
            'theid': theid
        })
        return t.render(c), size

    def filter_machines(self, machines, data):
        if data == 'disabled':
            machines = machines.filter(facts__fact_name='mac_sip_enabled', facts__fact_data='disabled').count()
            title = 'Macs with System Integrity Protection disabled'
        else:
            machines = None
            title = None

        return machines, title

