import axios from "axios";


export default {
    axios: axios.create({
        baseURL: "http://127.0.0.1:8000/",
        headers: {
            "Content-Type": "application/json",
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range',
            'Access-Control-Expose-Headers': 'Content-Length,Content-Range',

        }
    })
}