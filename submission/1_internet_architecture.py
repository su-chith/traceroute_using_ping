import subprocess

def replicate_tracert(destination):
    ans = []
    ttl = 1
    reached = False
    command0 = f'ping -4 {destination}'
    result0 = subprocess.run(command0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    line0 = result0.stdout.split('\n')
    data0 = line0[2].split(' ')
    ip0 = data0[2][:-1]
    ans = []
    while(not reached):  # Maximum TTL value for tracert
        command = f'ping -4 -n 1 -i {ttl} {destination}'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        lines = result.stdout.split('\n')
        # print(lines)
        data = lines[2].split(" ")
        ip = data[2][:-1]
        # if ip == destination:
        #     reached = True
        if ip == 'out':
            # print('requested time out')
            print(ttl, '*  ', " ", '*  ', " ", '*  ', " ",'Request timed out')
            ans.append([ttl, '* ', '* ', '*','Request timed out'])
        # print(ip, reached)
        else:
            if ip == ip0:
                reached = True
            command2 = f'ping -n 3 {ip}'
            result2 = subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            lines2 = result2.stdout.split('\n')
            # print(lines2)
            packet1 = lines2[2].split(' ')
            time1 = packet1[-2][5:]
            packet2 = lines2[3].split(' ')
            time2 = packet2[-2][5:]
            packet3 = lines2[4].split(' ')
            time3 = packet3[-2][5:]
            if time1 == '':
                time1 = '*  '
            if time2 == '':
                time2 = '*  '
            if time3 == '':
                time3 = '*  '
            print(ttl, time1, " ", time2, " ", time3, " ", ip)
            ans.append([ttl, time1, time2, time3, ip])
        # lines2[3]
        # lines2[4]
        # if len(lines) >= 3:
        #     time_info = lines[-3]
        #     print(f'TTL {ttl}: {time_info}')
        # else:
        #     reached = True
        #     print(f'TTL {ttl}: Request timed out')
        ttl += 1
    return ans

print(replicate_tracert('iitd.ac.in'))
# if __name__ == "__main__":
#     destination = input("Enter the destination IP or domain: ")
#     replicate_tracert(destination)

