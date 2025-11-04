#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8400419495:AAHPVhXaN4uKeiCGjvNGhic5S1SZWdH2YFc")
    API_ID = int(os.environ.get("API_ID", "29978901"))
    API_HASH = os.environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5776977809")
