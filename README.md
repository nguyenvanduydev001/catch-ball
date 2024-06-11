# Bắt bóng
Một trò chơi thị giác máy tính đơn giản được phát triển bởi Mediapipe, openCV và Pygame

# Cách chạy
**Chuẩn bị môi trường sẵn sàng bằng các bước dưới đây:**<br>
1- Cài đặt [python 3.10 and pip](https://www.python.org/) trên máy tính của bạn<br>
2- Clone dự án trên máy tính của bạn hoặc bạn có thể tải xuống mã từ liên kết GitHub ở trên và đặt nó vào hệ thống của bạn<br>
3-  Mở Terminal của bạn và  pip install mediapipe, pygame, cv2 and cvzone<br>
4- Mở ứng dụng Terminal của bạn trong thư mục Root của dự án và chạy main.py: `python main.py`<br>
5- Chơi trò chơi
## Demo
![demo](/images/demo.png)

# Cách chơi
Trong trò chơi, hãy cố gắng bắt Bóng bằng tay (không quan trọng là bóng nào), vì vậy hãy mở bàn tay của bạn ra và khi một quả bóng lọt vào tay bạn, hãy cố gắng đóng nó lại ngay lập tức.
# Soloution for possible errors
1. Bạn phải có webcam để chơi trò chơi này hoặc bạn có thể sử dụng điện thoại thông minh của mình làm webcam<br>
1. Bạn cần thay đổi ID webcam của mình và đặt thành 0 hoặc nếu không thể thay đổi ID camera, bạn có thể mở tệp main.py và ở dòng 10 thay đổi ID, đặt nó trên ID webcam của bạn<br>
1. Kiểm tra hướng của webcam và đảm bảo rằng nó không bị lộn ngược hoặc phản chiếu hình ảnh của bạn dưới dạng gương (điều đó sẽ khiến hình ảnh bàn tay trong trò chơi di chuyển theo hướng ngược lại với bàn tay thật của bạn)<br>
1. Trong trường hợp thiếu một thư viện cụ thể, hãy đảm bảo thư viện nào bị thiếu và thử Cài đặt nó (có thể là bất kỳ một trong những "cvzone, mediapipe, opencv và pygame")<br>
1. Nếu bạn gặp sự cố khi chơi trò chơi, chẳng hạn như tốc độ giảm hoặc trò chơi không hoạt động bình thường, hãy thử khởi động lại trò chơi để có thể giải quyết được sự cố.<br>
   
[Live demo]()

