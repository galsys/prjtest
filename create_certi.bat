mkdir certi

rem 루트 인증서 만들기
rem 루트 인증서의 비밀키 만들기 
openssl genrsa -out .\certi\rootca.key 2048

rem 루트 인증서의 키로 인증 요청서를 만들어요.
openssl req -new -key .\certi\rootca.key -out .\certi\rootca.csr -config root.conf

rem 루트 인증서를 발행합니다.
openssl x509 -req -days 3650 -extensions v3_ca -set_serial 1 -in .\certi\rootca.csr -signkey .\certi\rootca.key -out .\certi\rootca.crt -extfile root.conf

rem 만들어진 루트 인증서를 확인합니다.
openssl x509 -text -in .\certi\rootca.crt


openssl genrsa -out .\certi\bsgkorea.com.key 2048

openssl req -new -key .\certi\bsgkorea.com.key -out .\certi\bsgkorea.com.csr -config server.conf

openssl x509 -req -days 1825 -extensions v3_user -in .\certi\bsgkorea.com.csr -CA .\certi\rootca.crt -CAcreateserial -CAkey  .\certi\rootca.key -out .\certi\bsgkorea.com.crt  -extfile server.conf
