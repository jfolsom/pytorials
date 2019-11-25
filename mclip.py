#! python python3
# mclip.py - A multi-clipboard program.
import sys
import pyperclip

#create variables with empty strings in case they are needed later
senddata = ''
low28 = ''
funkybreak = ''

if sys.argv[1] == 'senddata':
    senddata = (sys.argv[2] + """,\n\nWe've completed testing for """ + sys.argv[3] +
               """.  Kindly confirm receipt, and if you have any question or concerns, let me know those to.\n""" +
               """Thanks for the work and best wishes.""")
if sys.argv[1] == 'low28':
    low28 = ("""I'm signing a break report with low 28 day breaks for set """ + sys.argv[2] +
             """ from """ + sys.argv[4] + """.""")

if sys.argv[1] == 'funkybreak':
    funkybreak = ("""I'm signing a concrete report for set """ + sys.argv[2] +
                  """I'm flagging this set because of: """ + sys.argv[3])


TEXT = {'agree': """Yes, I agree.  That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'senddata': senddata,
        'low28' : low28,
        'funkybreak' : funkybreak}



if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase ] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
