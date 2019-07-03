# django_20190628
django練習用

todo project : class Based View

board project : method Based View


■必要なものだけではなく、単に現在の状態記録の為に残している
<pre>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
</pre>

<pre>
CVE-2019-12781 詳しい情報
中程度
脆弱なバージョン： > = 2.2.0、<2.2.3
パッチを当てたバージョン： 2.2.3
Djangoの1.11.22より前の1.11、2.1.10より前の2.1、および2.2.3より前の2.2で問題が発見されました。SECURE_PROXY_SSL_HEADERおよびSECURE_SSL_REDIRECTの設定が使用されていて、プロキシがHTTPS経由でDjangoに接続している場合、HTTP要求はHTTPSにリダイレクトされません。つまり、クライアントがHTTPを使用している場合、django.http.HttpRequest.schemeの動作は正しくありません。
</pre>
