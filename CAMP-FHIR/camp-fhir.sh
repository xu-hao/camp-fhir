resources=$(cat table.hbm.xml | grep table | cut -d" " -f 6 | cut -d"=" -f 2 | cut -d\" -f 2)

echo $resources

for resc in $resources
do
    echo $resc
    mkdir -p ../../fhir/$resc
    java -jar target/CAMPFHIR-jar-with-dependencies.jar $resc ../../fhir/$resc 10000 &> $resc.out
done
