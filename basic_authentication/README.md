# jira_automation
Repository to the interact with Jira using CLI

# Introduction

Considering the present Agile scenario, we have so many sprints and lots of issues to work on. Sometimes it becomes hectic to login everytime over the JIRA Board and move the status of the issues, change the assignee for the issue or create the new issues. Hence I created simple python codes to ease this stuff


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


# Further Improvements

I am working on following improvements as of now

1. Create the ticket  using CLI
2. Bulk update the tickets with same status
3. Create the bulk tickets


## Authors
 **Harsh Khajgiwale** [harsh.khajiwale@gmail.com](harsh.khajiwale@gmail.com)
