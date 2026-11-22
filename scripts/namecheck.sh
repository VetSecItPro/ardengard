#!/bin/bash
# usage: namecheck.sh name...  prints name|gh_exact|npm|pypi|com|dev  (free = nothing found)
for n in "$@"; do
  l=$(echo "$n" | tr 'A-Z' 'a-z')
  gh_exact=$(gh api "search/repositories?q=$l+in:name&per_page=100" --jq "[.items[] | select((.name|ascii_downcase)==\"$l\")] | length" 2>/dev/null || echo ERR)
  npm=$(curl -s -o /dev/null -w '%{http_code}' "https://registry.npmjs.org/$l")
  pypi=$(curl -s -o /dev/null -w '%{http_code}' "https://pypi.org/pypi/$l/json")
  com=$(curl -s -o /dev/null -w '%{http_code}' "https://rdap.verisign.com/com/v1/domain/$l.com")
  dev=$(curl -s -o /dev/null -w '%{http_code}' "https://pubapi.registry.google/rdap/domain/$l.dev")
  echo "$n|$gh_exact|$npm|$pypi|$com|$dev"
  sleep 2
done
