import requests


class AnalyzeResponse:
    def __init__(self, link: str, timeout: int = 5):
        self.response = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://example.com',
            'Referer': 'https://example.com/',
            'Cookie': 'session=abc123',
            'X-CSRF-Token': 'token123',
            'X-Requested-With': 'XMLHttpRequest',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Authorization': 'Bearer token123',
            'API-Key': 'key123',
            'DNT': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }
        try:
            self.link = link
            self.timeout = timeout
            if len(self.link) == 0:
                raise ValueError
        except (TypeError, ValueError):
            self.link = "https://api.agify.io?name=alex"

    @property
    def get_response(self):
        return self.response.get(self.link, timeout=self.timeout, headers=self.headers)

    @property
    def status_code_get_response(self):
        return self.get_response.status_code

    @property
    def _headers_get_response(self):
        return self.response.headers

    @property
    def _user_agent_get_response(self):
        return self._headers_get_response["User-Agent"]

    @property
    def _accept_encoding_get_response(self):
        return self._headers_get_response["Accept-Encoding"]

    @property
    def _accept_get_response(self):
        return self._headers_get_response["Accept"]

    @property
    def _connection_get_response(self):
        return self._headers_get_response["Connection"]

    @property
    def _auth_required_get_response(self):
        if self.get_response in (401, 403):
            return True
        return False

    def text_get_response(self):
        return self.get_response.text

    def __str__(self):
        return (f"Link: {self.link}\n"
                f"Status Code: {self.status_code_get_response}\n"
                f"User-Agent: {self._user_agent_get_response}\n"
                f"Accept-Encoding: {self._accept_encoding_get_response}\n"
                f"Accept: {self._accept_get_response}\n"
                f"Connection: {self._connection_get_response}\n"
                f"Auth: {self._auth_required_get_response}\n")

    def __del__(self):
        print("\nThe class has completed its work completely and the requests have stopped working")

if __name__ == "__main__":
    try:
        analyze_response = AnalyzeResponse("", 4)
        print(analyze_response)
        print(analyze_response.text_get_response())
    except Exception as e:
        print(str(e))
