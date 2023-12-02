import os, cv2, csv
from deepface import DeepFace
import keras_core as keras

def output_data(output, file, output_obj, image):

    # creating a csv file with header
    with open(f'{output}/{file}.csv', 'w') as csvfile:
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            'file', 'face_id', 'face_rating', 'age', 
            'gender', 'race', 'emotion', 'height'])

    for i, f in enumerate(output_obj):
        face_id = f'ID_{i}'
        x, y, w, h = f['facial_area'].values()

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, face_id, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imwrite(f'{output}/{file}', image)

        with open(f'{output}/{file}.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([
                file, face_id, f['confidence'], f['age'], 
                f['dominant_gender'], f['dominant_race'], 
                f['dominant_emotion'], 'height'])


def face_recognition(input, output):

    for file in os.listdir(input):
        input_img_path = os.path.join(input, file)

        try:
            image = cv2.imread(input_img_path)
            detections = DeepFace.extract_faces(
                image,
                detector_backend = 'retinaface'
            )
            
        except Exception as e:
            print(str(e))

        else:
            output_obj = []
            for d in detections:
                x, y, w, h = d['facial_area'].values()
                detected_face = image[y:y+h, x:x+w]
                
                face_analyze = DeepFace.analyze(
                    img_path = detected_face,
                    enforce_detection = False,
                    detector_backend = 'skip',
                    actions = ['age', 'gender',
                            'race', 'emotion'])

                face_analyze[0]['confidence'] = d['confidence']
                face_analyze[0]['facial_area'] = d['facial_area']
                

                # to make predictions in production, load the model
                loaded_model = keras_core.saving.load_model('model.keras')

                # Use the loaded model to make predictions
                predictions = loaded_model.predict(your_data)


                output_obj.extend(face_analyze)

            output_data(output, file, output_obj, image)


if __name__ == "__main__":

    input = './input'
    output = './output'

    if not os.path.exists(output):
        os.makedirs(output)

    face_recognition(input, output)