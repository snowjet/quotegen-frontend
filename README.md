# quotegen-frontend

This is a simple frontend that displays famous quotes from a backend Quote Generator.

![Contribute](images/example.png)


## CodeReady Workspaces

[![Contribute](images/factory-contribute.svg)](https://codeready-openshift-workspaces.apps-crc.testing/f?url=https://github.com/snowjet/quotegen-frontend)


## create application with postgres backend

```bash

oc apply -f ./oc_templates/is_frontend.yaml
oc apply -f ./oc_templates/svc_frontend.yaml
oc apply -f ./oc_templates/dc_frontend.yaml

oc expose svc/frontend

```

## Backend Response Example:

```json
{
 "backend":"postgresql",
 "quotes": {
    "name":"Benjamin Franklin",
    "quote":"Tell me and I forget.  Teach me and I remember.  Involve me and I learn."
}}
```

## Backends

See https://github.com/snowjet/demo-quote-gen for backend