# Objective of this document

Showcase the steps to merge a pull request made by the security bot (snyk) on vulnerabilities detected on the dependencies used by the repository.

# Who should do it?

First person to acknowledge the pull request made by the security bot should do either one of these two actions:

- If you are an allowed reviewer, assign yourself to the PR.
- If you are not an allowed reviewer, ask someone from the list of allowed security committers to assign themselves to the PR by posting a comment pinging that person.

The people currently allowed to review and merge this PRs are:

- @ESapenaVentura
- @simonjupp
- @diekhans
- @willrockout
- @rolando-ebi

<!Anyone else?>

# How to review

1. Look at the security report.
   
   - Available as a link under the snyk-bot PR, under the section `Vulnerabilities that will be fixed`.
   - In the report, you should be able to find the severity of the vulnerability. The higher the severity, the faster something should be done about it.

1. Access the pull request opened by snyk.

   - Assign `Security` label to the PR
   - Check what tests use the dependencies changed by the bot.
   - `git checkout` to that branch to get the changes locally.
   - Change the base branch to "develop"

1. Check tests locally
   
   - Run the affected tests manually to check that they run fine. If any test has broken, avoid next steps and issue a ticket with the structure outlined at the end of this document.
   
1. Merge Pull Request
   
   - Check that there are no conflicts, fix them if there are, and merge.
   - Depending on the severity of the vulnerability, the next steps are:
      - **High security vulnerability**: This patch needs to be applied to all environments as soon as possible. Proceed to step 5.
      - **Low/Medium security vulnerability**: This patch is not urgent, so will get propagated from develop to `integration`, `staging` and `production` on their respective releases. Proceed to step 6.
   
1. Merge Pull Request to the other environments
   
   <!-- IMPORTANT: SHOULD WE RUN THE TESTS FOR EACH ENVIRONMENT? -->
   
   - Create a pull request, using the security branch as remote, to the following environments:
     
     - `integration`
     - `staging`
     - `master`
   
   - In order to do it, repeat the next steps for each environment:
     - Check out to snyk branch, make sure it's up to date in your computer and pull the environment branch into it:
        - `git checkout <snyk-branch>`
        - `git pull`
        - `git pull origin <env>`
     - If everything went correctly, you will be prompted to write a commit message. Leave it as it is and save-quit.
     - Go to GitHub and compare the <env> branch with the <snyk> branch.
        - Compare files in order to make sure only the security updates have been pushed.
        - Write the same title/body of the pull request that snyk made to master. Label it with the `Security` label.
        - Wait for the travis test to pass.
        
   - Merge pull requests as indicated in point 4.
   - Repeat the procedure for each environment.
  
1. Delete branch.
      
# Ticket structure

## High severity

<!-- Please follow the next pattern for the title of the ticket: 
[URGENT] High severity security issue - PR #<Number of PR>-->

As per date \<Date\>, a high priority vulnerability has been detected in the dependencies of this repository. Update to the recommended dependencies breaks the following tests:

- `test`

A fix is urgently needed.

## Medium or low severity
<!-- Please follow the next pattern for the title of the ticket: 
low/medium severity security issue - PR #<Number of PR>-->

As per date \<Date\>, a low priority vulnerability has been detected in the dependencies of this repository. Update to the recommended dependencies breaks the following tests:

- `test`

As a HCA DCP team member, I would like to address this low priority issue here and prompt to search for a solution in the least amount of time possible.