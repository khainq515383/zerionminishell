🔍 Step-by-Step Breakdown: Reconstructed PHP Malware Logic
⚠️ NOTE: This is a deobfuscated translation, not live code, and intended only for analysis.

Infected files: index.php, admin.php (at folder infected)

Payload file: admin.php

Clean decrypted downloader/dropper: index.php (decodeINFECTED)

Clean encrypted payload file: payload (decodeINFECTED)

Python Decoder: decode_payload.php (decodeINFECTED)

Webshell file: maliciousPAYLOAD.php 


--------------------( Possible webshell used )--------------------
https://github.com/TheBinitGhimire/Web-Shells/blob/master/PHP/mini.php

--------------------(CVE-2022-35583)--------------------


🔒 What This Script Does (Summary):
| Step | Purpose                                                                 |
| ---- | ----------------------------------------------------------------------- |
| 1    | Obfuscates a garbage string to confuse analysts.                        |
| 2    | Defines indirect function references via `$GLOBALS[...]`.               |
| 3    | Fetches payload from remote attacker server via HTTP.                   |
| 4    | Determines current server path and domain.                              |
| 5    | Optionally removes itself from `index.php` if `?del=my_code` is passed. |
| 6    | Writes `admin.php` (backdoor shell) into the web directory.             |
| 7    | Sends report with path/domain/status to `https://51la.zvo2.xyz/?d=...`. |
| 8    | Optionally clears injected code from index.php to hide presence.        |


🧼 How to Clean:
✅ Delete admin.php and the infected index.php (replace with clean backup).

✅ Scan the entire web root recursively for other infections.

✅ Check crontabs, /tmp, /var/tmp, and /dev/shm for persistence.

✅ Rotate credentials and consider auditing logs for exfiltration or lateral movement.

