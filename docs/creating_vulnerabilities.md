# How to Create Vulnerabilities for the Demo

This document is a guide on how to create vulnerabilities. These vulnerabilities should be added 
within an MR, that way GitLab Security features can be showcased.

## Static Application Security Testing (SAST) + Secret Detection

SAST scans the application's static source code for vulnerabilites.
It can detect things like bad file permissions, SQL injection, etc.

In this example we will make the code suseptible to SQL injection, by
adding some code vulnerable to SQL injection to [db.py](../notes/db.py):

```
def select_note_by_id_vulnerable(conn, id):
    query = "SELECT * FROM notes WHERE id = '%s'" % id

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    return str(rows)
```

You can also add make a file extermely permissive by adding configuring
the permission of the `notes.db` file generated in the [db.py](../notes/db.py) file:

```
os.chmod(name, 0o777)
```

For secret detection to run we can add an AWS sample Token to [run.py](../run.py):

```
    aws_key_id = "AKIAIOSFODNN7EXAMPLE"
    aws_key_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
```

## Dynamic Application Security Testing (DAST)

DAST scans a running application's for vulnerabilites by sending
malicious requests. It can detect things like XSS, etc.

In order to create a DAST vulnerability, we can add a new route to the
application in [routes.py](../notes/routes.py):

```
@note.route('/get-with-vuln', methods=['GET'])
def get_note_with_vulnerability():
    id = request.args.get('id')
    conn = db.create_connection()

    with conn:
        try:
            return str(db.select_note_by_id(conn, id))
        except Exception as e:
            return "Failed to delete Note: %s" % e
```

Be sure to add the new path to the [sitemap.xml](../notes/static/sitemap.xml)

## Dependency Scanning

Dependency Scanning checks the [requirements.txt](../requirements.txt) for
any libraries with vulnerabilities. In order to create a Depending Scanning
vulnerability you can add a vulnerable version of django and change the version
of Flask:

```
Flask==0.12.2
django==2.0.0
```

## Container Scanning

Container Scanning checks the [Dockerfile](../Dockerfile) for
any images with vulnerabilities. In order to create a Container Scanning
vulnerability you can change the version of alpine:

```
FROM python:alpine3.4
```

## License Scanning

License Scanning scans licenses for dependencies in [requirements.txt](../requirements.txt) and
matches them agains a policy. In order to create a License Scanning vulnerability you can add the
Apache 2.0 License to the list of denied licenses via the [License Compliance](https://docs.gitlab.com/ee/user/compliance/license_compliance/) Interface and add the following to requirements.txt:

```
dubbo-client
```
