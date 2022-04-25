echo "================ Generating Table 1"
bash table-1.sh

echo "================ Generating Table 2"
python3 table-2.py

echo "======== Generating Figure 6 all tests Venn diagram"
bash nio-pv-compare.sh "$(tail -n +2 nio-tests.csv)"

echo "======== Generating Figure 6 fixed tests Venn diagram"
bash nio-pv-compare.sh "$(egrep "Accepted|Rejected|Opened" nio-status.csv)"
