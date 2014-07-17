#!/usr/bin/python
import urllib2,json,requests

def post_deploy(url,deploy_payload,headers):
	# work
	response = requests.post(url,data=json.dumps(deploy_payload),headers=headers,verify=False)
	print response.status_code
	print response.text

def get_task_status(url,headers):	
	# https://ave:8543/deploymanager/task/job-sdf...
    response = requests.get(url,headers=headers,verify=False)

def get_deployed_proxy(url,headers):
	# work
	# url https://ave:8543/deploymanager/inventory/{proxyId}
	response = requests.get(url,headers=headers,verify=False)
	json_data = response.json()
	print json_data

def get_check_health(url,headers):
	# work
	# url https://ave:8543/deploymanager/inventory/{proxyId}/health
	response = requests.get(url,headers=headers,verify=False)
	print response.text

def post_change_password(url,change_password_payload,headers):
	# url https://ave:8543/deploymanager/inventory/{proxyId}/action/changePassword
	response = requests.post(url,change_password_payload,headers,verify=False)

def post_delete(url,headers):
	#work
    # url https://ave:8543/deploymanager/inventory/{proxyId}/action/delete
    response = requests.post(url,headers=headers,verify=False)	

def post_cancel(url,cancel_payload,headers):
	# url https://ave:8543/deploymanager/task/job---/action/cancel
	response = requests.post(url,cancel_payload,headers,verify=False)

def post_initialize(url,initialize_payload,headers):
	# work
	# url https://ave:8543/deploymanager/inventory/{proxyId}/action/initialize
	response = requests.post(url,data=json.dumps(initialize_payload),headers=headers,verify=False)
	print response.status_code
# if __name__ == "__main__":

headers = {
	"Accept"		: 'application/json',
	"Content-Type"	: 'application/json'
}	

# url = 'https://ave2.vmwareqa.local:8543/deploymanager/action/deploy'
# url = 'https://a4ipn452d2.asl.lab.emc.com:8543/deploymanager/action/deploy'
url = 'https://ave5.irvineqa.local:8543/deploymanager/action/deploy'

try:
	json_file = open("../json/proxy1.js")
except IOError as e:
	print "cannot open file"

try:
	json_data = json.load(json_file)
except IOError as e:
	print e

for proxy in json_data:
    print "deploy proxy " , proxy
    post_deploy(url,proxy,headers)

# print (json_data)

json_file.closed

# post_deploy(url,json_data,headers)

# for proxy in json_data:
# 	print "send post request deploy proxy %s \n" % proxy
	# post_deploy(url,proxy,headers)


########################## deploy proxy ################
# print "send post request deploy proxy\n"
# post_deploy(url,deploy_payload,headers)

########################## initialize proxy ##############
# print "initialize proxy"
# url = 'https://ave2.vmwareqa.local:8543/deploymanager/inventory/vm-557/action/initialize'
# initialize_payload = {
# 	"mcsAddress"	: "ave2.vmwareqa.local",
# 	"mcsDomain"		: "clients"
# }
# post_initialize(url,initialize_payload,headers)

#################### delete proxy #################
#print "delete proxy from vSphere"
# url = 'https://ave2.vmwareqa.local:8543/deploymanager/inventory/vm-219/action/delete'


#post_delete(url,headers)

################### health check proxy #############
# print "check health proxy"
# url = 'https://a4ipn452d2.asl.lab.emc.com:8543/deploymanager/inventory/vm-1128/health'
# get_check_health(url,headers)

################### view deployed proxy #############
# print "get deployed proxy"
# url = 'https://a4dpe303.asl.lab.emc.com:8543/deploymanager/inventory/vm-569'
# get_deployed_proxy(url,headers)
