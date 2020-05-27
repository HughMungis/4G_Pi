apt install ppp minicom wvdial;
echo "[Dialer Defaults]
Init1 = AT+CFUN=1
Init2 = ATZ
Init3 = AT+CGDCONT=1,"IP","soracom.io"
Dial Attempts = 3
Stupid Mode = 1
Modem Type = Analog Modem
Modem = /dev/ttyS0
Dial Command = ATD
Stupid Mode = yes
Baud = 115200
New PPPD = yes
ISDN = 0
APN = soracom.io
Phone = *99***1#
Username = sora
Password = sora
Carrier Check = no
Auto DNS = 1
Check Def Route = 1" > /etc/wvdial.conf;
echo "allow-hotplug wwan0" >> /etc/network/interfaces;
echo "iface wwan0 inet wvdial" >> /etc/network/interfaces;
#if you want the pi to prefer the usage of the 4G connection over wifi or ethernet, uncomment the next line
#echo "replacedefaultroute" >> /etc/ppp/peers/wvdial;
