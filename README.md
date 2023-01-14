This script will forward all alerts from a kismet server to a discord webhook url. It is up to you to configure kismet alerts on the server as desired. This does not differentiate between alert types. If you would like to add that a pr is welcome but I probably won't get that far

To get the required pip packages you can run:
pip3 install -r requirements.txt

Then just replace the 3 variables in the script with you kismet api key, discord webhook, and hostname or ip of the kismet server. To run just do:
python3 kimset_alert_forwarder.py

