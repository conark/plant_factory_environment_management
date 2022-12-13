import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'plant-factory-d18f0.appspot.com', # REPLACE WITH YOUR BUCKET ID
    'databaseURL': 'https://plant-factory-d18f0-default-rtdb.europe-west1.firebasedatabase.app/'  # REPLACE WITH YOUR dburl
})

bucket = storage.bucket()

ref = db.reference('/')
home_ref = ref.child('file')

#Uploades file to Fb Storage
def store_file(fileLoc):
    filename=os.path.basename(fileLoc)
    blob = bucket.blob(filename) # Store File in Fb Bucket
    blob.upload_from_filename(fileLoc)

#Pushes File name to Fb Realtime DB
def push_db(fileLoc, time):

    filename=os.path.basename(fileLoc)

    # Push file reference to image in Realtime DB
    home_ref.push({
        'image': filename,
        'timestamp': time}
    )

if __name__ == "__main__":
    f = open("./test.txt", "w")
    f.write("a demo upload file to test Firebase Storage")
    f.close()
    store_file('./test.txt')
    push_db('./test.txt', '12/11/2020 9:00' )