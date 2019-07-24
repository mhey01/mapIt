#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip

if sys.argv[1:2] == ['find']:
    if len(sys.argv) > 1:
    # Get address from command line.
        address = ' '.join(sys.argv[2:3])
    else:
    # Get address from clipboard.
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)  
elif sys.argv[1:2] == ['dir']:
    if len(sys.argv) > 1:
    # Get address from command line.
        address1 = ' '.join(sys.argv[2:3])
        address2 = ' '.join(sys.argv[3:4])
        travel = ' '.join(sys.argv[4:5])
    webbrowser.open('https://www.google.com/maps/dir/?api=1&origin=' + address1 + '&destination=' + address2 + '&travelmode=' + travel)
else:
    print("ERROR: 'find' or 'dir' not entered")

#https://www.google.com/maps/dir/?api=1&origin=Space+Needle+Seattle+WA&destination=Pike+Place+Market+Seattle+WA&travelmode=bicycling
