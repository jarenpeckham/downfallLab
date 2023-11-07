key=$(hexdump -vn16 -e'4/4 "%08X" 1 "\n"' /dev/urandom)
echo ${key:0:16}${key:16:16} > /tmp/downfallKey.txt
echo "Downfall" > /tmp/downfall.txt
openssl aes-128-cbc -salt -e -in /tmp/downfall.txt -out /tmp/downfall.txt.encrypted -K $key -iv 11111111111111111111111111111111
timeout 2s taskset -c 1 openssl aes-128-cbc -salt -e -in /dev/urandom -out /dev/null -K $key -iv 11111111111111111111111111111111
