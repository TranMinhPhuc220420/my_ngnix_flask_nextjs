import axios from "axios";

import {registerAuthRequest} from "./auth";

const getAccessToken = async () => {
    const res = await axios.post('http://localhost:3000/api/auth/get-access-token')
    return res.data;
};

export {
    getAccessToken,

    registerAuthRequest
};