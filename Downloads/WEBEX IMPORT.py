import requests 
import json 

access_token = "NzE4MDYyODctODNmOC00MTU5LWJlZDEtNjJiYzI2NzFmY2VlMTdjYjdjMDMtZjJh_P0A1_71b6b34c-abff-4407-ac50-5e62323aed80"

groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "GROUP_1" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Thomas", "email": "thomas.vankerckhoven2@student.odisee.be"},
                     {"person_id": "P-2" , "person_name": "Wilson", "email": "wilson.rukundo@student.odisee.be"},
                     {"person_id": "P-3" , "person_name": "Quentin", "email": "quentin.glineur@student.odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G2" , "group_name": "GROUP_2" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Martin", "email": "thomas.vankerckhoven2@student.odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "Bob", "email": "wilson.rukundo@student.odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alice", "email": "quentin.glineur@student.odisee.be"} 
                   ]     
                 }
      },
      { "group": { "group_id": "G3" , "group_name": "GROUP_3" ,    
                   "members": [   
                     {"person_id": "P-7" ,"person_name": "Matt", "email": "thomas.vankerckhoven2@student.odisee.be"}, 
                     {"person_id": "P-8" ,"person_name": "Lucas", "email": "wilson.rukundo@student.odisee.be"}, 
                     {"person_id": "P-9" ,"person_name": "Elsa", "email": "quentin.glineur@student.odisee.be"} 
                   ] 
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    NEW_SPACE_ID = res_space.json()["id"]
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)
