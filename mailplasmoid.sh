#!/bin/bash

RESULT=$(python ~/bin/py_gmail_notifier.py -C)
ERROR=$(echo $RESULT | grep -c -i ERROR)

if [ "$RESULT" == "" ]; 
then
	# no mail: MesloLGS NF font
	echo -e "\uF2B7"
elif [ "$ERROR" == "1" ]; 
then
	# ERROR: MesloLGS NF font
	echo -e "\uF260"
else
	# mail icon: MesloLGS NF font
	# echo -e "\uF2B6"
	# g-mail icon - MesloLGS NF font
	echo -e "\uF2B6"
fi
