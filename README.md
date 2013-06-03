chronos_backup
==============

Backs up AirBNB Chronos jobs and can restore them.

Requires:
  requests
  python >2.7
  
optional arguments:
  -h, --help            show this help message and exit
  -b BACKUP, --backup BACKUP
                        Specifies whether to backup the Chronos jobs and where
                        in the format chronosbackups/ and the folder must
                        already exist.
  -r RESTORE, --restore RESTORE
                        Specifies whether to restore from a json file to the
                        Chronos server.
  -u URL, --url URL     Specify URL for Chronos in the format
                        http://chronos:4400

Examples:
To restore
python response.py -u http://chronos.vimeo.com:4400 -r chronosbackupstest/2013-06-03\ 16:52:08.304948.json

To backup
python response.py -u http://chronos.vimeo.com:4400 -b chronosbackupstest/
