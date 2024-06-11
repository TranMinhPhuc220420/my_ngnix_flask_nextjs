'use server'

import axios from "axios";

const SERVER_URL = process.env.NEXT_PUBLIC_SERVER_URL;

/**
 * Process call request post
 *
 * @param {string} url
 * @param {object} params
 * @param {object|null} headers
 * @param {number|null} retry
 * @returns {Promise<{msg, data: null, success: boolean, code_error}|{msg: string, data: any, success: boolean}>}
 * @private
 */
export const _postRequest = async (url, params, headers, retry) => {
  try {
    const res = await axios.post(url, params, {headers: headers || null});
    const {status, statusText, data} = res;

    return {success: true, msg: statusText, data: data};

    // const response = await fetch(url, {
    //   method: 'POST',
    //   body: params || {},
    //   headers: headers || {},
    // })
    // // Handle response if necessary
    // return await response.json()

  } catch (error) {
    const {code, message} = error;
    return {success: false, code_error: code, msg: message, data: null}
  }
};

/**
 * Handler call request register new auth
 *
 * @param {FormData} formData
 * @returns {Promise<void>}
 */
export const registerAuthRequest = async (formData) => {
  // return await _postRequest(`${SERVER_URL}/api/v1/auth/register`, formData);
  return await _postRequest(`${SERVER_URL}/api/v1/auth/info`, formData);
};