from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:#######") # add your your ip_address

#print(client)

db = client["youtubemanager"]
video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def  update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time }}
    )

def  delete_video(video_id):
    video_collection.delete.one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\ Youtube manager App")
        print("1. List all video")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit a video")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the update video id to update: ")
            name = input("Enter the update video name: ")
            time = input("Enter the update video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the update video id to update: 2")
            delete_video(video_id, name, time)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
        

if __name__ == "__main__":
    main()
