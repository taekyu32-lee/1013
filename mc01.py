import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('picture.jpg')
print(f"세로 : {img.shape[0]}, 가로 : {img.shape[1]}")
results = model(img)
results.save()

print(results)

result = results.pandas().xyxy[0].to_numpy()
print(f"result type = {type(results)}")
print(f"reusult = {result}")
result = [item for item in result if item[6]=='person']
print(f"result-person = {result[0][1]}")
print(f"result-person = {result[1][1]}")


tmp_img = cv2.imread('picture.jpg')
tmp_img_test = cv2.imread('picture.jpg')
# print(tmp_img.shape)
for i,p in enumerate(result):
    cropped = tmp_img[int(result[i][1]):int(result[i][3]), int(result[i][0]):int(result[i][2])]
    print(cropped.shape)
    cv2.imwrite('people'+str(i)+'.png', cropped)
#print(f"rectangle = {results.xyxy[0][0][0]}")

# person만 가져와서 작업
for i,p in enumerate(result):
    cv2.rectangle(tmp_img, (int(result[i][0]), int(result[i][1])), (int(result[i][2]), int(result[i][3])), (255,255,255))
cv2.imwrite('result'+str(i)+'.png', tmp_img)

## xyxy[0] = 'person' ,xyxy[27] = tie  ------  results 에서 바로 작업
# for i,_ in enumerate(result):
#     cv2.rectangle(tmp_img, (int(results.xyxy[0][i][0].item()), int(results.xyxy[0][i][1].item())), (int(results.xyxy[0][i][2].item()), int(results.xyxy[0][i][3].item())), (255,255,255))
#     # cv2.rectangle(tmp_img, (int(result[i][0]), int(result[i][1])), (int(result[i][2]), int(result[i][3])), (255,255,255))
#     # tmp_img = cv2.imread('picture.jpg')
# cv2.imwrite('result.png', tmp_img)

# cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (0,0,255))
# cv2.imwrite('result.png', tmp_img)