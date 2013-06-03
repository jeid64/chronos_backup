chronos_backup
==============

Backs up AirBNB Chronos jobs and can restore them.

Requires:
---------
  requests

  python >2.7
  
Examples:
---------
python response.py -u http://chronos.vimeo.com:4400 -r chronosbackupstest/2013-06-03\ 16:52:08.304948.json

python response.py -u http://chronos.vimeo.com:4400 -b chronosbackupstest/
