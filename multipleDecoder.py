from struct import * 


#def encode(motion):
#	return unpack('>i', pack('>f', motion))[0]

def decode(enc):
	return unpack('>f', pack('>i',enc))
encodedYaw=list()
decodedYaw=list()


f=open("yaw_encoded")
while(f.readline()!=""):
	encodedYaw.append(f.readline())

"""
#output to file test
f=open("what.txt","w")
for x in range(len(encodedYaw)):
	f.write(encodedYaw[x])
#print test
for x in range(len(encodedYaw)):
	print(encodedYaw)
"""

#decode that doesnt work
for x in range(len(encodedYaw)):
	decodedYaw.append(str(decode(int(encodedYaw[x]))))#but why
#file output that works
f=open("yaw_decoded","w")
for x in range(len(decodedYaw)):
	f.write(decodedYaw[x]+"\n")

#motion = -0.5
#motion = 1009342213
#yaw = decode(motion)
#print(yaw)



