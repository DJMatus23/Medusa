# coding=utf-8

from __future__ import unicode_literals

import datetime

from medusa import app, network_timezones
from medusa.server.web.core.base import PageTemplate, WebRoot
from medusa.system.schedulers import generate_schedulers

from tornroutes import route


@route('/healthz(/?.*)')
class Healthz(WebRoot):
    def __init__(self, *args, **kwargs):
        super(WebRoot, self).__init__(*args, **kwargs)

    def index(self):
        response = 'Schedules no beuno:\n'

        for gen in generate_schedulers():
            if not gen['isAlive']:
                response += gen['name'] + '\n'
                self.set_status(500)

        self.finish(response)