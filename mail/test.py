# -*- coding: utf-8 -*-
'''
Created on Mar 18, 2016

@author: fky
'''

import smtplib
if not 'SMTP_SSL' in smtplib.__all__:
    print('''error: Server does not support SMTP-over-SSL. You could use STARTTLS instead. If SSL is needed, an upgrade to Python 2.6 on the server-side should do the trick.''')
print(smtplib.__all__)
