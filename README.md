[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/itl/master.svg)](https://results.pre-commit.ci/latest/github/asottile/itl/master)
itl
===

Load an iTunes Music Library and produce some "interesting" statistics.

1. [Enable the `xml` library file](https://support.apple.com/en-us/HT201610)
2. `python itl.py`

Here's the output for my library:

```console
$ python itl.py
===============================================================================
Total listening time: 409 Days, 2 Hours, 38 Minutes, 51 Seconds
===============================================================================
Top artists (by play time)
===============================================================================
1. The All-American Rejects: 65 Days, 10 Hours, 58 Minutes, 16 Seconds
2. Yellowcard: 49 Days, 23 Hours, 37 Minutes, 13 Seconds
3. Hollywood Undead: 37 Days, 59 Minutes, 10 Seconds
4. twenty one pilots: 34 Days, 21 Hours, 26 Minutes, 5 Seconds
5. Anberlin: 34 Days, 20 Hours, 2 Minutes, 6 Seconds
6. blink-182: 30 Days, 23 Hours, 57 Minutes, 14 Seconds
7. Relient K: 30 Days, 3 Hours, 21 Minutes, 41 Seconds
8. Manchester Orchestra: 16 Days, 11 Minutes, 36 Seconds
9. Taking Back Sunday: 8 Days, 21 Hours, 56 Minutes, 1 Second
10. Dashboard Confessional: 7 Days, 11 Hours, 43 Minutes, 12 Seconds
===============================================================================
Top songs (by count)
===============================================================================
1. [The All-American Rejects] One More Sad Song: 484
2. [The All-American Rejects] Sierra's Song: 480
3. [Hollywood Undead] This Love, This Hate: 480
4. [The All-American Rejects] Drive Away: 464
5. [The All-American Rejects] Don't Leave Me: 458
6. [The All-American Rejects] Too Far Gone: 434
7. [The All-American Rejects] I Wanna: 432
8. [blink-182] Down: 430
9. [The All-American Rejects] The Cigarette Song: 426
10. [Hollywood Undead] Coming Back Down: 426
11. [Relient K] Which To Bury, Us Or The Hatchet: 421
12. [The All-American Rejects] The Last Song: 420
13. [The All-American Rejects] Bite Back (B-Side): 416
14. [The All-American Rejects] Fallin' Apart: 415
15. [Hollywood Undead] No 5: 403
16. [Hollywood Undead] City: 401
17. [The All-American Rejects] Gives You Hell: 398
18. [blink-182] Feelin' this: 397
19. [The All-American Rejects] It Ends Tonight: 396
20. [Hollywood Undead] Pain (Bonus Track): 393
21. [The All-American Rejects] Damn Girl: 392
22. [The All-American Rejects] Can't Take It: 390
23. [Linkin Park] Waiting For The End: 388
24. [Taking Back Sunday] This Is All Now: 388
25. [Anberlin] Adelaide: 387
===============================================================================
Top songs (by play time)
===============================================================================
1. [Anberlin] *(fin): 1 Day, 17 Hours, 25 Minutes, 18 Seconds
2. [The All-American Rejects] The Last Song: 1 Day, 11 Hours, 3 Minutes, 2 Seconds
3. [The All-American Rejects] Sierra's Song: 1 Day, 9 Hours, 53 Minutes, 29 Seconds
4. [Relient K] When I Go Down: 1 Day, 9 Hours, 20 Minutes, 44 Seconds
5. [The All-American Rejects] Bite Back (B-Side): 1 Day, 8 Hours, 12 Minutes, 19 Seconds
6. [Anberlin] Depraved: 1 Day, 7 Hours, 40 Minutes, 43 Seconds
7. [Hollywood Undead] This Love, This Hate: 1 Day, 7 Hours, 37 Minutes, 32 Seconds
8. [The All-American Rejects] Drown Next to Me: 1 Day, 6 Hours, 55 Minutes, 29 Seconds
9. [Relient K] Which To Bury, Us Or The Hatchet: 1 Day, 5 Hours, 28 Minutes, 24 Seconds
10. [The All-American Rejects] Too Far Gone: 1 Day, 5 Hours, 27 Minutes, 54 Seconds
11. [Anberlin] Art Of War: 1 Day, 5 Hours, 14 Minutes, 28 Seconds
12. [30 Seconds to Mars] Kings and Queens: 1 Day, 4 Hours, 52 Minutes, 9 Seconds
13. [Anberlin] You Belong Here: 1 Day, 4 Hours, 10 Minutes, 47 Seconds
14. [The All-American Rejects] Don't Leave Me: 1 Day, 3 Hours, 2 Minutes, 43 Seconds
15. [The All-American Rejects] It Ends Tonight: 1 Day, 2 Hours, 55 Minutes, 51 Seconds
16. [Sum 41] Walking Disaster: 1 Day, 2 Hours, 38 Minutes, 54 Seconds
17. [Taking Back Sunday] This Is All Now: 1 Day, 2 Hours, 14 Minutes, 40 Seconds
18. [The All-American Rejects] Back to Me: 1 Day, 2 Hours, 8 Minutes, 28 Seconds
19. [blink-182] Always: 1 Day, 2 Hours, 7 Minutes, 29 Seconds
20. [Hollywood Undead] Pour Me: 1 Day, 2 Hours, 3 Minutes, 34 Seconds
21. [The All-American Rejects] When the Wind Blows: 1 Day, 2 Hours, 24 Seconds
22. [Manchester Orchestra] The River: 1 Day, 1 Hour, 53 Minutes, 21 Seconds
23. [The All-American Rejects] The Cigarette Song: 1 Day, 1 Hour, 30 Minutes, 18 Seconds
24. [The All-American Rejects] Another Heart Calls: 1 Day, 1 Hour, 19 Minutes, 6 Seconds
25. [The All-American Rejects] Eyelash Wishes [*]: 1 Day, 1 Hour, 16 Minutes, 19 Seconds
```
