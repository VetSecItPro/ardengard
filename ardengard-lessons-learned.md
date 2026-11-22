# Ardengard Lessons Learned

Two or three sentences per entry: what went wrong (especially what the AI got wrong unprompted), the correction, the
guard. Central date and time on every entry. Entries before 2026-11-22 10:45 CT were made while the work lived in
17.scratchpad and are copied here as the project's own history.

## 2026-11-21 10:27 CT: time stamps written from memory
Stamps such as 10:40 and 11:15 CT were typed into the log and backlog when the clock read 10:08 to 10:27 CT. Correction: every stamp rechecked against the clock. Guard: scripts compute the stamp themselves (zoneinfo America/Chicago); prose gets it from a `date` call made just before.

## 2026-11-22 09:46 CT: an account switch cut off the workbook page
After a /login to the other Claude account, the session could not read or update the page, the same failure as FerryMail two days earlier. Correction: republished from the local files under the current account. Guard: every first publish names the owning account and asks the operator to share it with the other one.

## 2026-11-22 10:10 CT: names offered without checking them
The first name list was all real words, every one already used by other projects; the operator asked why. Correction: invented names, checked with scripts/namecheck.sh (which passed a known-answer control) before showing any. Guard: never offer a name that has not passed the check.

## 2026-11-22 09:56 CT: a terms-of-service claim stated too strongly
Claude said stealth browsing and CAPTCHA bypass would break sites' terms, then the operator asked why a paid service could sell it. Correction: terms bind the site's user, not the tool seller, and legality depends on the site and on logged-in versus public data. Guard: state legal points with their limits and say "not legal advice".
