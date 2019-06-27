# Objective of this document

Showcase the steps to merge a pull request made by the security bot (snyk) on vulnerabilities detected on the dependencies used by the repository.

# Who should do it?

First person to acknowledge the pull request made by the security bot should do either one of these two actions:

- Take the PR if you are an allowed reviewer.
- Ask someone from the list of allowed security commiters by posting a comment pinging that person.

The people currently allowed to review and merge this PRs are:

- @malloryfreeberg
- @ESapenaVentura
- @daniwelter
- @simonjupp

<!Anyone else?>

# How to review

1. Look at the security report.
   
   - You should be able to find it somewhere?
   - In the report, you should be able to find the severity of the vulnerability. The higher the severity, the faster something should be done about it.

1. Access the pull request opened by snyk.

   - Assign `Security` label to the PR
   - Check what tests use the dependencies changed by the bot.
   - `git checkout` to that branch to get the changes locally.

1. Check tests locally
   
   - Run the affected tests manually to check that they run fine. If any test has broken, avoid next steps and issue a ticket with the structure outlined at the end of this document.
   
1. Merge Pull Request to master
   
   - Check that there are no conflicts, fix them if there are, and merge.
   - **DO NOT DELETE BRANCH**
   
1. Merge Pull Request to the other environments
   
   - Create a pull request, using the security branch as remote, to the following enviroments:
     
     - `develop`
     - `integration`
     - `staging`
   
   - In order to do it, follow the next steps:
     - If not in the branch, `git checkout <nameofsnykbranch>`
     - `git push origin <environment>`
     - Go to GitHub and press on `Compare and pull`
     - Input the necessary information and label it with the `Security` label
   
   - Merge pull requests as indicated on the point 4.
   
1. Delete branch 
      
# Ticket structure

## High severity

<!-- Please follow the next pattern for the title of the ticket: 
[URGENT] High severity security issue - PR #<Number of PR>-->

As per date \<Date\>, a high priority vulnerability has been detected in the dependencies of this repository. Updated to the recommended dependencies breaks the following tests:

- `test`

A fix is urgently needed.

## Medium or low severity
<!-- Please follow the next pattern for the title of the ticket: 
low/medium severity security issue - PR #<Number of PR>-->

As per date \<Date\>, a low priority vulnerability has been detected in the dependencies of this repository. Updated to the recommended dependencies breaks the following tests:

- `test`

As a HCA DCP team member, I would like to address this low priority issue here and prompt to search for a solution in the least amount of time possible.