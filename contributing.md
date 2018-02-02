# The Human Cell Atlas Metadata Update Process SOP

## General information about the update process

Information about the process by which the HCA metadata schema will evolve can be found in the [HCA metadata lifecycle and versioning](https://docs.google.com/document/d/1eUVpYDLu2AxmxRw2ZUMM-jpKNxQudJbznNyNRp35nLc/edit#heading=h.6p3dwsx7c3hb) document. This document includes the HCA schema design principles and the semantics and process for versioning and updating these schema. For discussion of the detailed format and syntax of the metadata schema and their instantiation, see the complementary document [Metadata schema structure specification](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?ts=59b16455). These documents should be viewable by everyone. Please contact us if you do not have access to view.

## Specific commands for contributing changes to the v5_prototype branch

If you are viewing this text, you are in the v5_prototype branch of the metadata-schema repo. This branch is the current working branch for schema changes to move from v4.6.1 to v5.0.0 of the HCA metadata schema. This is a major version change and constitues a large number of structural changes to the schemas as well as additions of many new fields based on 2017 Q4 user evaluations. Because this is a large schema change prior to going live, we are not implementing the typical major.minor.patch versioning scheme for upgrading to v5.0.0. 

This section outlines steps for members of the DCP's ingest team (collaboration between UCSC and EBI) to contribute changes to the v5_prototype branch.


1. **Clone** the metadata-schema repository into your local environment.

    `git clone git@github.com:HumanCellAtlas/metadata-schema.git`

1. **Navigate** to the metadata-schema repo.

    `cd metadata-schema`
    
1. **Switch** to the v5_prototype branch. All updates should be based on the current working version of v5.0.0.

    `git checkout v5_prototype`

1. **Make** and **switch** to a new working branch from v5_prototype. Name the branch following the convention: `v5_prototype-brief_desc_of_branch_scope`

    `git checkout -b v5_prototype-brief_desc_branch_scope`

1. **Make** changes locally to the new working branch. After making changes, it is important to run the `src/schemas_are_valid_json.py` and `src/json_examples_validate_against_schema.py` scripts (which are run by Travis CI). The first script checks whether each .json file in the `json_schema` folder is valid JSON format. The second script attempts to validate example JSON files in the `schema_test_files` directory against their corresponding schemas. Some of the JSON files are meant to fail (e.g. they are lacking required fields) and as their failure is expected behavior, the script should exit with status 0. Ensure both scripts exit with status 0 (you should see `Process finished with exit code 0` printed to the terminal) before committing changes. If either test fails, you will have to debug and fix the errors in the changes you made.

1. **Stage** and **commit** your changes to the working branch often. We recommend committing after making a few logically grouped changes to help track changes. Use helpful/short messages in commit statement. If your commit specifically fixes/addresses a current GitHub issue, you can add the phrase "Fixes #000" to the commit statement, replacing "000" with the number of the issues. This phrase is handy because when the changes are merged into the master branch, it automatically closes the issue indicated.

    `git add <changed files>`
    
    `git commit -m "Helpful commit message here. Fixes #000."`

1. **Push** the committed changes to the working branch.

    `git push origin v5_prototype-brief_desc_branch_scope`

1. **Continue** to make, stage, and commit changes to the working branch - ensuring that the two Travis CI scripts pass - until you have completed and pushed all the changes within the scope of your new branch. In the GitHub UI, **create** a pull request (PR) against the `v5_prototype` branch by doing the following:
    - Navigate to the [metadata-schema repo](https://github.com/HumanCellAtlas/metadata-schema)
    - Click on "master" in the drop-down menu in the top left of the page and select your new working branch
    - Click "Pull request" in the upper right corner
    - Change the base branch to "v5_prototype" and make sure the compare branch is your new working branch
    - In the comment section of the PR, write a general description of the changes followed by a bulleted list of the specific changes made in the files
    - Click "Create pull request" when ready
    - Assign reviewers (top right of page) to send notifications that a PR needs to be reviewed and merged. **Do not merge your own PR.**

1. After a PR is merged, delete the branch if there are no more changes to be made for that specific topic. We would like to keep the list of active branches clean.

## Observed guidelines

- Don't merge your own PR. This ensures that at least one other person has reviewed your suggested changes and has approved them. The only exception is if another person specifically "approves" your PR, but doesn't actually merge it. In this scenario, because the other person gave approval that they agree with the changes, the original PRer is allowed to merge their own changes.
- Be as clear and descriptive as possible when commenting on the PR. Include references to current GitHub issues when appropriate. Reference specific people if the PR addresses someones concerns. Include reasoning behind changes that could be controvesial (e.g. reason why a field names changes, but no reason needed to fix a typo in a field description).

