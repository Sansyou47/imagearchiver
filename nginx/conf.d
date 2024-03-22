server {
   # 80番ポートを開放する
   listen 80;
   
   # "/"から始まるURIに{}内の設定を適用する
   location / {   
       # uwsgiのパラメータを読み込む
       include uwsgi_params;
       # uwsgiとの通信に用いるソケットファイルを指定する(パスは任意)
       uwsgi_pass unix:///tmp/uwsgi.sock;
   }
}
