# How to run this demo

This Demo is meant to showcase the different workflows which developers and appsec
engineers can collborate on, in order to secure an application.

## Developer Workflow

1. Create an MR with GitLab using a feature branch
    - Introduce common security vulnerabilities
1. Create an MR, as well as have one that is already available (since it takes too long for the scans to run)
1. Describe the pipeline from end to end and go over each test that runs on the feature branch.
1. Within MR show the detailed information provided by the GitLab scanners
    - Show a vulnerability for each type of scanner
    - Show line of code where vulnerability has been found
    - Show information on vulnerabilities
    - Show how to resolve
    - Show how a confidential issue can be created
    - Show how a vulnerability can be dismissed
1. Resolve a vulnerability and re-run the pipeline
1. Display Merge-Request approvals
    - Go over Vulnerability-Check
    - Go over License-Check

## AppSec Engineer Workflow

1. Display the Project-Level Security Dashboard
    - Go over different types of sorting
    - View a vulnerability
    - Change the status of that vulnerability
    - Show that the user who changed the status as well as when is recorded.
1. Display the Group-Level Security Dashboard
    - Go over different types of sorting
    - Examine rate of change
    - Display A-F risk

## Configuration

1. Display the [.gitlab-ci.yml](../.gitlab-ci.yml) file.
    - Go into how to add security scanner templates
    - Go over environment variable
1. Show how to configure security scans with Auto DevOps
1. Show how to configure security scans using UI
