# 4G_Pi
For all questions, contact admin@HughMungis.com

####BEFORE YOU RUN setup.sh####

First thing's first, make sure you change APN, user, and password in setup.sh
The sim card I'm using is from soracom, if you are using something else, make sure you get that information from your provider and change out what is in setup.sh

After you run the setup script, all you need to do to create the 4G interface is run "sudo wvdial"
At this point if you check your available interfaces with ifconfig, you should see a new "ppp" interface. This is your SIM internet connection.

If it doesn't work at first, I found it helpful to power off the hat, and then power it back on, which is why I included those scripts in the repo.
