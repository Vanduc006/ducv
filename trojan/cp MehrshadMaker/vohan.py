import cv2

# Tạo đối tượng VideoCapture
cap = cv2.VideoCapture(0)

# Lấy kích thước khung hình
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Tạo đối tượng VideoWriter để ghi video
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width,frame_height))

# Đọc và ghi từng khung hình vào file mp4
while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Webcam', frame)
    
    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
out.release()
cv2.destroyAllWindows()


