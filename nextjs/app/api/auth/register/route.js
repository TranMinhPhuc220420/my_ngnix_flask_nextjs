// import {NextApiRequest, NextApiResponse} from "next/types";

/**
 *
 * @param {NextApiRequest} req
 * @param {NextApiResponse} res
 * @returns {Promise<Response>}
 * @constructor
 */
export async function POST(req, res) {
  // console.log(request)

  const data = req.body;
  console.log(data)

  // const username = res.get('username');
  // console.log(username)
  // const password = res.get('password');
  // console.log(password)
  // const avatar_file = res.get('avatar_f');

  // const res = await axios({
  //     method: 'post',
  //     url: 'http://127.0.0.1:5000/api/v1/auth/register',
  //     headers: {},
  //     data: {
  //         username: username,
  //         password: password,
  //         avatar_file: avatar_file,
  //     }
  // });
  //
  // return Response.json(res.data)

  // const {data} = await axios.post('http://127.0.0.1:5000/api/v1/auth/register', request.body, {
  //   responseType: "stream",
  //   headers: {
  //     "Content-Type": request.headers["content-type"], // which is multipart/form-data with boundary included
  //   },
  // });
  // data.pipe(response);

  return Response.json({message: 'ok'})
}
