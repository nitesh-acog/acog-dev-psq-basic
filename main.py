import requests

url='http://127.0.0.1:8000/api/'


if __name__=='__main__':
    print(requests.post(url,data={'infile':'/Users/nitesh/Documents/Projects/PSQ/acog-dev-psq-basic/data/','outfile':'/Users/nitesh/Documents/Projects/PSQ/acog-dev-psq-basic/datat'}))