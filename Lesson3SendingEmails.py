#!/usr/bin/env python

import email_helper
recipient = 'blaforest@oit.umass.edu'
subject = 'Test message'
message = '''
This is a fictional test message.

Regards,

Briand
'''
sender = 'blaforest@oit.umass.edu'
 
email_helper.send_mail(recipient, subject, message, sender)
