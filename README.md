# monies-script

This is a script for calculating debts based on a simple Telegram 2 person chat.  

The script is very simple and only works for a pretty specific accounting format. However, I have found it quite easy to track common expenses with my flatmate using this system.  

The script can handle the following messages:
- `100`
- `200 - Pizza`
- `400: Pizza Pasta`
  
In this method, a common expense is logged into the dedicated chat. For example, one person pays 400 for the evening pizza and logs it into the chat. This script can then calculate that the Diff is 400 and the other person owes 200.
