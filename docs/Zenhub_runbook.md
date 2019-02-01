# Metadata-schema Zenhub Pipelines Runbook

This document defines what the different pipelines (columns) in ZenHub mean for the metadata-schema repo in GitHub.

## Glossary

Milestone = sprint period

Issue = ticket

GH = GitHub

ZH = ZenHub

## Pipeline definitions

### New Issues

DEFINITION: Issues are automatically put into New Issues when they are
created in GH/ZH.

The metadata-schema repo has 4 main types of Issues:

1.  Requests for schema updates
1.  Requests for new schemas
1.  Bug reports
1.  Other repo tasks

New Issues of type 1, 2, or 3 should:
-   have all sections of the issue template filled out
-   not be assigned to someone

New Issues of type 4 should:
-   have as many of the sections of the issue template filled out as possible*
-   not be assigned to someone

\* *Acceptance Criteria may be left blank until Sprint Planning*

Anyone (on Metadata Team or not) can create Issues in the metadata-schema repo. Every two weeks during Sprint Planning, the Metadata Team and Product Owner will go through the New Issues and update the following:

New Issues (after Sprint Planning) should:
-   be assigned appropriate label(s)
-   not be assigned to someone
-   not be assigned a milestone
-   be assigned estimated points, if applicable
-   be assigned to an Epic, if applicable
-   be updated with **Acceptance Criteria** (type 4 Issues only)

If the New Issue *has* the above items completed during Sprint Planning (**Acceptance Criteria** is especially important for type 4 Issues), then it should:
-   be moved to Icebox if the New Issue *will likely never* be addressed in the current scope of the project
-   be moved to Backlog if the New Issue *will* be addressed

If the New Issue *does not have* the above items completed during Sprint Planning, then it remains in the New Issue pipeline until it does.

### Icebox

DEFINITION: Issues that do not fall within the current scope of the project are moved from New Issues into the Icebox. Periodic review of scope and priorities should occur with the Product Owner, and any Icebox Issues determined to now fall within the scope and priorities of the project should be moved to the Backlog.

Icebox Issues should:
-   already have been assigned appropriate label(s)
-   not be assigned to someone
-   not be assigned milestone
-   already have been assigned estimated points, if applicable
-   already have been assigned to an Epic, if applicable
-   be moved to Backlog pipeline if determined to now be in scope and priorities of the project

### Epics

DEFINITION: Epics are longer, more complex tasks that (usually) cannot be addressed with one Issue. Epics should be written like user stories. The Epic *title* should define the concrete goal, and the Epic *description* should define the type of user, what they want, and why they want it. An example Epic is:

> *Title*: Release first draft of schemas to support imaging spatial transcriptomics
>
> *Description*: As a SpaceTx developer, I want to be able to incorporate SpaceTx metadata into the HCA metadata schema in order to describe imaging data using the HCA metadata schema.

Epics should:
-   be assigned appropriate label(s)
-   never be assigned to someone
-   never be assigned a milestone
-   never be assigned estimated points
-   be moved to Epics pipeline

### Backlog

DEFINITION: Backlog Issues are issues that need to be addressed in the current scope and priorities of the project. Issues should be moved from New Issues or Icebox into the Backlog pipeline after discussion with the Product Owner. Backlog should be prioritized, although currently the Metadata Team and Product Owner do not do specific backlog grooming.

Backlog Issues should:
-   already have been assigned appropriate label(s)
-   not be assigned to someone
-   not be assigned milestone(s)
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
-   be moved to To Do/Ready pipeline when the Issue is in the scope of the current milestone

### To Do/Ready

DEFINITION: To Do/Ready Issues are issues that are in the scope of the current milestone. The Metadata Team does not currently run in typical "sprints", but are going to try working in 1 month intervals and see how that works.

To Do/Ready Issues should:
-   already have been assigned appropriate label(s)
-   not be assigned to someone
-   be assigned to the current milestone
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
-   be moved to In Progress pipeline when a Committer starts to work on it

### In Progress

DEFINITION: In Progress Issues are issues that a Committer has selected to work on. The Issue is currently being addressed in a new branch made by the Committer off of the develop branch. **Before making a PR, Committer should run tests over their branch that test whether the schema updates adhere to the metadata standards. We don't have these tests right now.**

In Progress Issues should:
-   already have been assigned appropriate label(s)
-   be assigned to the Committer who takes the Issue
-   already have been assigned milestone(s)
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
-   be moved to Review/QA pipeline when a PR is opened against develop

### Review/QA

DEFINITION: Review/QA Issues are Issues for which the associated branch with changes is in an open PR.

Review/QA Issues should:
-   already have been assigned appropriate label(s)
-   already have been assigned a Committer
-   be assigned Reviewers
-   already have been assigned milestone(s)
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
-   be moved to Done pipeline when associated PR is merged into develop

### Done

DEFINITION: Done Issues are Issues for which the associated branch with changes has been merged into develop. **At this point, some tests should run over develop that test integration of schema updates. We don't have these tests right now.**

Done Issues should:
-   be assigned the "Done" label
-   already have been assigned appropriate label(s)
-   already have been assigned a Committer
-   already have been assigned Reviewers
-   already have been assigned milestone(s)
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
-   be moved to Closed pipeline when associated PR is merged into master

### Closed

DEFINITION: Closed Issues are Issues for which the associated branch with changes has been merged into master. If an Issue was specifically tagged in a commit statement for a PR is merged to master, the Issue will close automatically. Otherwise, the Issue should be closed manually.

Closed Issues should:
-   already have been assigned appropriate label(s)
-   already have been assigned a Committer
-   already have been assigned Reviewers
-   already have been assigned milestone(s)
-   already have been assigned estimated points
-   already have been assigned to Epic(s), if appropriate
