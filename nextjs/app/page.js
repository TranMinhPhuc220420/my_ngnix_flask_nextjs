'use client'

import {registerAuthRequest} from "./requests";

export default function Home() {

  async function onSubmit (event) {
    event.preventDefault()

    const formData = new FormData(event.target)
    const res = await registerAuthRequest(formData);

    console.log(res)
  }

  return (
    <>
      <form onSubmit={onSubmit}>
        <input type="text" name="username" defaultValue={"test@plt.pro.net"} style={{margin: '0 0 10px 0'}}/>
        <br/>
        <input type="text" name="password" defaultValue={"123123"} style={{margin: '0 0 10px 0'}}/>
        <br/>
        <input type="file" name="avatar_f" style={{margin: '0 0 10px 0'}}/>
        <br/>
        <button type="submit">Submit</button>
      </form>
    </>
  );
}
