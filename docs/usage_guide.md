# Simply Simple Notes Usage Guide

This guide is meant to guide a user through the process of getting started with
Build, Testing, Scanning, and Deploying an application within GitLab. It has a
high emphasis on testing out the Security features provided by GitLab.

This guide is meant for a user who wishes to move over this application to their
namespace and play around with it on there. If user just intends to view the security
features, they can see the [Running Demo](./running_demo.md) section.

**Note:** Requires [GitLab Gold](https://about.gitlab.com/pricing/ultimate/).

## Create a GitLab Account

If you do not already have a [GitLab account](https://gitlab.com/), please create one. 
GitLab Gold is avaliable as a [free-trial](https://about.gitlab.com/free-trial/) for 30 days.

## Migrate Application

You can import [Simply Simple Notes](https://gitlab.com/gitlab-examples/security/simply-simple-notes) to your project repo using it's
[Git Repository URL](https://docs.gitlab.com/ee/user/project/import/repo_by_url.html).

## Create a Kubernetes Cluster

This application is containerized and provides a helm chart so that it can be deployed onto
a Kubernetes Cluster. A Kubernetes cluster is required in order to run this demo application.

In order to create a cluster and attach a Kubernetes cluster to your project,
see the [Add/Remove Cluster documentation](https://docs.gitlab.com/ee/user/project/clusters/add_remove_clusters.html)

The cluster should be enabled as a GitLab-managed cluster. Also the Simply Simple Notes
project should be added as a [Cluster Management Project](https://docs.gitlab.com/ee/user/clusters/management_project.html).

**Cluster Requirements:**

The minimum cluster requirements are as follows:

- CPU: 2 vCPU
- Memory: 2 GB
- Hard-Disk: Standard 100GB

## Setup the DNS

In order to get the full benefit of the application, you should add a [DNS entry](https://cloud.google.com/dns)
to your Kubernetes cluster's ingress external IP.

To access the ingress-controller's external IP, run the following command:
```
$ kubectl get service -n gitlab-managed-apps
NAME                                    TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)
ingress-nginx-ingress-controller        LoadBalancer   10.0.14.46    130.211.232.146   80:32512/TCP,443:32411/TCP
```

Then you can add the DNS entry to your Kubernetes cluster's [base domain](https://docs.gitlab.com/ee/user/project/clusters/#base-domain).

Once the DNS has been setup, you need to change a few variables to enable DAST to scan the correct URL.
- [README.md](../README.md): has a link to the url where the project is hosted, we just need to change this.
- [.gitlab-ci.yml](../.gitlab-ci.yml): tells DAST which URL to scan, this needs to be changed.
- [sitemap.xml](../notes/static/sitemap.xml): provides the sitemap for your application, this needs to be changed.

## Run Pipeline

Once the project has been migrated and the cluster has been attached, 
you can [run a pipeline](https://docs.gitlab.com/ee/ci/pipelines/#run-a-pipeline-manually) on the master branch and make sure that the
security scans are running.

[Adding Security to your CICD Pipeline](https://youtu.be/Fd5DhebtScg) provides more information on how the security scans are configured in the pipeline.
