import ultralytics


class AcceptModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parent_path = "/".join(self.file_path.split("\\")[:-1])
        self.model = ultralytics.YOLO(self.parent_path + '/best.pt')

    def predict(self, image_path):
        pred = self.model(image_path, verbose=False);
        if len(pred[0]) == 0:
            return "Accept button wasn't found"
        else:
            return pred[0].boxes.xyxy.tolist()[0]
