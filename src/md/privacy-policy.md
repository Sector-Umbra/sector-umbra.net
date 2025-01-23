Policy last updated: 23rd of January, 2025

A notice will be made if this document is changed.

<br>

<div class="warn"><strong>IMPORTANT NOTICE</strong><br>This document was written with the best of intentions, but has not been reviewed by a GDPR compliance expert. Such a review has been requested from the relevant Data Protection Authority in Belgium, and this document will be updated to reflect any feedback provided to us, when that feedback is provided.</div>

<br>

# Contact information.

Data Controller: TsjipTsjip (Project Manager and Server Manager at Sector Umbra)
- Discord: `TsjipTsjip`
- E-mail: Address available on request.
- Patreon: Built-in messaging for members.

# For what purposes do we process your personal data?

1. **Game server operation:** To offer members-only access to the Sector Umbra game server, on the conditions outlined in our server rules.
2. **Game server rules enforcement:** To enforce our server rules and uphold imposed punishments for violations of our server rules, even if the member is no longer whitelisted on our server as a result, in the interest of maintaining a safe and moderated environment for our members.
3. **Website operation:** To offer public access to supplementary information via this website and the wiki website.
4. **Wiki accounts:** To permit easy modification to authorised individuals of pages on the wiki website.
5. **Round replays:** To offer access to replay recordings made from scheduled sessions recorded on the Sector Umbra game server for the purpose of browsing and referencing past in-universe events.
6. **Patreon donations:** To allow members who wish to do so the ability to donate to the project financially for the purpose of funding the monthly costs hosting the server incurs.

<br>

We use these numbers to link back to these purposes throughout the document.

---

We consider the purposes listed above to be lawful purposes for processing personal data on the following grounds for processing listed in [Art. 6 of the GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504&qid=1532348683434):

<br>

| **Legal basis** | **1.** | **2.** | **3.** | **4.** | **5.** | **6.** |
|-----------------|--------|--------|--------|--------|--------|--------|
| <div class="left">Processing to perform a contract</div> | <abbr title="The contract is formed by the requirement to explicitly agree to our server's rules before being able to play, in return for being offered access to a safe and moderated environment to play.">✅</abbr> | | | | | |
| <div class="left">Explicit consent for processing</div> | | | <abbr title="Explicit consent is given by you navigating to this site.">✅</abbr> | <abbr title="Explicit consent is given by you logging in, and permitting the SS14 authentication server to provide access to the required personal data to create a mirror account on the Wiki.">✅</abbr> | | <abbr title="Explicit consent is given by you choosing to become a donator for our server.">✅</abbr> |
| <div class="left">Legitimate interest for processing</div> | | <abbr title="It is in the legitimate interest of the server and its players that problematic players are removed.">✅</abbr> | | | <abbr title="We consider the ability to look back on past events and obtain a bigger picture than what would be gained through the perspective of a player's character to be in the legitimate interest of the players.">✅</abbr> | |

<br>

# What data do we process for these purposes?

<br>

| **Data type** | **1.** | **2.** | **3.** | **4.** | **5.** | **6.** |
|---------------|--------|--------|--------|--------|--------|--------|
| <div class="left">SS14 Account names</div> | ✅ | ✅ | | ✅ | ✅ | |
| <div class="left">SS14 Account ID's</div> | ✅ | ✅ | | ✅ | | |
| <div class="left"><abbr title="An automatically generated logs system by the SS14 codebase, for the purpose of allowing admins to investigate rulebreaking behavior.">Admin logs</abbr></div> | | ✅ | | | | |
| <div class="left"><abbr title="Essentially a limited version of admin logs, showing only whether or not you did or did not participate in a SCHEDULED round.">Round participation</abbr></div> | | <abbr title="Not directly used, but indirectly processed as Admin Logs."></abbr>| | | ✅ | |
| <div class="left"><abbr title="Includes both IPv4 and IPv6 addresses used when connecting to our services.">Internet Protocol addresses</abbr></div> | ✅ | ✅ | ✅ | ✅ | | |
| <div class="left">Robust Hardware ID's</div> | | ✅ | | | | | |
| <div class="left"><abbr title="Includes account name, e-mail address, linked discord account, payment history and payment currency">Patreon account information</abbr></div> | | | | | | ✅ |

