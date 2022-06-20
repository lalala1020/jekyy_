
function ping_one(){
    python test_ip.py > out.txt
    cp out.txt ip_list.yml
}

ping_one
echo "ping_one"
