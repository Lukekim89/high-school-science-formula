# main.py - 고등학교 과학 공식 모음 실행 스크립트
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# index.html 파일이 이미 존재하면 로드하고, 없으면 자동으로 생성합니다.
def get_html_content():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    else:
        # index.html 파일이 생성되어 있지 않은 경우 기본 안내 메시지
        return """<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>고등학교 과학 공식 모음</title></head>
<body>
  <h2>index.html 파일이 필요합니다.</h2>
  <p>저장소에 생성된 index.html 파일을 포함시켜 주세요.</p>
</body>
</html>"""

def run_server():
    # index.html 존재 확인
    if not os.path.exists("index.html"):
        print("💡 index.html 생성 중...")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(get_html_content())

    Handler = http.server.SimpleHTTPRequestHandler
    
    # 포트 충돌 방지 옵션 적용
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"🚀 웹 서버가 실행되었습니다: {url}")
        print("종료하려면 터미널에서 Ctrl+C 를 누르세요.")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")

if __name__ == "__main__":
    run_server()
