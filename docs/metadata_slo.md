# Metadata SLO

This document outlines the HCA DCP metadata team’s promises related to metadata schema updates.


Type of Measure | Example SLO Requirement | Measurement Period
--- | --- | ---
Transparency | We commit to publishing any planned schema changes for review and discussion via the metadata-schema Github issue tracker and Github pull requests, and allow an appropriate number of working days for comments, as defined in the metadata schema update acceptance process | 3-10 working days before pre-release of a software-breaking change, depending of severity of change
Transparency | We commit to publishing develop, integration and staging pre-release versions of new schema ahead of production release, until such a time as an orthogonal testing suite has been developed to allow insulation of schema changes from software components. | Every major, minor, and patch change
Transparency | We commit to announcing schema changes and publish release notes on the Slack #hca-metadata and #dcp channels as soon as a schema pre-release is made. | Every major and minor pre-release; bug-fixing patch pre-release
Transparency | We commit to following the DCP release schedule for promotion of schema changes from integration to staging and staging to production, until such a time as an orthogonal testing suite has been developed to allow insulation of schema changes from software components. | DCP release schedule
Responsiveness | We commit to responding in a timely manner to concerns flagged by schema users monitoring schema release announcements and upcoming schema changes. | Ongoing
Transparency | We commit to developing and maintaining an orthogonal test suite to provide guarantees over schema changes and revise this test suite in response to changes in requirements of the metadata. | Ongoing


