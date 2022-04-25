This is the artifact repository for "Preempting Flaky Tests via Non-Idempotent-Outcome Tests" (accepted at ICSE'22). All the detected Non-Idempotent-Outcome (NIO) tests have been merged into [International Dataset of Flaky Tests (IDoFT)](https://mir.cs.illinois.edu/flakytests/).

This artifact contains the following files:
# For Java
* Java/known-polluters.csv  - List of polluters identified by Lam et al. in their TACAS'21 work [92]. Obtained from the [author's website](http://mir.cs.illinois.edu/winglam/publications/2021/WeiETAL21TACAS.zip)
* Java/known-victims.csv    - List of victims identified by Lam et al. in their TACAS'21 work [92]. Obtained from the [author's website](http://mir.cs.illinois.edu/winglam/publications/2021/WeiETAL21TACAS.zip)
* Java/nio-mod-time.csv      - List of modules that have at least one NIO test and the runtime of the three modes for each module. esR,esT represents the readable formatted time and the time in seconds, respectively, for the entire-suite mode. The formatted time is represented as `<days>-<hours>:<minutes>:<seconds>` (e.g., `1-01:00:00` is 25 hours, aka 90000 seconds)
* Java/nio-module-list.csv   - List module IDs for each module
* Java/nio-pv-compare.sh     - Script to compare the NIO tests we detected to known polluters and victims (Figure 6 for Java)
* Java/nio-status.csv           - List of NIO tests and the submitted status of the PRs for fixing the tests
* Java/nio-tests.csv            - List of NIO tests detected by iDFlakies and confirmed by the ways we described in Section 3.3. `nonIdemPass`, `allpass`, or `allfail` indicate that a test was found to be NIO, passed in all runs, or failed in all runs by iDFlakies (respectively)
* Java/run-all.out             - Expected output from running run-all.sh
* Java/run-all.sh              - Script to generate Table 1, Table 2, and Figure 6 (for Java)
* Java/table-1.sh              - Script to generate Table 1 (for Java)
* Java/table-2.py              - Script to generate Table 2 (for Java)

# For Python
* Python/figure-6.py       - Script to generate Figure 6 (for Python)
* Python/known-victims.csv - List of victims identified by Gruber et al. [41]. Obtained from the [officially released dataset](https://zenodo.org/record/4450435/files/victims_brittles.csv)
* Python/nio-status.csv     - List of NIO tests and the submitted status of the PRs for fixing the tests
* Python/run-all.out       - Expected output from running run-all.sh. Contains Table 1 and Table 2 detailed breakdown for 90 Python projects
* Python/run-all.sh        - Script to generate Table 2 and Figure 6 (for Python)
* Python/table-2.py        - Script to generate Table 2 (for Python)

# Acknowledgments
If you find the dataset useful, please cite our work and our dataset:
```
@inproceedings{WeiETAL22NIO,
    title = {{Preempting Flaky Tests via Non-Idempotent-Outcome Tests}},
    author = {Wei, Anjiang and Yi, Pu and Li, Zhengxi and Xie, Tao and Marinov, Darko and Lam, Wing},
    booktitle = {2022 IEEE/ACM 44th International Conference on Software Engineering (ICSE)},
    year = {2022}
}
@misc{InternationalDatasetofFlakyTests,
    title = {{International Dataset of Flaky Tests (IDoFT)}},
    author = {Lam, Wing},
    year = {2022},
    url = {http://mir.cs.illinois.edu/flakytests}
}
```
