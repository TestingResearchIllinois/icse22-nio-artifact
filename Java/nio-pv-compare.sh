test_names="$1"
polluters=$(cat known-polluters.txt new-polluters.txt | sort -u )
nios=$(echo "$test_names" | cut -d, -f4 | sort)
victims=$(cat known-victims.txt new-victims.txt | sort -u )
echo "only nio : $(comm -23 <( echo "$nios" ) <( cat      <( echo "$polluters" ) <( echo "$victims" ) | sort -u ) | wc -l)"
echo "ni&p - v : $(comm -12 <( echo "$nios" ) <( comm -23 <( echo "$polluters" ) <( echo "$victims" ) ) | wc -l)"
echo "ni&p&v   : $(comm -12 <( echo "$nios" ) <( comm -12 <( echo "$polluters" ) <( echo "$victims" ) ) | wc -l)"
echo "ni&v - p : $(comm -12 <( echo "$nios" ) <( comm -13 <( echo "$polluters" ) <( echo "$victims" ) ) | wc -l)"

echo "only p   : $(comm -23 <( comm -13 <( echo "$nios" ) <( echo "$polluters" ) ) <( comm -13 <( echo "$nios" ) <( echo "$victims" ) ) | wc -l)"
echo "p&v - nio: $(comm -12 <( comm -13 <( echo "$nios" ) <( echo "$polluters" ) ) <( comm -13 <( echo "$nios" ) <( echo "$victims" ) ) | wc -l)"
echo "only v   : $(comm -13 <( comm -13 <( echo "$nios" ) <( echo "$polluters" ) ) <( comm -13 <( echo "$nios" ) <( echo "$victims" ) ) | wc -l)"
