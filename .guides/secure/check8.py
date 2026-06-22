#!/usr/bin/env python
import os, sys

text = os.environ['CODIO_FREE_TEXT_ANSWER']
sys.path.append('/usr/share/codio/assessments')
from lib.grade import send_grade_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT

points = 0
total = 2

# check for required key words
if 'Nevada' in text:
	points+=2
elif 'NV' in text:
	points+=2
else:
	print("❌ You did not specify the correct state. ")

if points==2:
	print("✅ Your answer has passed. ")
	exit(0)

exit(1)