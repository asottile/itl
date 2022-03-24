[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/itl/main.svg)](https://results.pre-commit.ci/latest/github/asottile/itl/main)

itl
===

Load an iTunes Music Library and produce some "interesting" statistics.

1. [Enable the `xml` library file](https://support.apple.com/en-us/HT201610)
2. `python itl.py`

Here's the output for my library:

```console
$ python itl.py
===============================================================================
Total listening time: 467 Days, 15 Hours, 24 Minutes, 58 Seconds
===============================================================================
Top artists (by play time)
===============================================================================
1. The All-American Rejects: 72 Days, 5 Hours, 29 Minutes, 33 Seconds
2. Yellowcard: 57 Days, 17 Hours, 32 Minutes, 2 Seconds
3. Hollywood Undead: 41 Days, 18 Hours, 15 Minutes, 57 Seconds
4. twenty one pilots: 40 Days, 3 Hours, 30 Minutes, 55 Seconds
5. Anberlin: 38 Days, 6 Hours, 40 Minutes, 36 Seconds
6. blink-182: 36 Days, 4 Hours, 43 Minutes, 14 Seconds
7. Relient K: 34 Days, 19 Hours, 23 Minutes, 14 Seconds
8. Manchester Orchestra: 18 Days, 8 Hours, 9 Minutes, 43 Seconds
9. Taking Back Sunday: 9 Days, 16 Hours, 23 Minutes, 8 Seconds
10. Dashboard Confessional: 9 Days, 5 Hours, 32 Minutes, 19 Seconds
===============================================================================
Top songs (by count)
===============================================================================
1. [The All-American Rejects] One More Sad Song: 542
2. [The All-American Rejects] Drive Away: 525
3. [The All-American Rejects] Sierra's Song: 523
4. [Hollywood Undead] This Love, This Hate: 512
5. [The All-American Rejects] Don't Leave Me: 510
6. [The All-American Rejects] Too Far Gone: 481
7. [The All-American Rejects] The Cigarette Song: 469
8. [The All-American Rejects] Fallin' Apart: 468
9. [The All-American Rejects] I Wanna: 467
10. [The All-American Rejects] Bite Back (B-Side): 463
11. [blink-182] Down: 461
12. [Relient K] Which To Bury, Us Or The Hatchet: 454
13. [The All-American Rejects] The Last Song: 453
14. [The All-American Rejects] Gives You Hell: 442
15. [Hollywood Undead] Coming Back Down: 435
16. [blink-182] Feelin' this: 434
17. [Hollywood Undead] City: 433
18. [Hollywood Undead] Pain (Bonus Track): 432
19. [Anberlin] You Belong Here: 432
20. [The All-American Rejects] Can't Take It: 424
21. [Anberlin] Adelaide: 420
22. [Hollywood Undead] No 5: 420
23. [Hollywood Undead] Black Dahlia: 417
24. [Hollywood Undead] Pour Me: 415
25. [The All-American Rejects] It Ends Tonight: 414
===============================================================================
Top songs (by play time)
===============================================================================
1. [Anberlin] *(fin): 1 Day, 19 Hours, 30 Minutes, 28 Seconds
2. [The All-American Rejects] The Last Song: 1 Day, 13 Hours, 48 Minutes, 16 Seconds
3. [The All-American Rejects] Sierra's Song: 1 Day, 12 Hours, 55 Minutes, 39 Seconds
4. [Relient K] When I Go Down: 1 Day, 12 Hours, 55 Minutes, 35 Seconds
5. [The All-American Rejects] Bite Back (B-Side): 1 Day, 11 Hours, 50 Minutes, 38 Seconds
6. [Anberlin] Depraved: 1 Day, 9 Hours, 45 Minutes, 16 Seconds
7. [Hollywood Undead] This Love, This Hate: 1 Day, 9 Hours, 44 Minutes, 2 Seconds
8. [The All-American Rejects] Too Far Gone: 1 Day, 8 Hours, 39 Minutes, 5 Seconds
9. [The All-American Rejects] Drown Next to Me: 1 Day, 8 Hours, 31 Minutes, 42 Seconds
10. [Relient K] Which To Bury, Us Or The Hatchet: 1 Day, 7 Hours, 47 Minutes, 1 Second
11. [30 Seconds to Mars] Kings and Queens: 1 Day, 7 Hours, 34 Minutes, 22 Seconds
12. [Anberlin] You Belong Here: 1 Day, 7 Hours, 27 Minutes, 23 Seconds
13. [Anberlin] Art Of War: 1 Day, 7 Hours, 22 Minutes, 9 Seconds
14. [Manchester Orchestra] The River: 1 Day, 6 Hours, 38 Minutes, 51 Seconds
15. [The All-American Rejects] Don't Leave Me: 1 Day, 6 Hours, 8 Minutes, 28 Seconds
16. [blink-182] Always: 1 Day, 4 Hours, 50 Minutes, 41 Seconds
17. [Sum 41] Walking Disaster: 1 Day, 4 Hours, 43 Minutes
18. [The All-American Rejects] It Ends Tonight: 1 Day, 4 Hours, 9 Minutes, 17 Seconds
19. [The All-American Rejects] The Cigarette Song: 1 Day, 4 Hours, 4 Minutes, 46 Seconds
20. [Hollywood Undead] Pour Me: 1 Day, 4 Hours, 1 Minute, 2 Seconds
21. [The All-American Rejects] One More Sad Song: 1 Day, 3 Hours, 57 Minutes, 39 Seconds
22. [Taking Back Sunday] This Is All Now: 1 Day, 3 Hours, 48 Minutes
23. [The All-American Rejects] Back to Me: 1 Day, 3 Hours, 47 Minutes, 3 Seconds
24. [The All-American Rejects] When the Wind Blows: 1 Day, 3 Hours, 45 Minutes, 18 Seconds
25. [Anberlin] Dismantle.Repair: 1 Day, 3 Hours, 36 Minutes, 17 Seconds
```