<br>

# Who processes this data?

<br>

| **Person / Role** | **SS14 Name** | **SS14 ID** | **ALogs** | **Round participation** | **IP's** | **HWID's** | **Patreon info** |
|-------------------|---------------|-------------|-----------|-------------------------|----------|------------|------------------|
| <div class="left"><abbr title="This is the server host, and for this reason they have access to all processed information at all times.">TsjipTsjip</abbr></div> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| <div class="left"><abbr title="Access is available at any time.">Project Managers</abbr></div> | ✅ | ✅ | ✅ | ✅ | <abbr title="This information is only accessed with TsjipTsjip's permission and supervision.">✅</abbr> | <abbr title="This information is only accessed with TsjipTsjip's permission and supervision.">✅</abbr> | | |
| <div class="left"><abbr title="Includes Trial Game Masters. Access is only available while the GM is connected to the server.">Game Masters</abbr></div> | ✅ | ✅ | ✅ | ✅ | | | |
| <div class="left"><abbr title="Only while making use of the server and only with relation to data subjects actively connected. In the case of historical data (replays), only when this condition would have been true at the time.">Players</abbr></div> | ✅ | <abbr title="While no direct access is given, an accurate and current SS14 name can be uniquely related to an SS14 ID by means of querying the authentication server not operated by Sector Umbra."></abbr> | | ✅ | | | |

## IPIntel API

As of the 24th of January 2025, the Sector Umbra game server codebase has the ability to perform automatic IPIntel checking with IP addresses of connecting clients. Sector Umbra does not use this functionality, and connecting IP addresses are explicitly not shared with this third party.

# How long is this data retained after processing?

This is defined per-purpose. If multiple retention periods apply of which at least one has not expired, data is still retained but the data will not be used for purposes whose retention period has expired. If all applicable retention periods expire, <abbr title="Depending on the type of data stored, scanning and removal of this data is expensive, and is only done every week.">the server will require at most **an additional 7 days** to fully remove the data from disk due to technical constraints</abbr>. Data considered to be deleted will not show up in backups.

<br>

Retention periods:

1. **Game server operation:** Not retained after functional purpose (= maintaining the connection and permitted the user to play) ends.
2. **Game server rules enforcement:** Retained for 1 year after the connection that provided the information ends. Admin notes and bans are retained for 1 year after issuing and after expiring respectively.
3. **Website operation:** Not retained after connection ends.
4. **Wiki accounts:** Retained for as long as the wiki account is relevant. Accounts can be deleted on request.
5. **Round replays:** Retained for 2 months after the replay is recorded, deleted afterwards.
6. **Patreon donations:** Retained by Patreon for as long as Patreon deems the retention relevant. Sector Umbra is not able to delete information on request, these requests should be directed to Patreon instead. We do not store personal data used for this purpose outside of Patreon.

# Disclosure on third-party sharing of information.

The following third-parties have access to personal data under the conditions defined:

- <abbr title="Currently, the following servers are considered reputable: RMC-14, Delta-V, Cosmatic Drift, Harmony, Suspicion on Space Station">**Administration of other reputable servers:**</abbr> On manual request made to a Project Manager or above, information can be shared about whether or not we have seen a player before, and a general description of the player's records (if any) can be provided for the purposes of allowing these servers to make informed decisions regarding rule enforcement within their jurisdiction. A record of these transactions is maintained, and data subjects have the right to insight in these transactions.
- **Hetzner Gmbh (DE):** This party automatically processes all personal data related to purposes 1, 2, 3, 4 and 5 as they host our server. A <abbr title="A Data Processing Agreement is a formal contract between two parties that allows a Data Controller to supply data to a third-party Data Processor for processing based on a business need or necessity. The Data Processor must inform the Data Controller of a data breach that happened on their behalf.">Data Processing Agreement</abbr> has been made on the 13th of November 2024 between Sector Umbra (the Client) and Hetzner Gmbh (the Supplier). Insight into this document is available on request.
- **Patreon Inc:** This party is the Data Controller of all personal data related to purpose 6. We are a Data Processor of this personal data. No specific Data Processing Agreement is available, but a generalised Data Processing Agreement is available on Patreon's website.
