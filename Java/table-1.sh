for f in $(tail -n +2 nio-tests.csv | cut -d, -f-3 | sort -u ); do
    mid=$(grep ,$f$ nio-module-list.csv | cut -d, -f1)
    slug=$(echo $f | cut -d, -f1);
    sha=$(echo $f | cut -d, -f2);
    module=$(echo $f | cut -d, -f3);
    modified_slug_module="$(echo $(echo ${slug} | rev | cut -d'/' -f1-2 | rev) | tr '[:upper:]' '[:lower:]') - $(echo ${module} | cut -d'.' -f2- | rev | cut -d'/' -f1 | rev)";

    idm=$(grep ^$f, nio-tests.csv | cut -d, -f5 | grep "nonIdemPass" | wc -l)
    idc=$(grep ^$f, nio-tests.csv | cut -d, -f6 | grep "nonIdemPass" | wc -l)
    ids=$(grep ^$f, nio-tests.csv | cut -d, -f7 | grep "nonIdemPass" | wc -l)

    idmt=$(grep ^$f, nio-mod-time.csv | cut -d, -f11)
    idct=$(grep ^$f, nio-mod-time.csv | cut -d, -f9)
    idst=$(grep ^$f, nio-mod-time.csv | cut -d, -f7)
    idsidm=$(printf %.1f $(grep ^$f, nio-mod-time.csv | cut -d, -f4))
    idcidm=$(printf %.1f $(grep ^$f, nio-mod-time.csv | cut -d, -f5))
     # & ${sha:0:7}
    echo "$mid & $modified_slug_module & $idm & $idc & $ids & $idmt & $idct & $idst & $idcidm & $idsidm \\\\"
done
