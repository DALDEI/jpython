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
url = 'https://a4dpe303.asl.lab.emc.com:8543/deploymanager/action/deploy'
deploy_payload = {
	"name"				: "proxy51 Indio",
	"hostSystemMoid"	: "host-33",
	"datastoreMoid"		: "datastore-36",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-16",
	"vamiIp"			: "10.6.245.32",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.245.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "ave2.vmwareqa.local",
	"mcsDomain"			: "clients"
}


deploy_payload_proxy10 = {
	"name"				: "proxy10 Harmony",
	"hostSystemMoid"	: "host-801",
	"datastoreMoid"		: "datastore-589",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-597",
	"vamiIp"			: "10.6.244.89",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy11 = {
	"name"				: "proxy11 Harmony",
	"hostSystemMoid"	: "host-696",
	"datastoreMoid"		: "datastore-698",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-597",
	"vamiIp"			: "10.6.244.91",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy16 = {
	"name"				: "proxy16 Harmony",
	"hostSystemMoid"	: "host-583",
	"datastoreMoid"		: "datastore-587",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-597",
	"vamiIp"			: "10.6.244.85",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy17 = {
	"name"				: "proxy17 Harmony",
	"hostSystemMoid"	: "host-851",
	"datastoreMoid"		: "datastore-857",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-597",
	"vamiIp"			: "10.6.244.86",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy18 = {
	"name"				: "proxy18 Harmony",
	"hostSystemMoid"	: "host-854",
	"datastoreMoid"		: "datastore-864",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-597",
	"vamiIp"			: "10.6.244.107",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy22 = {
	"name"				: "proxy22 Harmony",
	"hostSystemMoid"	: "host-118",
	"datastoreMoid"		: "datastore-134",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "DistributedVirtualPortgroup-dvportgroup-245",
	"vamiIp"			: "10.6.244.107",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy26 = {
	"name"				: "proxy26 Harmony",
	"hostSystemMoid"	: "host-118",
	"datastoreMoid"		: "datastore-134",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "DistributedVirtualPortgroup-dvportgroup-245",
	"vamiIp"			: "10.6.244.107",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy27 = {
	"name"				: "proxy27 Harmony",
	"hostSystemMoid"	: "host-123",
	"datastoreMoid"		: "datastore-136",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "DistributedVirtualPortgroup-dvportgroup-245",
	"vamiIp"			: "10.6.244.134",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy48 = {
	"name"				: "proxy48 Harmony",
	"hostSystemMoid"	: "host-123",
	"datastoreMoid"		: "datastore-136",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "DistributedVirtualPortgroup-dvportgroup-245",
	"vamiIp"			: "10.6.244.107",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4ipn452d2.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy50 = {
	"name"				: "proxy50 Harmony",
	"hostSystemMoid"	: "host-33",
	"datastoreMoid"		: "datastore-36",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-16",
	"vamiIp"			: "10.6.245.31",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.245.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4dpe303.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy51 = {
	"name"				: "proxy51 Harmony",
	"hostSystemMoid"	: "host-33",
	"datastoreMoid"		: "datastore-36",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-16",
	"vamiIp"			: "10.6.245.32",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.245.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4dpe303.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

deploy_payload_proxy52 = {
	"name"				: "proxy52 Harmony",
	"hostSystemMoid"	: "host-33",
	"datastoreMoid"		: "datastore-36",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-16",
	"vamiIp"			: "10.6.245.33",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.245.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4dpe303.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}


deploy_payload_proxy7 = {
	"name"				: "proxy7 Harmony",
	"hostSystemMoid"	: "host-33",
	"datastoreMoid"		: "datastore-36",
	"folderMoid"		: None,
	"resourcePoolMoid"	: None,
	"networkMoid"		: "network-17",
	"vamiIp"			: "10.6.244.74",
	"vamiDnsString"		: "10.6.242.33",
	"vamiGateway"		: "10.6.244.1",
	"vamiNetmask"		: "255.255.255.0",
	"mcsAddress"		: "a4dpe303.asl.lab.emc.com",
	"mcsDomain"			: "clients"
}

proxies = [deploy_payload_proxy50,deploy_payload_proxy51,
           deploy_payload_proxy52,deploy_payload_proxy7]

# for proxy in proxies:
# 	print "send post request deploy proxy %s : " % proxy
# 	post_deploy(url,proxy,headers)


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
print "get deployed proxy"
url = 'https://a4dpe303.asl.lab.emc.com:8543/deploymanager/inventory/vm-569'
get_deployed_proxy(url,headers)
