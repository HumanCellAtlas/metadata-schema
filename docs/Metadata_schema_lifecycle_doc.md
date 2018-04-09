# HCA Metadata schema lifecycle - v2.0

# Parts of this document to be divided into contributing, evolution, structure, and rationale docs

The **metadata design principles** can be read in the [Metadata schema lifecycle doc](docs/Metadata_schema_lifecycle_doc.md).

## Table of Contents
- [Open questions](#open-questions)

## Open questions

This section lists open questions about this process which are not yet covered by the process description 

#### Handling submissions in prep

Do we have a strategy for submissions in preparation while the update gets put in?

#### What is the testing process for changes to the metadata-schema?

When a new pull request is made, what integration tests need to be run to reduce the likelihood of something breaking

#### How are update requests assigned to committers?

How do we ensure that all update requests are assigned to a committer and there is a reasonable feedback timeframe.

#### What labels do we need in the github repo to label issues and PRs?

Github has a label system and we need to define the correct labels to annotate issues and PRs to enable more rapid assessment

#### Which developers/teams should be notified for which modules?

We need a process so the committers reviewing a change know which teams need to be reached out to for different suggested changes or to figure out how best to enable people to watch given modules in a git repo

#### What happens if a suggested change required a new software update to be deployed which can’t be carried out in the given timeframe?

How do we modify the process to handle this?

#### Are readmes/other docs in metadata-schema subject to the same review process?

Can the readmes or other documentation which is not contained inside a schema be edited by committers without PR review?

#### What is the formal process of tagging and making a new release in git?

Are there any existing HCA DCP processes we can adopt here

#### How long is reasonable between approval and merge of new schema and it being in production?

Presumably in almost all cases this needs to be instant (or near as damn it) but it would be good to understand if there are occasions where it can’t be if the change happening requires an update to the ingest or any other DCP software. We should discuss this with the engineering teams?
