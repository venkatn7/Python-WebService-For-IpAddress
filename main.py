from flask import Flask, jsonify, render_template, request
import re
import os, socket

app = Flask(__name__)


@app.route('/_Ping_nodes')
def Ping_nodes():
    a = request.args.get('a', 0, type=str)

    def buffer_data():
        store_data = []
        with open("Bufferfile.txt", 'w', encoding='utf-8') as infile:
            for line in a:
                textdata = infile.write(line.strip(''))
                print("Line Printed." + str(line))
        with open("Bufferfile.txt", 'r', encoding='utf-8') as infile1:
            for row in infile1.read().split():
                match1 = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)", row)
                if match1:
                    ip = match1.group(0)
                    x = os.system("ping -c 1 " + ip)
                    if x == 0:
                        store_data.append(row + "--Active" + "\n")
                    else:
                        store_data.append(row + "--Inactive" + "\n")
            return ("".join(store_data))
            print("complete")

    return jsonify(result=buffer_data())

@app.route('/_Nslookup')
def Nslookup():
    a = request.args.get('a', 0, type=str)

    def buffer_data():
        store_data = []
        with open("Bufferfile.txt", 'w', encoding='utf-8') as infile:
            for line in a:
                textdata = infile.write(line.strip(''))
                print("Line Printed." + str(line))
        with open("Bufferfile.txt", 'r', encoding='utf-8') as infile1:
            for row in infile1.read().split():
                match1 = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)", row)
                if match1:
                    ip = match1.group(0)
                    x = socket.getfqdn(ip)
                    if x != 0:
                        store_data.append(ip +" -- " + x + "\n")
                    else:
                        pass
            return ("".join(store_data))
            print("complete")

    return jsonify(result=buffer_data())


@app.route('/')
def index():
    return render_template('test3.html')


if __name__ == '__main__':
    app.run(debug=True)
