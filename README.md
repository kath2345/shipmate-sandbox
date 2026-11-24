# shipmate-sandbox

Test target repo for Shipmate, our Agentware T2 entry.

A tiny Python app with a deliberately failing CI: `test_average_empty`
expects `average([])` to return 0, but the current code raises
ZeroDivisionError, so the workflow fails on every push.

Shipmate practices on this repo: PR triage, code review, failed-build
diagnosis and first response to new issues.
