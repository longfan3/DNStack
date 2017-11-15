#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio
# Index Page

from BaseHandler import BaseHandler

class Page404Handler(BaseHandler):
    # @Auth
    def get(self):
        self.render('page/404.html')

class Page500Handler(BaseHandler):
    # @Auth
    def get(self):
        self.render('page/500.html')

class PageErrorHandler(BaseHandler):
    def get(self):
        self.render('page/error.html')