# Lab 1 report

Replace every `TODO` with your answer. The automated checks make sure nothing is left blank.

## Part A: Observe the web

**A1.** Open https://lebaveux.com, open the developer tools (F12), **Network** tab, and reload. For the first request:

- Method: TODO
- Status code: TODO
- Three response headers (name and value): TODO

**A2.** Find the `strict-transport-security` header. What does it do?

TODO

**A3.** Run `curl -i "https://www.federalregister.gov/api/v1/documents.json?per_page=2"`.

- Status code: TODO
- Content type: TODO
- In the JSON, name one object, one list and one key/value pair: TODO

**A4.** Run the same command on a path that does not exist: `curl -i "https://www.federalregister.gov/api/v1/documentz.json"`.

- Status code, and what it means: TODO

## Part B: The double charge

**B1.** Run `python credits.py` *before* fixing it. How many analyses start? How many credits are left?

TODO

**B2.** Explain the double charge in about five lines, using the timeline table from lesson 2.

TODO

**B3.** Describe your fix in one or two sentences.

TODO

**Going further (optional).** With 10 simultaneous clicks and 3 credits, how many analyses should start? Did you check it?

TODO
