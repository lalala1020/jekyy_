
function ping_one(){
    python test_ip.py > out.txt
    cp out.txt ip_list.yml
}

# while [true]
# do 
#     ping_one
#     echo "ping_one"
#     sleep 3
# done

ping_one
echo "ping_one"
