# The Human Cell Atlas Metadata Update Process SOP

## General information

You can read the work in progress in [HCA metadata lifecycle and versioning](https://docs.google.com/document/d/1eUVpYDLu2AxmxRw2ZUMM-jpKNxQudJbznNyNRp35nLc/edit?usp=sharing).

## Specific commands for contributing changes to the v5_prototype branch

This section will outline steps for contributing changes to the v5_prototype branch in the command line

1. Clone the metadata-schema repository into your local machine

    `git clone git@github.com:HumanCellAtlas/metadata-schema.git`

1. Navigate to the metadata-schema repo

    `cd metadata-schema`
    
1. Switch to the v5_prototype branch

    `git checkout v5_prototype`

1. Make and switch to a new working branch from v5_prototype. Name the branch following the convention: `v5_prototype-brief_desc_branch_scope`

    `git checkout -b v5_prototype-brief_desc_branch_scope`

1. Make changes locally to this branch. After a set of changes, run the `src/schemas_are_valid_json.py` and `src/json_examples_validate_against_schema.py` scripts and ensure both exit with status 0. These are the tests that Travis CI runs in GitHub.

1. Commit to the working branch often and after a set of logically grouped changes to help track changes. Use helpful/short messages in commit statement.

    `git add <changed files>`
    
    `git commit -m "Helpful commit message here."`

1. Push changes to working branch when ready.

    `git push origin v5_prototype-brief_desc_branch_scope`

1. New changes can be committed and pushed to this branch at any time, even after merging (if the branch isnt' deleted). Once the changes are ready for a review and pull request, switch back to the GitHub UI to create the PR (or do it in the CL if you're fancy).
    - Navigate to the repo[here](https://github.com/HumanCellAtlas/metadata-schema)
    - Switch to the working branch
    - Click "Pull request" in the upper right corner
    - Make sure the base branch is "v5_prototype" and the compare branch is the working branch
    - In the comment section of the PR, write a general description of the changes followed by a bulleted list of the specific changes made in the files
    - Click "Create pull request" when ready
    - Assign reviewers (top right of page) to send notifications that a PR needs to be reviewed and merged. **Do not merge your own PR.**

1. After a PR is merged, delete the branch if there are no more changes to be made for that specific topic. We would like to keep the list of active branches clean.
