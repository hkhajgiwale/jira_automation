# Dependencies

You should have python installed at your machine and the major depenedency is:
```
pip install jira
```


# Usage

First things first. The login needs to be done using basic authentication mechanism. So you need to update the credentials.txt with your respective email id, password and JIRA Link. This is completely interactive so you would get the easily get through it. File usage is as under:

1. Change the name of the assignee
```
python change_assignee_of_ticket.py -f credentials.txt
```

2. Change the status of the ticket (Pick Up, Verified, Invalid, Reopen)

```
python change_ticket_status.py -f credentials.txt
```


## Authors
 **Harsh Khajgiwale** [harsh.khajgiwale@gmail.com](harsh.khajiwale@gmail.com)
