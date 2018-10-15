from jira import JIRA
import argparse
from ConfigParser import SafeConfigParser


cli_args = argparse.ArgumentParser()
cli_args.add_argument("-f","--file", required = True, help = "name of credentials file")
args = cli_args.parse_args()
args = vars(cli_args.parse_args())
credentials_file = str(format(args["file"]))
cf_parser = SafeConfigParser()
cf_parser.read(credentials_file)


JIRA_URL = cf_parser.get("credentials", "JIRA_URL")
JIRA_USERNAME = cf_parser.get("credentials", "JIRA_USERNAME")
JIRA_PASSWORD = cf_parser.get("credentials", "JIRA_PASSWORD")
JIRA_ID = raw_input("Enter Jira ID.[Eg: DL-1234]:\t")

class JiraInitializer:

    def __init__(self, jira_id, jira_url, jira_username, jira_password):
        self.jira_id = jira_id
        self.jira_url = jira_url
        self.jira_username = jira_username
        self.jira_password = jira_password

    def get_details(self):
            return "\n\t\tJIRA ID is: %s/%s"  %(self.jira_url,self.jira_id)

    def login_to_jira(self):
        jira_set_url = {'server': self.jira_url}
        jira_object = JIRA(jira_set_url, basic_auth=(str(self.jira_username),str(self.jira_password)))
        return jira_object

def change_status(JiraInitializer):
    jira_object = JiraInitializer.login_to_jira()
    issue_id = jira_object.issue(JIRA_ID.upper())
    print "\nPresent status  of issue: %s" %(issue_id.fields.status)
    print "\nAvaialable transitions are \t \n\t1. Pick Up \n\t2. Complete \n\t3. Verified \n\t4. Reopen"
    choice = input("\nEnter your choice\t")
    
    if choice == 1:
        if str(issue_id.fields.status) == 'In Progress' or str(issue_id.fields.status) == 'Verification':
            print "You cannot pick this ticket as the transition is:   %s" %(issue_id.fields.status)
        else:
            jira_object.transition_issue(issue_id, transition='Pick Up');
            print "Ticket %s is now allocated to you" %(JIRA_ID.upper())

    elif choice == 2:
        if str(issue_id.fields.status) == 'Verification':
            print "You cannot close this ticket as this is in Verification stage"
        else:
            closing_comment = raw_input("\nPlease add the closing comment:\t")
            jira_object.transition_issue(issue_id, transition='Complete', comment = str(closing_comment));
            print "Ticket %s has been closed" %(JIRA_ID.upper())

    elif choice == 3:
        if str(issue_id.fields.status) == 'Verification' and str(issue_id.fields.status) != 'In Progress':
            jira_object.transition_issue(issue_id, transition='Verified');
            print "Ticket %s is verified" %(JIRA_ID.upper())
        else:
            print "Ticket %s cannot be Verified since it is %s" %(JIRA_ID.upper(),issue_id.fields.status)

    elif choice == 4:
        if str(issue_id.fields.status) == 'Done':
            jira_object.transition_issue(issue_id, transition='Reopen');
            print "Ticket %s is now re-opened at your request" %(JIRA_ID.upper())
        else:
            print "Ticket is in %s state" %(issue_id.fields.status)

    elif choice == 5:
        if str(issue_id.fields.status) == 'Done':   
            jira_object.transition_issue(issue_id, transition='Invalid');
            print "Ticket %s has been marked as Invalid" %(JIRA_ID.upper())
        else:
            print "Ticket is in %s state"  %(issue_id.fields.status)


jiraInitializer = JiraInitializer (JIRA_ID.upper(), JIRA_URL, JIRA_USERNAME, JIRA_PASSWORD)
change_status(jiraInitializer)