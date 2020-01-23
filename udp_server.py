import asyncore
import socket

class UdpServer(asyncore.dispatcher):

    def __init__(self):
        asyncore.dispatcher.__init__(self)

        # 5000 番ポートにバインド
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(('192.168.170.58', 51452))
        return

    # ポートにバインドされた時
    def handle_connect(self):
        print ('Udp server Started...')
        return

    # データが飛んできた時
    def handle_read(self):
        data, addr = self.recvfrom(1024)

        # 特定のデータが飛んできたら終了
        if data == False:
            raise asyncore.ExitNow('Server is quitting!')
        return


    def handle_write(self):
        pass


# 例外をキャッチする．サーバー終了後に，何かしらの処理をしたい用
def run():
    instance = UdpServer() 
    try:
        asyncore.loop()    # 非同期ループを開始
    except asyncore.ExitNow as e:
        print (e)


if __name__ == '__main__':
    run()
