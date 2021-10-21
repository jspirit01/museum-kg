import json

db_dir = "../datasets/"
db_file = "museum.json"
with open(db_dir + db_file, encoding='utf-8') as json_file:
    json_data = json.load(json_file)


last_id = json_data["nodes"][-1]["id"]  # find the last id in current database

def createNewNode(shape="circularImage", image="", label=""):
    
    new_node = {
        "id": int(last_id)+1,
        "shape": shape,
        "image": image,
        "label": label
    }
    
    json_data["nodes"].append(new_node)
    return json_data["nodes"]

def createNewLink(from_node_id=None, to_node_id=None, label=""):
    if from_node_id == None or to_node_id == None:
        print("[Error] node id can not be null.")
    new_link = {
        "from": str(from_node_id),
        "to": str(to_node_id),
        "label": label
    }
    
    json_data["links"].append(new_link)
    return json_data["links"]

def writeChanges(filename="new_database.json", json_data=None, new_nodes=None, new_links=None):
    if json_data == None:
        print("[Error] the json data is null.")
    if new_nodes != None:
        json_data["nodes"] = new_nodes
    if new_links != None:
        json_data["links"] = new_links

    with open(db_dir + filename, 'w', encoding='UTF8') as out_file:
        json.dump(json_data, out_file, indent=4, ensure_ascii=False)



def i_createNewNode(shape="circularImage", image="../imgs/학무늬베개/", label=""):
    global last_id
    while True:
        label = input("label: ")
        if label == 'q': break
        last_id = int(last_id) + 1
        new_node = {
            "id": str(last_id),
            "shape": shape,
            "image": image,
            "label": label
        }
        
        json_data["nodes"].append(new_node)

    res = input("Do you want to save? [y/n] : ")
    if res in ['y', "Y"]:
        writeChanges(json_data=json_data, new_nodes=json_data["nodes"])   
    else:
        print("No save, nothing changes.")
    return 0

def i_createNewLink(from_node_id=None, to_node_id=None, label=""):
    if from_node_id == None or to_node_id == None:
        print("[Error] node id can not be null.")
    new_link = {
        "from": str(from_node_id),
        "to": str(to_node_id),
        "label": label
    }
    
    json_data["links"].append(new_link)
    return json_data["links"]



# newNode = createNewNode()
# newLink = createNewLink(4, 2)
# writeChanges("new_database.json", json_data, newNode, newLink)
i_createNewNode()
