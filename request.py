import socket

R_IP = '10.48.30.30'
R_PORT = 5060

message = b"INVITE sip:1002@10.48.30.30:5060 SIP/2.0\r\n" \
          b"Max-Forwards: 61\r\n" \
          b"Via: SIP/2.0/UDP 10.48.52.203:5060;branch=z9hG4bKg3Zqkv7i41d39qocgwqwqr5z1y27d8erj\r\n" \
          b"To: <sip:1002@10.48.30.30>\r\n" \
          b"From: \"Anonymous\" <sip:anonymous@anonymous.invalid>;tag=h7g4Esbg_p65546t1678361086m433915c80467s1_3831292796-1406912277\r\n" \
          b"Call-ID: p65546t1678361086m433915c80467s2\r\n" \
          b"CSeq: 1 INVITE\r\n" \
          b"Contact: <sip:sgc_c@10.48.52.203;transport=udp>\r\n" \
          b"Record-Route: <sip:10.48.52.203;transport=udp;lr>\r\n" \
          b"Accept-Contact: *;+g.3gpp.icsi-ref=\"urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel\"\r\n" \
          b"Min-Se: 900\r\n" \
          b"Privacy: id\r\n" \
          b"Session-Expires: 1800\r\n" \
          b"Supported: timer\r\n" \
          b"Supported: replaces\r\n" \
          b"Supported: 199\r\n" \
          b"Supported: 100rel\r\n" \
          b"Content-Type: application/sdp\r\n" \
          b"Content-Length: 503\r\n" \
          b"Session-ID: c9a39ee1d35802c0bcfcd85f509ad0c8\r\n" \
          b"Allow: REGISTER, REFER, NOTIFY, SUBSCRIBE, INFO, PRACK, UPDATE, INVITE, ACK, OPTIONS, CANCEL, BYE\r\n" \
          b"Accept-Encoding: identity\r\n" \
          b"Accept: application/sdp\r\n" \
          b"\r\n"\
          b"v=0\r\n" \
          b"o=- 839180543226151 1671619438 IN IP4 10.48.52.203\r\n" \
          b"s=Session SDP\r\n" \
          b"c=IN IP4 217.0.5.215\r\n" \
          b"t=0 0\r\n" \
          b"m=audio 16510 RTP/AVP 101 10 0 8 3 4 111 112 5 122 118 123 124 125 126 127 96 7 18 110 117 119 97 9 102 115 116 107\r\n" \
          b"a=rtpmap:101 telephone-event/8000\r\n" \
          b"a=fmtp:101 0-16\r\n" \
          b"a=maxptime:20\r\n" \
          b"a=rtpmap:10 L16/8000\r\n" \
          b"a=rtpmap:0 PCMU/8000\r\n" \
          b"a=rtpmap:8 PCMA/8000\r\n" \
          b"a=rtpmap:3 GSM/8000\r\n" \
          b"a=rtpmap:4 G723/8000\r\n" \
          b"a=fmtp:4 annexa=no\r\n" \
          b"a=rtpmap:111 G726-32/8000\r\n" \
          b"a=rtpmap:112 AAL2-G726-32/8000\r\n" \
          b"a=rtpmap:5 DVI4/8000\r\n" \
          b"a=rtpmap:122 L16/12000\r\n" \
          b"a=rtpmap:118 L16/16000\r\n" \
          b"a=rtpmap:123 L16/24000\r\n" \
          b"a=rtpmap:124 L16/32000\r\n" \
          b"a=rtpmap:125 L16/44000\r\n" \
          b"a=rtpmap:126 L16/48000\r\n" \
          b"a=rtpmap:127 L16/96000\r\n" \
          b"a=rtpmap:96 L16/192000\r\n" \
          b"a=rtpmap:7 LPC/8000\r\n" \
          b"a=rtpmap:18 G729/8000\r\n" \
          b"a=fmtp:18 annexb=no\r\n" \
          b"a=rtpmap:110 speex/8000\r\n" \
          b"a=rtpmap:117 speex/16000\r\n" \
          b"a=rtpmap:119 speex/32000\r\n" \
          b"a=rtpmap:97 iLBC/8000\r\n" \
          b"a=fmtp:97 mode=20\r\n" \
          b"a=rtpmap:9 G722/8000\r\n" \
          b"a=rtpmap:102 G7221/16000\r\n" \
          b"a=fmtp:102 bitrate=32000\r\n" \
          b"a=rtpmap:115 G7221/32000\r\n" \
          b"a=fmtp:115 bitrate=48000\r\n" \
          b"a=rtpmap:116 G719/48000\r\n" \
          b"a=fmtp:116 bitrate=64000\r\n" \
          b"a=rtpmap:107 opus/48000/2\r\n" \
          b"a=sendrecv\r\n"

def send_packet():
   with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
       s.connect((R_IP , R_PORT)) 
       s.sendall(message)                                       

send_packet()