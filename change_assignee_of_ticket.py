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

def change_assignee(JiraInitializer):
    jira_object = JiraInitializer.login_to_jira()
    issue_id = jira_object.issue(JIRA_ID)
    new_assignee = raw_input("\nEnter the new Assignee:\t")
    issue_id.update(assignee={'name': new_assignee})
    print "Issue %s has been assigned to: %s" %(JIRA_ID,new_assignee) 

jiraInitializer = JiraInitializer (JIRA_ID, JIRA_URL, JIRA_USERNAME, JIRA_PASSWORD)
change_assignee(jiraInitializer)
