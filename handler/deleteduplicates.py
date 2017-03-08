from jamaclient import JamaClient
import json


class Delete_Duplicates():
    def __init__(self):
        self.deleted_list = {}
        self.ignore_list = {}
        self.deleted_item_counter = 0
        self.ignored_item_counter = 0
        self.jamaClient = JamaClient()

    def delete(self, rows):
        for row in rows:
            item = self.jamaClient.get_item_for_documentkey(row)
            if item != None:
                if self.stripString(str(rows.get(row))) != self.stripString(item["fields"]["name"]):
                # if str(rows.get(row)).strip("]").strip("[").__contains__(item["fields"]["name"]) == False:
                    self.ignore_list.__setitem__(row, item)
                    print("Name from csv file did not match retrieved item's name. Item with documentKey: " + row + " will not be deleted.")
                    self.ignored_item_counter = self.ignored_item_counter + 1
                else:
                    self.deleted_list.__setitem__(row, item)
                    print("deleting item with id: " + str(item["id"]) + " and documentKey: " + row)
                    if self.jamaClient.delete_item(item["id"]) == True:
                        self.deleted_item_counter = self.deleted_item_counter + 1


        print("Total number of items deleted: " + str(self.deleted_item_counter))
        print("ToTal number of items ignored: " + str(self.ignored_item_counter))

        if self.ignored_item_counter > 0:
            with open('ignored_items.json', 'wb') as fp:
                json.dump(self.ignore_list, fp)

        if self.deleted_item_counter > 0:
            with open("deleted_items.json", "wb") as fp:
                json.dump(self.deleted_list, fp)


    def stripString(self, row):
        return row.replace("\"", "").replace("\'", "").replace("[", "").replace("]", "").replace("\\\\", "")
