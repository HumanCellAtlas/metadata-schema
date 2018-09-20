# The Human Cell Atlas: Metadata Test Plan

## Table of Contents
- [Introduction](#introduction)
- [Develop tests](#develop_tests)
- [Integration tests](#integration_tests)
- [Stress tests](#stress_tests)
- [Ideas for improvement](#ideas_for_improvement)

## Introduction

This document is an overview of *proposed* test process for the metadata
schema.  The goal is to provide a test system that ensures the schema is
correct and follows the style, depreciation, and versioning guidelines.

The tests will be deployed using a continuous integration (CI) system that
validates changes when are tested when pushed to the repository.  By using a CI
system, there are no requirements on the developers or unexpected software.

Documentation extraction is done the CI process, making it a product of the
primary source, rather than checking it into the tree.


**What is in this document?**
 - The test plan for the metadata schema definition
 - Goals and high-level definition of the metadata schema tests
 
**Who should be reading this document?**
 - Schema developers

**What *isn't* in this document?**
 - Specific details of the implementation of the tests
 - Testing of metadata validation
 - Testing of metadata tools and libraries outside of this repository

## Develop tests
These tests will be run as part of a pull request to the development
repository and ideally configured to run when a developer pushes to a feature
branch in a repository.

The following are the set of tests to run on the schema.  Some of these may be combined into a single program.

1. Schema syntax checking. Validate that the schema is a valid JSON schema
1. Schema style lint.  Validate that the schema conforms to the style guide.  Configured known exceptions to the style guide generate warnings rather than errors.
1. Example validation.  All examples in the tree are validated against the schema and must reflect the current version for each schema module.
1. Validate and generate documentation.  Formatted documentation is an artifact of the CI build.
1. Version compatibility validation. This compares the current version of the schema with the previous version, based on semantic version number.  It validates that the semantic versioning and depreciation rules have been followed.


## Integration tests

A pull request to integration runs the [Develop tests](#develop_tests) and additional runs the following test:

1. Validation of a subset of real data.  This validates a specified set of production metadata against both the specified version and the latest compatible version (same major number) of the referenced schema. The subset is select based on a breadth of data types and previously failed examples.

## Stress tests

The stress tests are designed to do an extensive validation of existing metadata analogous to the DCP software stress tests.  These are run on a fixed schedule rather than being triggered by repository events.  If there have been no schema definition changes since the last run, the test is skipped.

1. Validation of the full set of real data.  This validates all current production metadata against both the specified version and the latest compatible version (same major number) of the referenced schema

## Ideas for improvement

*ideas welcome!*
