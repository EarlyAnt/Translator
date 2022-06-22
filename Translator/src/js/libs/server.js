!function () {
    var $ = {}
    var SERVER = {}
    window.$ = $;

    function getServerURL() {
        return 'https://translate.google.com/translate_a/t?';
    }

    //封装统一请求
    async function request(params) {
        const url = params.url;
        const method = params.method || 'GET';

        let headers = {
            "Content-Type": "application/json"
        };
        if (params.headers) {
            for (let item in params.headers) {
                headers[item] = params.headers[item];
            }
        }

        let data = {};
        if (params.data) {
            for (let item in params.data) {
                data[item] = params.data[item];
            }
        }

        let body;
        if (headers['Content-Type'] == 'application/json') {
            body = JSON.stringify(data);
        } else if (headers['Content-Type'] == 'application/x-www-form-urlencoded') {
            let bodys = [];
            for (let item in data) {
                bodys.push(item + '=' + data[item]);
            }
            body = bodys.join("&");
        }

        console.log("method:" + method + ", url: " + url);
        console.log(headers);
        // console.log(data);
        // console.log(body);

        if (method.toLowerCase() == 'get') {
            body = null;
        }

        const res = await fetch(url, {
            method: method,
            mode: "no-cors",
            // mode: "cors",
            // body: body,
            // headers: headers,
        });

        // console.log("res: " + res.ok + ", data: " + res.msg + ", formData: " + res.formData);
        // return await res.json();
        return res;
    }
    $.request = request;

    async function callApi(params) {
        if (!$.request) throw new Error("pls confirm request already mounted");

        console.log("method: " + params.method + ", content: " + params.q)

        const res = await $.request({
            url: getServerURL() + "client=" + params.client + "&sl=" + params.sl + "&tl=" + params.tl + "&q=" + params.q,
            // method: params.method || "POST",
            headers: params.headers || {}
        })

        return res;
    }
    SERVER.callApi = callApi;

    window.SERVER = SERVER;
}();