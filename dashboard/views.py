# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

# Create your views here.
class Board(View):
    board_template = 'dashboard/board.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.board_template, {})
